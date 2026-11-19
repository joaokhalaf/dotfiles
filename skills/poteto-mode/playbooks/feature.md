### Feature

**Você é dono do design. Planeje, revise, verifique.**

1. Rastreie o subsistema afetado.
2. `architect` para o formato.
3. Escreva o checkpoint de throughput como quatro itens na lista de tarefas. Uma dimensão que não se aplica mantém o item com `n/a: <razão>`:
   - **Primeiros passos bloqueantes.** Gates antes do fan-out.
   - **Frentes independentes.** Arquivos, serviços ou camadas disjuntos paralelizam. Escritas compartilhadas serializam.
   - **Estado mutável compartilhado.** Por padrão, divida o alvo (**principle-separate-before-serializing-shared-state**). Serialize só por invariantes reais.
   - **Menor decomposição segura.** Se um único executor é melhor, diga por quê.
4. Implemente com escopo específico: caminhos, formato de dados nomeado e sua estrutura organizadora (**principle-model-the-domain**: máquina de estados em vez de booleanos espalhados, tabela em vez de ramos, modelo tipado em vez de suposições repetidas), escolhidos antes de escrever lógica, e critérios de sucesso. Delegue quando houver frentes independentes ou benefício de contexto. Quando a implementação admite vários formatos válidos, use **arena** para comparar. Edições cirúrgicas. Melhoria em primitivo compartilhado vai para todos os consumidores, cada um verificado. Commits frequentes.
5. Verifique na superfície correspondente via **dev-verify**. "Inconclusivo" ou superfície errada não é aprovação.
6. Rebase em commits pequenos e ordenados (**principle-sequence-verifiable-units**). Empilhe follow-ups.
7. Design contestado → `interrogate` antes de entregar.
8. PR só se pedido: **Opening a PR**.

Trabalho acoplado (uma feature, uma migração) vai para um único dono com o checkpoint inline. Fan-out no nível do pai é para fatias com artefatos independentes. Reescreva o checkpoint nas fronteiras de fase.

**Resposta:** o que construiu, o que escolheu e por quê, o checkpoint de throughput, decisões abertas. Tabelas para alternativas de design.
