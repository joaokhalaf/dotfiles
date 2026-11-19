# Runner de terminal (opcional)

scripts/factory.py continua disponível para quem quiser execução em lote. Ele
controla uma sequência fixa e mantém SQLite, worktrees e logs. A conversa não
depende dele. As seções seguintes documentam somente essa opção de execução.

## Trocar provider

factory.example.json oferece dois perfis. O piloto já está configurado em
[pilots/esports-simulator](../pilots/esports-simulator/README.md).

```sh
python3 scripts/factory.py --config pilots/esports-simulator/factory.local.json --profile home doctor
python3 scripts/factory.py --config pilots/esports-simulator/factory.local.json --profile work doctor
```

home é o padrão: Codex com modelo herdado da CLI e duas revisões em sessões novas
com focos distintos. São revisões independentes do mesmo modelo padrão; não se
apresentam como multi-modelo. work usa Claude, autor Sonnet e revisores Sonnet/Opus.
Para modelos distintos no Codex, defina `model` nos reviewers conforme seu acesso.
Não há fallback silencioso de modelo ou provider.

Cada perfil define:

```json
{
  "executor": {"provider": "codex", "model": null},
  "reviewers": [
    {"provider": "codex", "model": null, "focus": "contratos e entradas inválidas"},
    {"provider": "codex", "model": null, "focus": "regressões e critérios de aceite"}
  ]
}
```

Os adapters estão em scripts/providers.py; normalizam execução, resultado e uso.
Adicionar um provider exige implementar esse contrato e testes, sem alterar fila
ou playbooks. Podem-se configurar providers diferentes por lane. Configurações
anteriores author_model/review_models continuam aceitas como Claude.

## Usar skills no terminal ou em uma interface de agente

Codex: peça ao coordenador para ler o SKILL.md desejado em skills/ e o contrato
skills/poteto-mode/references/runtime.md. O runner fornece caminhos absolutos aos
agentes, sem depender do carregador de plugins do Claude.

Claude Code no repositório alvo:

```sh
claude --plugin-dir /home/khalaf/work/home-dev-setup
```

Use /home-factory:poteto-mode ou /home-factory:autopilot-stack.
Alternativa para comandos sem namespace: `python3 scripts/install.py --dest
/caminho/projeto/.claude/skills`. Não use as duas formas na mesma sessão. O instalador
não sobrescreve arquivos existentes. Abra sessão nova após editar skills.

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

Codex usa workspace-write para autor e read-only para revisores. Claude usa as
permissões existentes, sem bypass; restrições podem bloquear ferramentas no modo
não interativo. O contrato de leitura dos revisores Claude é instrução, não sandbox.
MCPs também mantêm suas permissões reais. Não flexibilize gates para conseguir verde.

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

Claude informa custo estimado quando disponível; Codex fornece tokens, sem converter
para USD. max_estimated_usd_per_run é um limite de admissão entre chamadas, não um
teto rígido: chamadas em andamento podem excedê-lo. Com limite monetário configurado
e sem telemetria, novas chamadas bloqueiam; deixe null para Codex. Tokens/custo não
medem saldo de assinatura ou cota restante do Max 5x. Não há retry infinito.

