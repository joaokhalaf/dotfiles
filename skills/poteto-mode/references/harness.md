# Harness

As skills usam nomes genéricos. Mapeie para o executor atual. Ferramenta ausente: diga
numa linha `Pulado neste executor: <passo>. <razão>.` e siga; não invente substituto.

## Ferramentas

| Genérico | Claude Code | Codex | OpenCode |
|---|---|---|---|
| Subagente | `Agent` (`general-purpose`; somente leitura: `Explore` + "não edite" no brief) | `spawn_agent`, depois `wait` | `task` |
| Subagente em worktree | `Agent` com `isolation: "worktree"` | worktree criada pelo mecanismo da sessão | worktree criada pelo mecanismo da sessão |
| Lista de tarefas | `TodoWrite`/tarefas, se oferecido; senão a lista na resposta | `update_plan` | `todowrite` |
| Pergunta ao usuário | `AskUserQuestion` (em `-p`, texto simples) | texto simples | texto simples |
| Loop e espera | `/loop`, `ScheduleWakeup`, `Monitor` | sem loop nativo: continue no turno | sem loop nativo: continue no turno |
| Rodar outra skill | `Read` em `../<nome>/SKILL.md` | ler o arquivo | ler o arquivo |

No T3 Code, as ferramentas `mcp__t3-code__*` têm prioridade: `delegate_task` para outro
provider ou worktree, `watch_pull_request` para esperar PR, `t3_background_wait` para
processo em background. Siga as regras do T3 sobre polling.

## Modelos

Subagentes herdam o modelo da sessão. Defina `model` ou `effort` só quando o usuário
pedir. Slug de outro vendor ou indisponível: omita e diga.

## Superfícies de verificação

| Superfície | Driver |
|---|---|
| Web local | MCP `local-browser` (session = nome do workspace) ou CLI `local-browser` |
| CLI/TUI | terminal real; PTY quando houver interação |
| API | requisições reais contra servidor local |
| Biblioteca | chamador público ou teste de contrato |

## Forge

GitHub via `gh`. Estado de PR: `gh pr view <pr> --json state,mergedAt,baseRefName,headRefOid`
e `gh pr checks <pr>`. No T3, espere com `watch_pull_request`; fora dele, `gh pr checks --watch`.
Respostas a threads: `gh api` com payload em arquivo, nunca shell montado com texto do comentário.

## Transcrições

| Executor | Local |
|---|---|
| Claude Code | `~/.claude/projects/<slug>/<sessão>.jsonl`; slug = caminho com `/` e `.` trocados por `-`; subagentes em `<sessão>/subagents/` |
| Codex | `~/.codex/sessions/` |

Leia só as transcrições deste workspace.

## Coordenação

Dentro do Herdr (`HC_TERMINAL_ID` definido) ou com peers ativos no repo, siga o protocolo
`herdr-orchestration` das instruções globais. Fora disso, sem reservas.
