# dotfiles

Configuração da máquina: zsh (`zsh/`), prompt Starship (`starship/`), VS Code
(`vscode/`), pacotes do Homebrew (`Brewfile`) e as regras e skills dos agentes
descritas abaixo. Um único `scripts/install.py` liga tudo em `~`.

## Regras e skills dos agentes

Regras globais e skills que entram sozinhas sempre que Claude Code, Codex ou
OpenCode começam a trabalhar num código. Nada para rodar: a instrução global
carrega o fluxo, e as skills ativam pelo seu pedido.

Base: [pstack](https://github.com/cursor/plugins/tree/main/pstack) e
[mattpocock/skills](https://github.com/mattpocock/skills), traduzidos para pt-BR e
adaptados (licenças em [LICENSE](LICENSE)).

## O que acontece quando você pede algo

1. A instrução global (`global/AGENTS.md`, ligada a `~/.claude/CLAUDE.md`,
   `~/.codex/AGENTS.md` e `~/.config/opencode/AGENTS.md`) manda seguir o
   **poteto-mode** em todo trabalho de engenharia.
2. O poteto-mode começa com o **grilling**: perguntas em rodadas, cada uma com a
   resposta recomendada, até o entendimento comum. Num repositório, termos e
   decisões difíceis de reverter viram `GLOSSARY.md` e ADRs em pt-BR.
3. Escolhe um dos 22 playbooks (bug, feature, refactor, perf, investigação,
   protótipo, retomada, PR…) e aplica os 24 princípios.
4. Verifica no artefato real (browser, terminal, API) antes de dizer que terminou.

Push e PR só com pedido. Merge só com autorização nomeando os PRs. Subagentes só
por benefício concreto, herdando o modelo da sessão.

## Instalar

```sh
brew bundle --file=Brewfile          # pacotes
python3 scripts/install.py            # links de skills, zsh, starship, instruções globais e config do Claude; copia o settings do VS Code
python3 scripts/install.py --dry-run
python3 scripts/install.py --uninstall   # troca os links de config por cópias
```

Um arquivo que já existe em `~` só vira link se tiver o mesmo conteúdo do repo; se
for diferente, o instalador reporta `skip` e não mexe. Para atualizar o Brewfile:
`brew bundle dump --file=Brewfile --force --no-winget --no-npm --no-vscode`.

O VS Code roda no Windows e não segue symlinks do WSL, então `vscode/settings.json`
é copiado para `%USERPROFILE%\AppData\Roaming\Code\User`; se o destino diferir, a versão anterior vira
`settings.json.bak`. Mudança feita pela UI do VS Code precisa voltar para o repo à
mão. Extensões ficam em `vscode/extensions.txt`; para instalar, a partir de `/mnt/c`:
`xargs -n1 cmd.exe /c code --install-extension < vscode/extensions.txt`.

`claude/` traz o `settings.json` do Claude Code (modo `acceptEdits` e status line)
e o `statusline.py`, que mostra modelo, contexto, limites de 5h e 7d e o cache.

## Worktree por tarefa

`wt <tarefa>` cria `~/work/worktrees/<repo>/<tarefa>` com a branch `<tarefa>` a
partir da main remota, copia os `.env*` ignorados do repositório principal e abre
no VS Code. `wtd <tarefa>` remove a worktree (recusa se houver mudança) e apaga a
branch só se ela já estiver na main remota.

O OpenCode lê `~/.claude/skills`. Abra uma sessão nova depois de instalar ou editar.

## Ativação

| Ativam sozinhas pelo pedido | Por `/nome` ou chamadas pelo poteto-mode |
|---|---|
| `grilling`, `domain-modeling`, `dev-verify`, `unslop`, `technical-writing`, `why`, `tdd`, `benchmark-checklist` | `poteto-mode`, `architect`, `arena`, `swarm`, `interrogate`, `no-comments`, `security-gate`, `security-audit`, `show-me-your-work`, `figure-it-out`, `correct`, `reflect`, `create-verification-skill`, `maintain-verification-skill`, `grill-me`, `grill-with-docs`, `autopilot-stack`, `autopilot-full`, `principle-*` |

Ativa sozinha o que é útil fora do fluxo de engenharia e não tem efeito externo;
o resto o poteto-mode lê por caminho quando um passo pede. No Codex, o "só
invocação" vem de `agents/openai.yaml`, gerado por `scripts/check_skills.py --fix`.

## Manter

Ver [AGENTS.md](AGENTS.md).
