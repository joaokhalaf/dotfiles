# Factory conduzida pelo chat

A camada de [segurança](skills/security-review/SKILL.md) seleciona revisão focada
por risco e gates específicos do projeto. A skill [Cloudflare security-audit](skills/security-audit/SKILL.md)
está preservada em versão fixa para auditorias completas solicitadas, com licença
e validadores upstream. Funciona como instruções para Codex/Claude; não depende
do runner Python. Para Claude: /home-factory:security-review ou
/home-factory:security-audit. Para Codex, leia o respectivo SKILL.md.

Use a [política por projeto](skills/security-review/references/project-policy.md)
para definir scanners de segredos, dependências e código, gatilhos e bloqueios.
Esses scanners ainda não foram instalados nos aplicativos. Esta integração não
fornece sandbox de auditoria nem agenda execuções periódicas.

O agente principal da conversa escolhe o fluxo e executa ou delega conforme a tarefa.
Skills orientam o método; ferramentas do executor permitem agir. Não é necessário
iniciar Python, criar cards JSON ou usar Herdr para começar.

## Começar nesta conversa

Neste repositório, AGENTS.md aponta para skills/poteto-mode/SKILL.md. Você pode pedir:

> Use poteto-mode para melhorar esta factory. Trabalhe direto no que for pequeno,
> delegue quando ajudar e valide o resultado. Registre o necessário para retomar.

O main conduz investigação, arquitetura, implementação e verificação conforme a
necessidade. Swarm e interrogate são opcionais; autopilot-stack entra quando você
pedir PRs e autopilot-full apenas para merges autorizados. Correct/reflect servem
para melhorar o processo com evidências, não para acumular regras após cada tarefa.

Para outra pasta com Codex, peça para ler o caminho absoluto de
skills/poteto-mode/SKILL.md deste setup. Para Claude Code, carregue o plugin:

```sh
claude --plugin-dir /home/khalaf/work/home-dev-setup
```

Então use /home-factory:poteto-mode. Desktop só conduz ações que a sessão realmente
oferecer: acesso ao projeto, execução e delegação não são fornecidos pelas skills.
Não instalamos uma extensão de Desktop. Sem delegação, o main faz o possível e
identifica a lacuna; não inicia um runner para contornar limitações do executor.

## Primeira rodada na própria factory

O registro em [runs/chat-first.md](runs/chat-first.md) acompanha escopo, decisões,
evidências e retomada desta adaptação. As duas tarefas antigas do esports estão
suspensas por direção do usuário; seus testes gerados, logs e worktrees são preservados.
Nenhum comando abaixo deve ser executado para retomá-las por conta própria.

## Runner auxiliar, uso explícito pelo terminal

scripts/factory.py continua disponível para quem quiser execução em lote. Ele
controla uma sequência fixa e mantém SQLite, worktrees e logs. A conversa não
depende dele. As seções seguintes documentam somente essa opção de execução.

## Trocar provider

factory.example.json oferece dois perfis. O piloto já está configurado em
[pilots/esports-simulator](pilots/esports-simulator/README.md).

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

## Melhorar o ambiente para agentes

Architect centraliza operações de domínio. Correct prefere API → tipos → lint/CI →
testes → documentação. Reflect ajusta as skills com base em evidência de rodadas.
Restrições a useEffect e comentários são definidas por projeto, com alternativas
e exceções justificadas; não foram aplicados banimentos globais nos seus apps.

## Replicar e validar

Copie/versione as fontes sem .factory, .claude, configurações pessoais ou credenciais.
No trabalho instale/autentique Claude e gh, use --profile
work. Ajuste apenas caminho do projeto e seus checks. Não copie históricos/tokens.

```sh
claude plugin validate .
python3 -m unittest discover -s tests -v
```

Testes usam Git/worktrees/checks reais com respostas simuladas dos providers.
Execução com modelos e validação remota de PRs continuam sendo etapas do piloto.

## Coordenação portátil

`coordination: "local"` é o padrão. O runner possui lock, worktrees separadas,
escopo e logs próprios; os agentes não precisam chamar Herdr ou qualquer MCP.
`coordination: "herdr"` ativa o protocolo externo e bloqueia se faltar acesso.
Não é feito fallback após uma reserva negada. Políticas obrigatórias específicas
do repositório continuam sendo respeitadas em qualquer modo.

Claude Code Desktop pode usar as skills numa sessão com acesso ao repositório
e às ferramentas locais necessárias. Este projeto não instala uma extensão de
Desktop nem configura sua integração: a fila Python continua executável pelo
terminal. Herdr é apenas uma das interfaces possíveis.

BLOCKED/ISSUES agora exibem o resumo do agente no campo error, com o caminho do
log. Relatórios inválidos são identificados separadamente. Uma recusa correta do
agente não é tratada como erro de formato.

## Regras de qualidade

A [política](skills/poteto-mode/references/quality.md) proíbe novas ocorrências de
useEffect e evita quase todos os comentários explicativos. APIs de domínio, tipos
e checks automáticos devem substituir decisões ambíguas e regras só em texto.

Use no-comments para revisar comentários/workarounds no diff. Use
create-verification-skill para gerar um procedimento específico do projeto com
launch, doctor, driver real, mapa de jornadas, evidências e cleanup. A skill gerada
só é considerada comprovada depois de executar uma jornada end-to-end.

Estas skills já estão nas fontes carregadas pelo plugin Claude; para Codex, leia
os respectivos SKILL.md pelo caminho local. O lint de um app React ainda precisa
ser configurado e testado naquele app; nenhuma aplicação foi modificada nesta rodada.
