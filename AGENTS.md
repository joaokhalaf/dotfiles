# dotfiles

Este repositório é a fonte única da configuração da máquina: `zsh/`, `starship/`,
`vscode/`, `Brewfile`, instruções globais e skills de Claude Code, Codex e OpenCode.
`scripts/install.py` liga os arquivos de config listados em `CONFIG` e as skills, e copia os de
`copies()` (settings do VS Code no Windows). `global/AGENTS.md` é o destino dos symlinks `~/.claude/CLAUDE.md`,
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
Mantenha em `LICENSE` o aviso de licença de tudo que vier de fora.
`skills/security-audit` é cópia fixada da Cloudflare, com licença própria em
`skills/security-audit/LICENSE`: não edite além do `disable-model-invocation: true`
no frontmatter e do `agents/openai.yaml` gerado.
