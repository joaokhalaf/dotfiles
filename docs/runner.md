# Runner de terminal (opcional)

scripts/factory.py continua disponível para quem quiser execução em lote. Ele
controla uma sequência fixa e mantém SQLite, worktrees e logs. A conversa não
depende dele. As seções seguintes documentam somente essa opção de execução.

## Providers e perfis

O runner chama as CLIs em modo não interativo. Cada etapa é um processo novo, com
`PWD` igual à worktree da tarefa.

| Provider | Autor | Revisor | Relatório |
|---|---|---|---|
| `claude` | `claude -p` com as permissões existentes, `--permission-prompts none` | idem; somente leitura por instrução, não por sandbox | `--json-schema` (saída estruturada) |
| `codex` | `codex exec --sandbox workspace-write` | `codex exec --sandbox read-only` | `--output-schema` |
| `opencode` | `opencode run --agent build` | `opencode run --agent plan` (sem edição) | JSON pedido no prompt, lido da última mensagem |

`factory.example.json` traz os perfis `claude` (padrão), `codex`, `opencode` e
`misto` (autor Claude, revisores Codex e OpenCode). `model: null` herda o padrão de
cada CLI; no OpenCode, `model` usa o formato `provider/modelo`. Revisões do mesmo
provider são sessões independentes, não multi-modelo. Não há fallback silencioso
de modelo ou provider.

```sh
python3 scripts/factory.py --config factory.local.json --profile misto doctor
```

Os adapters estão em `scripts/providers.py`. Adicionar um provider exige
implementar `build`/`parse`/`authenticated` e testes, sem alterar fila ou skills.
Todos os agentes leem `skills/poteto-mode/worker.md` pelo caminho absoluto; as
skills globais instaladas por `scripts/install.py` ficam disponíveis do mesmo jeito.

## Configurar um projeto

Requisitos: Git, Python 3, CLI do provider autenticada e ferramentas de validação do projeto.
Herdr e MCPs são integrações opcionais. gh autenticado é necessário na entrega de PRs, não para escrever código.
Copie factory.example.json para factory.local.json e defina repo/base reais. Faça
fetch e confira a base local: o runner não atualiza nem troca branches automaticamente.

Defina prepare (opcional), checks e behavior_checks como arrays argv, sem shell:

```json
{
  "prepare": [["pnpm", "install", "--frozen-lockfile"]],
  "checks": [["pnpm", "run", "ci"], ["pnpm", "run", "check-types"], ["pnpm", "run", "build"]],
  "behavior_checks": [["pnpm", "test"]]
}
```

Use comandos reais do projeto; tipos/build não substituem prova comportamental.
Os dois grupos de checks são obrigatórios. Instalação e serviços precisam funcionar
na worktree. Para browser use local-browser e ambiente isolado; jamais produção
como fixture. Checks não executados não contam como aprovação.

Card JSON:

```json
{
  "title": "Correção pequena",
  "goal": "Comportamento desejado",
  "acceptance": ["Critério observável"],
  "scope": ["src/auth/*", "tests/login/*"],
  "depends_on": []
}
```

Scope usa fnmatch em caminhos relativos Git. O host rejeita mudanças fora do escopo
antes de fazer commit. Dependências referenciam ids anteriores e só liberam depois
de merged confirmado. Stacks de branches antes do merge são conduzidos pelo
coordenador, não pelo runner inicial.

```sh
python3 scripts/factory.py --config factory.local.json enqueue card-1.json
python3 scripts/factory.py --config factory.local.json enqueue card-2.json
python3 scripts/factory.py --config factory.local.json run
python3 scripts/factory.py --config factory.local.json status
```

run é uma entrada do operador no terminal; não deve ser lançado por um agente para
contornar as ferramentas de delegação do harness. Inicia até duas tarefas elegíveis
e termina. O autor escreve na worktree; o host confere escopo e cria o commit.
Depois executa checks e revisões no SHA exato. Novo head, checkout sujo, reprovação
ou revisão sem evidência bloqueiam a tarefa.

Codex usa workspace-write para autor e read-only para revisores. Claude e OpenCode
usam as permissões existentes, sem bypass; restrições podem bloquear ferramentas no
modo não interativo. O revisor OpenCode usa o agente `plan`, que nega edições; o
revisor Claude é somente leitura por instrução, não por sandbox. MCPs também mantêm
suas permissões reais. Não flexibilize gates para conseguir verde.

## Entrega e retomada

Estados: queued → running → verified_local → pr_open → pr_verified → merged;
falhas ficam blocked. verified_local ainda não é um PR pronto. Passe ids, worktrees,
SHAs e logs ao coordenador autopilot-stack para publicar apenas os itens autorizados.
Depois registre links reais:

```sh
python3 scripts/factory.py --config factory.local.json record-pr 1 https://github.com/ORG/REPO/pull/123
python3 scripts/factory.py --config factory.local.json sync-pr 1
```

Esses comandos consultam GitHub; confirmam repo/base/head. pr_verified exige checks
presentes e verdes; não significa aprovação humana ou autorização de merge. Após
merge humano, sync-pr atualiza merged. Mudanças de configuração invalidam a
verificação registrada. Nenhum comando deste runner faz merge.

```sh
python3 scripts/factory.py --config factory.local.json stop
python3 scripts/factory.py --config factory.local.json resume
python3 scripts/factory.py --config factory.local.json retry 1
```

STOP e SIGINT/SIGTERM interrompem a etapa ativa. Logs e worktrees são preservados.
retry exige blocked e tentativas restantes. Após queda abrupta, confira processos
antigos antes de `recover 1 --confirm-no-live-processes`; depois execute run.
Lock impede dois runners na mesma fila. Não use cópias deste setup concorrentes
contra o mesmo repo, pois seus locks não se comunicam.

## Limites, logs e consumo

Estado em .factory/<hash-do-repo>/: SQLite, worktrees e logs por tarefa/tentativa,
com prompts, relatórios, comandos, tokens e ids de sessão quando disponíveis.
Padrão: duas tentativas, 30 minutos por etapa e seis chamadas por rodada.

Claude informa custo estimado quando disponível; Codex e OpenCode fornecem tokens, sem converter
para USD. max_estimated_usd_per_run é um limite de admissão entre chamadas, não um
teto rígido: chamadas em andamento podem excedê-lo. Com limite monetário configurado
e sem telemetria, novas chamadas bloqueiam; deixe null para Codex e OpenCode. Tokens e custo não
medem saldo nem cota da assinatura. Não há retry infinito.

