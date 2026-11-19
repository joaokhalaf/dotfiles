# Estado para retomar pelo chat

Use um arquivo Markdown pequeno no projeto quando a tarefa atravessar sessões,
for pausada ou tiver vários agentes/artefatos. Prefira atualizar um registro existente.
Não crie um arquivo para cada operação trivial nem exija scripts para editá-lo.

Registre apenas o necessário:

- Objetivo, escopo e critérios de aceite atuais.
- Estado das tarefas: pendente, em andamento, verificada, bloqueada ou suspensa.
- Decisões e autorizações relevantes; o que ainda exige decisão humana.
- Arquivos/branches/worktrees/PRs envolvidos e dono ativo, quando houver.
- Comandos/resultados e SHA ou hash do conteúdo que foi verificado.
- Bloqueios, trabalho preservado e próximo passo concreto.

Na retomada, confira checkout/diff, processos ou agentes ainda ativos e validade
das evidências. Sem histórico verificável, trate a informação como hipótese.
Não reexecute trabalho suspenso sem instrução de retomar. Não copie credenciais
nem transcrições inteiras. O registro informa o coordenador; não executa tarefas.
