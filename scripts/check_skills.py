#!/usr/bin/env python3
"""Validate skills: frontmatter, relative links and **skill-name** references."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'skills'
LINK = re.compile(r'\]\(([^)#\s]+)(?:#[^)]*)?\)')
SKILL_REF = re.compile(r'\*\*([a-z0-9]+(?:-[a-z0-9]+)+|[a-z]{3,})\*\*')


def frontmatter(text):
    if not text.startswith('---\n'):
        return None
    end = text.find('\n---', 4)
    return None if end < 0 else dict(
        line.split(':', 1) for line in text[4:end].splitlines() if ':' in line)


def main():
    skills = {p.name for p in ROOT.iterdir() if (p / 'SKILL.md').is_file()}
    errors, missing = [], {}
    for skill in sorted(skills):
        meta = frontmatter((ROOT / skill / 'SKILL.md').read_text())
        if not meta or meta.get('name', '').strip() != skill or not meta.get('description', '').strip():
            errors.append(f'{skill}/SKILL.md: frontmatter needs name: {skill} and a description')
    vendored = {p.parent for p in ROOT.glob('*/LICENSE')}
    for md in sorted(ROOT.rglob('*.md')):
        if md.parent in vendored:
            continue
        text = md.read_text()
        for target in LINK.findall(text):
            if '://' not in target and not (md.parent / target).exists():
                errors.append(f'{md.relative_to(ROOT)}: broken link {target}')
        for name in SKILL_REF.findall(text):
            if name not in skills:
                missing.setdefault(name, set()).add(str(md.relative_to(ROOT)))
    for name, files in sorted(missing.items()):
        errors.append(f'missing skill {name} (referenced by {len(files)} files, e.g. {sorted(files)[0]})')
    print('\n'.join(errors) or f'ok: {len(skills)} skills')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
