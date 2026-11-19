# Boas práticas de engenharia para agentes

Este repositório é a fonte única das instruções globais e das skills de Claude Code,
Codex e OpenCode. `global/AGENTS.md` é o destino dos symlinks `~/.claude/CLAUDE.md`,
`~/.codex/AGENTS.md` e `~/.config/opencode/AGENTS.md`. `skills/` é instalado por
`python3 scripts/install.py` em `~/.claude/skills` (também lido pelo OpenCode) e
`~/.codex/skills`.

Para mudar uma skill, siga o playbook `skills/poteto-mode/playbooks/authoring-a-skill.md`.
Antes de commitar, rode:

```sh
python3 scripts/check_skills.py --fix
python3 scripts/check_skills.py
python3 scripts/install.py
```

`check_skills.py --fix` gera `agents/openai.yaml` para toda skill com
`disable-model-invocation: true`; é assim que o Codex respeita o "só invocação".
Diferenças entre providers ficam só em `skills/poteto-mode/references/harness.md`.
Registre em `UPSTREAM.md` a origem e as adaptações de tudo que vier de fora.
`skills/security-audit` é cópia fixada da Cloudflare: não edite além do que o
UPSTREAM.md documenta.
