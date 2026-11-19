### Retomada de sessão

**Você é dono do ponto de retomada. Leia a trilha anterior; não a refaça.**

1. Localize a trilha anterior: transcrição local (caminhos em [harness](../references/harness.md); só deste workspace), registro de estado em Markdown, thread do T3 ou branch publicada. Leia primeiro a visão geral e as últimas mensagens, depois volte aos pontos de decisão. Transcrição longa vai para um subagente; a linha do tempo reduzida fica no main.
2. Reconstrua o estado operacional: branch e worktree, o que já entrou (`git log`, `git diff` contra a base), tarefas abertas, decisões tomadas, processos ou agentes ainda ativos. A trilha anterior é entrada autoritativa; resista a rederivá-la.
3. Compare feito vs pendente. Nomeie o ponto de retomada; não reexecute a repro anterior nem refaça trabalho concluído.
4. Rote o restante para o playbook correspondente e escolha o veredito: continuar, entregar uma recomendação pronta, ratificar ou sobrepor uma conclusão, ou fazer postmortem. Este playbook termina aqui.
5. Verifique as alegações herdadas contra o objetivo original no artefato real (**principle-prove-it-works**). Autodeclaração anterior não é prova.

Trabalho suspenso pelo usuário só retoma com instrução explícita.

**Resposta:** onde o agente anterior parou, o que herdou vs refez (idealmente nada), o ponto de retomada e o resultado.
