### Pausa segura

**Você é dono de uma parada limpa. Deixe um checkpoint de onde um agente frio possa retomar.** Só quando pedido. Com "continue", "vou dormir, continue" ou "não pare", não pause.

1. Pare numa fronteira segura. Termine o passo atômico atual ou desfaça-o. Não comece nada novo e cancele subagentes aninhados.
2. Nenhuma ação irreversível para pausar. Sem PR e sem push, salvo se já havia um.
3. Torne o trabalho durável. Edições não commitadas viram um commit `wip:` na branch atual. Árvore quebrada: diga numa linha no corpo do commit.
4. Escreva a nota de retomada fora do contexto, em arquivo (ex.: `<scratch>/<slug>-resume.md` ou `runs/<slug>.md` no repo quando for durável): intenção, o que fazia, progresso e o que está verificado (com SHA ou hash), estado atual, próximos passos, arquivos-chave, pegadinhas. Se existe trilha **show-me-your-work**, aponte para ela.

**Resposta:** onde está no loop, o que está em disco vs só na cabeça (caminhos, sem dumps de diff), commits feitos e se a árvore está limpa, a primeira ação ao retomar. É uma pausa, não relatório final.
