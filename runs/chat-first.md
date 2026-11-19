# Rodada 1 — factory conduzida pelo chat

## Objetivo e escopo

Adaptar a própria factory para main no chat e subagentes opcionais. Critérios:
iniciar só com pedido em linguagem natural; não exigir Python/JSON/Herdr; escolher
delegação por benefício; manter evidência e retomada; preservar runner e tarefas antigas.
Escopo: instruções, skills, documentação e este registro. Sem push/PR/merge.

## Estado

- Adaptação das instruções: concluída para o fluxo pelo chat.
- Validação estrutural: plugin/skills passaram; quick_validate passou nas quatro
  skills alteradas; todas as referências locais resolvem.
- Cenário independente de retomada: avaliado por chat_flow_trial em contexto novo,
  mesmo modelo herdado; nenhuma contradição operacional encontrada.
- Rodada esports: suspensa a pedido do usuário. Não modificar nem reiniciar.
  Estado observado no SQLite: ids 1/2 blocked, attempts=2. Suspensa é a intenção
  do operador, não uma alteração desse estado técnico. Artefatos preservados em
  .factory/ed0ac7f5ab03; testes
  criados nas worktrees 1/2, bloqueio relatado no IPC do tsx dentro do sandbox.

## Decisões e observações

Main implementa esta mudança acoplada diretamente; um revisor separado vai exercitar
as instruções em cenário de retomada. Nenhuma delegação de implementação é necessária.
Os perfis e limites do runner não controlam ferramentas/modelos do chat.
Herdr é usado nesta sessão pelas instruções existentes, sem se tornar requisito
de uso para outras sessões. Não alterar permissões para fazer um cenário passar.

## Evidências desta rodada

O main leu poteto-mode/runtime, implementou diretamente uma mudança de instruções
acoplada e usou um único revisor separado para avaliar as instruções. Não iniciou
runner, autores por CLI, PRs ou merges. As validações foram estruturais e de referências;
não foi adicionada uma suíte que apenas compara o texto das regras.

O revisor exercitou dois pedidos: retomar uma correção pequena de documentação sem
runner/Herdr e solicitar revisão independente de skill não commitada usando somente
o modelo atual. Resultado: trabalho direto e leitura do registro para o primeiro;
contexto separado, sem exigir modelo diferente ou commit, para o segundo. Também
identificou que diff Git isolado omite arquivos não rastreados; conferiu os hashes.

Cobertura: leitura e decisão sobre cenários, não execução de uma correção por outro
agente nem sessão realmente sem Herdr. Nesta conversa Herdr era exigido e foi usado.
Não há prova de funcionamento no Claude Desktop; depende das ferramentas da sessão.

Conteúdo revisado: poteto-mode SHA256
1414a66605b9ce0ddf3287ba9bde2b4ddcbb0ffa0269493ec78e8383a1eab68b;
runtime SHA256 00e7a363096b58eacdfc04b6598fb0367d9c38cab84104359c392eaf94383c82;
interrogate SHA256 7bb8263237cda9ce2b23ccd56d6ca213de3fe8fdbbf670c4ea84ddda40a0155b.
Runner preservado, SHA256
0d7a0e8f94d76625671280f818c1486a2525b86ced06be1fc14b0a037127f558.

## Aprendizado aplicado (reflect)

A interface desejada deve orientar a arquitetura: runner/perfis são opcionais,
e não pré-requisitos das skills. Esta é uma decisão de produto/julgamento,
registrada no ponto de entrada e no contrato, sem tentar impor via lint textual.
Delegação serviu para avaliação independente, sem fragmentar uma edição acoplada.

## Próximo passo

Usar o coordenador nesta conversa para uma melhoria concreta escolhida pelo usuário;
manter verificações proporcionais e registrar apenas novos aprendizados demonstrados.
A rodada esports continua suspensa até pedido explícito de retomada.
