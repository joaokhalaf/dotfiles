# Primeira rodada: esports-simulator

Repo: /home/khalaf/work/esports-simulator; base master, inspecionada no commit
32a5e9569f37c1eea936b715942b0db583151755. Checkout principal estava limpo.
Há outra worktree de homepage em andamento; não reutilizá-la para a factory.

Dois cards independentes, somente testes de contratos públicos:

1. worlds-validation.json: invariantes de snapshots Worlds, arquivo próprio.
2. americas-draft.json: leitura de drafts Americas válidos/malformados, arquivo próprio.

Não introduzem funcionalidades ou regras novas. Se revelarem defeito de produção,
o agente deve reportar a reprodução, sem ampliar a mudança além do arquivo autorizado.

## Baseline observado

- 22 testes de domínio/adaptador passaram, sem banco ou rede.
- Biome CI passou, com 20 avisos preexistentes.
- API check-types passou.
- Claude Code estava sem login; GitHub CLI autenticado. Nenhum agente foi executado.

A instalação das dependências é repetida em cada worktree, com lockfile congelado.
Checks: Biome, API tipos/build, pnpm test (inclui os novos arquivos automaticamente).
O teste PostgreSQL pode ser SKIP sem TEST_DATABASE_URL; isso não equivale a integração
validada. CI completo, browser e Worker continuam necessários para entregar o PR;
essa rodada não os declara aprovados pela validação local de domínio.

## Executar no terminal do operador

Perfil home usa Codex, já autenticado via ChatGPT neste WSL. Não depende de login
do Claude. Para usar no trabalho, selecione --profile work e autentique a CLI Claude
no ambiente do trabalho. Nenhuma credencial é copiada.

As duas tarefas estão enfileiradas. Para iniciar:

```sh
cd /home/khalaf/work/home-dev-setup
python3 scripts/factory.py --config pilots/esports-simulator/factory.local.json status
python3 scripts/factory.py --config pilots/esports-simulator/factory.local.json run
```

O runner inicia o provider selecionado com as permissões/sandbox existentes. Se uma ferramenta precisar
de permissão que não possa ser concedida em modo não interativo, a tarefa deve
bloquear e mostrar os logs. Não habilitar bypass como solução automática.

Após verified_local, abra uma sessão de qualquer provider (as skills são globais) e
use /autopilot-stack com os ids, SHAs e logs da rodada para entregar
PRs verificados. Sem merge. Não rodar factory.py de dentro do agente para delegar.

Configuração local é ignorada no Git por conter caminho desta máquina. Para levar
a outro WSL, copie factory.example.json e ajuste o caminho e checks; os cards são
versionáveis. Estado, logs e worktrees ficam em .factory no repositório do setup.

## Execução independente do Herdr

O piloto usa coordination local. A primeira tentativa foi bloqueada antes de
editar porque o contrato antigo exigia Herdr. A exigência foi removida para este
modo. Logs e limites de tentativas são preservados; retry é explícito e não inicia
agentes. Use retry 1 e retry 2, depois run, com a mesma configuração.
