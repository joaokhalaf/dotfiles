#!/usr/bin/env python3
import base64
import json
import mimetypes
import os
import pathlib
import shutil
import subprocess
import sys

ACTIONS = ['open', 'snapshot', 'click', 'fill', 'press', 'hover', 'scroll', 'screenshot', 'console', 'errors', 'get',
           'back', 'reload', 'eval']
SCHEMA = {
    'type': 'object',
    'properties': {
        'action': {'type': 'string', 'enum': ACTIONS},
        'args': {'type': 'array', 'items': {'type': 'string'}},
        'session': {'type': 'string', 'description': 'Workspace name. Use the same name to share a browser across '
                                                     'agents; different names isolate tasks.'},
    },
    'required': ['action'],
    'additionalProperties': False,
}
TOOL = {
    'name': 'browser',
    'description': 'Navigate and test local web apps in Chromium. open URL, snapshot for @refs, click/fill refs, '
                   'screenshot path, console/errors, eval JS. args are individual CLI arguments. Default session '
                   'local-validation. Start the app server before opening localhost. Snapshot after navigation; '
                   'refs may change.',
    'inputSchema': SCHEMA,
}
BIN = shutil.which('local-browser') or str(pathlib.Path.home() / '.local/bin/local-browser')
TIMEOUT = 60


def failure(text):
    return {'content': [{'type': 'text', 'text': text}], 'isError': True}


def call(arguments):
    if not isinstance(arguments, dict):
        return failure('arguments must be an object')
    action, args, session = arguments.get('action'), arguments.get('args', []), arguments.get('session')
    if action not in ACTIONS:
        return failure(f'action must be one of: {", ".join(ACTIONS)}')
    if not isinstance(args, list) or not all(isinstance(a, str) for a in args):
        return failure('args must be a list of strings')
    if session is not None and not isinstance(session, str):
        return failure('session must be a string')
    env = os.environ.copy()
    runtime_dir = pathlib.Path('/run/user') / str(os.getuid())
    if 'XDG_RUNTIME_DIR' not in env and runtime_dir.is_dir():
        env['XDG_RUNTIME_DIR'] = str(runtime_dir)
    try:
        r = subprocess.run([BIN, '--task', session or 'local-validation', action, *args], capture_output=True,
                           text=True, env=env, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return failure(f'{action} timed out after {TIMEOUT}s')
    except OSError as e:
        return failure(str(e))
    content = [{'type': 'text', 'text': r.stdout + r.stderr or 'Done'}]
    shot = next((pathlib.Path(a) for a in reversed(args) if not a.startswith('-')), None)
    if action == 'screenshot' and r.returncode == 0 and shot and shot.is_file():
        mime = mimetypes.guess_type(shot.name)[0] or 'image/png'
        content.append({'type': 'image', 'mimeType': mime, 'data': base64.b64encode(shot.read_bytes()).decode()})
    return {'content': content, 'isError': r.returncode != 0}


class MethodNotFound(Exception):
    pass


def respond(req):
    method, params = req.get('method'), req.get('params') or {}
    if method == 'initialize':
        return {'protocolVersion': params.get('protocolVersion', '2024-11-05'), 'capabilities': {'tools': {}},
                'serverInfo': {'name': 'local-browser', 'version': '2.0.0'}}
    if method == 'ping':
        return {}
    if method == 'tools/list':
        return {'tools': [TOOL]}
    if method == 'tools/call':
        if params.get('name') != 'browser':
            return failure(f'unknown tool: {params.get("name")}')
        return call(params.get('arguments', {}))
    raise MethodNotFound(method)


for line in sys.stdin:
    try:
        req = json.loads(line)
    except ValueError:
        continue
    if not isinstance(req, dict) or 'id' not in req:
        continue
    try:
        out = {'jsonrpc': '2.0', 'id': req['id'], 'result': respond(req)}
    except MethodNotFound as e:
        out = {'jsonrpc': '2.0', 'id': req['id'], 'error': {'code': -32601, 'message': f'Method not found: {e}'}}
    except Exception as e:
        out = {'jsonrpc': '2.0', 'id': req['id'], 'error': {'code': -32603, 'message': str(e)}}
    print(json.dumps(out), flush=True)
