#!/usr/bin/env python3
"""Link this repo's skills and config files into the home directory.

Owned links point into this repo. Stale owned skill links are removed. A regular
file at a config target is replaced only when its content matches the repo copy;
anything else at a target path is left untouched and reported. Uninstall turns
config links back into plain copies so the shell keeps working. Files from
copies() are copied instead of linked (VS Code on Windows can't follow WSL links);
a differing target is saved as <name>.bak before being overwritten.
"""
import argparse
import filecmp
import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'
HOME = Path.home()
SKILL_DESTS = [HOME / '.claude/skills', HOME / '.codex/skills']
CONFIG = {
    HOME / '.zshrc': ROOT / 'zsh/.zshrc',
    HOME / '.zshenv': ROOT / 'zsh/.zshenv',
    HOME / '.config/starship.toml': ROOT / 'starship/starship.toml',
    HOME / '.claude/CLAUDE.md': ROOT / 'global/AGENTS.md',
    HOME / '.claude/settings.json': ROOT / 'claude/settings.json',
    HOME / '.claude/statusline.py': ROOT / 'claude/statusline.py',
    HOME / '.codex/AGENTS.md': ROOT / 'global/AGENTS.md',
    HOME / '.config/opencode/AGENTS.md': ROOT / 'global/AGENTS.md',
}


def vscode_user_dir():
    if shutil.which('cmd.exe') and shutil.which('wslpath'):
        # %APPDATA% can be redirected by the launching app (T3 points it elsewhere); %USERPROFILE% is stable.
        profile = subprocess.run(['cmd.exe', '/c', 'echo %USERPROFILE%'], capture_output=True, text=True,
                                 cwd='/mnt/c').stdout.strip()
        return Path(subprocess.run(['wslpath', '-u', profile], capture_output=True, text=True,
                                   check=True).stdout.strip()) / 'AppData/Roaming/Code/User'
    return HOME / '.config/Code/User'


def copies():
    return {vscode_user_dir() / 'settings.json': ROOT / 'vscode/settings.json'}


def owned(path, base=ROOT):
    return path.is_symlink() and Path(os.readlink(path)).is_relative_to(base)


def plan_skills(dest, sources, uninstall):
    wanted = {} if uninstall else {s.name: s for s in sources}
    actions = []
    if dest.is_dir():
        for path in sorted(dest.iterdir()):
            if owned(path, SKILLS) and Path(os.readlink(path)) != wanted.get(path.name):
                actions.append(('remove', path, None))
    for name, source in wanted.items():
        target = dest / name
        if owned(target, SKILLS) and Path(os.readlink(target)) == source:
            continue
        if os.path.lexists(target) and not owned(target, SKILLS):
            actions.append(('skip', target, None))
        else:
            actions.append(('link', target, source))
    return actions


def plan_config(uninstall):
    actions = []
    for target, source in CONFIG.items():
        if uninstall:
            if owned(target):
                actions.append(('copy', target, source))
        elif owned(target) and Path(os.readlink(target)) == source:
            continue
        elif not os.path.lexists(target) or owned(target):
            actions.append(('link', target, source))
        elif target.is_file() and not target.is_symlink() and filecmp.cmp(target, source, shallow=False):
            actions.append(('link', target, source))
        else:
            actions.append(('skip', target, None))
    return actions


def plan_copies(uninstall):
    if uninstall:
        return []
    return [('copy', target, source) for target, source in copies().items()
            if not (target.is_file() and filecmp.cmp(target, source, shallow=False))]


def apply(kind, target, source):
    if kind == 'remove':
        target.unlink()
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    if kind == 'copy' and target.is_file() and not target.is_symlink():
        shutil.copy2(target, target.with_name(target.name + '.bak'))
    if os.path.lexists(target):
        target.unlink()
    if kind == 'copy':
        shutil.copy2(source, target)
    else:
        target.symlink_to(source, target_is_directory=source.is_dir())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, action='append', help='override skill destinations (repeatable); skips config files')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--uninstall', action='store_true')
    args = parser.parse_args()
    sources = sorted(p for p in SKILLS.iterdir() if (p / 'SKILL.md').is_file())
    actions = [a for dest in [d.expanduser().absolute() for d in args.dest or SKILL_DESTS]
               for a in plan_skills(dest, sources, args.uninstall)]
    if not args.dest:
        actions += plan_config(args.uninstall) + plan_copies(args.uninstall)
    for kind, target, source in actions:
        print(f'{kind:6} {target}' + (f' -> {source}' if source else ''))
        if not args.dry_run and kind != 'skip':
            apply(kind, target, source)
    skipped = sum(1 for kind, *_ in actions if kind == 'skip')
    print(f'{len(actions) - skipped} changes, {skipped} skipped' + (' (dry run)' if args.dry_run else ''))


if __name__ == '__main__':
    main()
