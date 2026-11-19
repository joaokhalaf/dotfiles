#!/usr/bin/env python3
"""Link factory skills into each agent's global skills directory.

Owned links point into this repo's skills/. Stale owned links are removed;
anything else at a target path is left untouched and reported.
"""
import argparse
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'
DESTS = [Path.home() / '.claude/skills', Path.home() / '.codex/skills']


def owned(path):
    return path.is_symlink() and Path(os.readlink(path)).is_relative_to(SKILLS)


def plan(dest, sources, uninstall):
    wanted = {} if uninstall else {s.name: s for s in sources}
    actions = []
    if dest.is_dir():
        for path in sorted(dest.iterdir()):
            if owned(path) and Path(os.readlink(path)) != wanted.get(path.name):
                actions.append(('remove', path, None))
    for name, source in wanted.items():
        target = dest / name
        if owned(target) and Path(os.readlink(target)) == source:
            continue
        if os.path.lexists(target) and not owned(target):
            actions.append(('skip', target, None))
        else:
            actions.append(('link', target, source))
    return actions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, action='append', help='override destinations (repeatable)')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--uninstall', action='store_true')
    args = parser.parse_args()
    sources = sorted(p for p in SKILLS.iterdir() if (p / 'SKILL.md').is_file())
    for dest in [d.expanduser().absolute() for d in args.dest or DESTS]:
        actions = plan(dest, sources, args.uninstall)
        for kind, target, source in actions:
            print(f'{kind:6} {target}' + (f' -> {source}' if source else ''))
            if args.dry_run or kind == 'skip':
                continue
            if kind == 'remove':
                target.unlink()
            else:
                dest.mkdir(parents=True, exist_ok=True)
                if os.path.lexists(target):
                    target.unlink()
                target.symlink_to(source, target_is_directory=True)
        print(f'{dest}: {sum(1 for p in dest.iterdir() if owned(p)) if dest.is_dir() else 0} factory skills')


if __name__ == '__main__':
    main()
