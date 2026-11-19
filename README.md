# Boas práticas de engenharia para agentes

Regras globais e skills que entram sozinhas sempre que Claude Code, Codex ou
OpenCode começam a trabalhar num código. Nada para rodar: a instrução global
carrega o fluxo, e as skills ativam pelo seu pedido.

Base: [pstack](https://github.com/cursor/plugins/tree/main/pstack) e
[mattpocock/skills](https://github.com/mattpocock/skills), traduzidos para pt-BR e
adaptados (origem e mudanças em [UPSTREAM.md](UPSTREAM.md)).

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
python3 scripts/install.py            # links em ~/.claude/skills e ~/.codex/skills
python3 scripts/install.py --dry-run
python3 scripts/install.py --uninstall
```

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
