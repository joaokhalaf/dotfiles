# Factory

Regras globais e skills de engenharia para Claude Code, Codex e OpenCode, a partir
de uma única fonte. Base: [pstack](https://github.com/cursor/plugins/tree/main/pstack)
e [mattpocock/skills](https://github.com/mattpocock/skills), traduzidos para pt-BR e
adaptados (origem e mudanças em [UPSTREAM.md](UPSTREAM.md)).

## Como funciona

- `global/AGENTS.md` é a instrução global dos três providers, via symlinks em
  `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md` e `~/.config/opencode/AGENTS.md`.
- Em trabalho de engenharia, a instrução global manda seguir o **poteto-mode**. Ele
  começa com o **grilling** (entrevista em rodadas até o entendimento comum; num repo,
  com glossário e ADRs em pt-BR), escolhe um dos 22 playbooks e aplica os 24 princípios.
- Push e PR só com pedido. Merge só com autorização nomeando os PRs.
- Subagentes só por benefício concreto, herdando o modelo da sessão.

## Instalar

```sh
python3 scripts/install.py            # links em ~/.claude/skills e ~/.codex/skills
python3 scripts/install.py --dry-run
python3 scripts/install.py --uninstall
```

Abra uma sessão nova depois de instalar ou editar skills.

## Ativação

| Ativam sozinhas pelo pedido | Só por invocação (`/nome`) ou chamadas pelo poteto-mode |
|---|---|
| `grilling`, `domain-modeling`, `dev-verify`, `unslop`, `technical-writing`, `why`, `tdd`, `benchmark-checklist` | `poteto-mode`, `architect`, `arena`, `swarm`, `interrogate`, `no-comments`, `security-gate`, `security-audit`, `show-me-your-work`, `figure-it-out`, `correct`, `reflect`, `create-verification-skill`, `maintain-verification-skill`, `grill-me`, `grill-with-docs`, `autopilot-stack`, `autopilot-full`, `principle-*` |

O critério: ativa sozinha o que é útil fora do fluxo de engenharia e não tem efeito
externo; o resto o poteto-mode lê por caminho quando um passo pede. No Codex, o "só
invocação" vem de `agents/openai.yaml`, gerado por `scripts/check_skills.py --fix`.

## Manter

Ver [AGENTS.md](AGENTS.md). O runner de terminal opcional está em [docs/runner.md](docs/runner.md).
