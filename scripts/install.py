#!/usr/bin/env python3
"""Link local Claude Code skills without replacing existing configuration."""
import argparse
import os
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, default=Path.home() / '.claude/skills')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--uninstall', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    sources = sorted((root / 'skills').iterdir())
    pairs = [(source, args.dest.expanduser().absolute() / source.name)
             for source in sources if (source / 'SKILL.md').is_file()]
    # Preflight every path before changing anything.
    for source, target in pairs:
        exists = os.path.lexists(target)
        owned = target.is_symlink() and target.resolve() == source.resolve()
        if exists and not owned and not args.uninstall:
            parser.error(f'Existing path left untouched: {target}')
    for source, target in pairs:
        owned = target.is_symlink() and target.resolve() == source.resolve()
        if args.uninstall:
            if owned:
                print(f'Remove {target}')
                if not args.dry_run:
                    target.unlink()
        elif not owned:
            print(f'Link {target} -> {source}')
            if not args.dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.symlink_to(source, target_is_directory=True)
        else:
            print(f'Already installed: {target}')


if __name__ == '__main__':
    main()
