---
name: swarm
description: Distribui N executores em paralelo, coleta todos e devolve um relatório. Use para /swarm, "faz um swarm", ou cobertura paralela, corridas, baterias de verificação e exploração.
disable-model-invocation: true
---

# Swarm

Delegue só quando há benefício: paralelismo real, contexto novo ou avaliação independente. Mapeie ferramentas com o harness do **poteto-mode** (`../poteto-mode/references/harness.md`).

## Começo

Abra uma lista de tarefas com uma entrada por fase antes de lançar qualquer coisa: Enquadrar, Fan-out, Agregar, Relatório.

## Fase A: Enquadrar

1. Declare o predicado de pronto e o artefato ou relatório que o swarm devolve.
2. Escolha o formato: partição em fatias, corrida de N executores com briefs idênticos, ou misto. Em corrida ou misto, declare antes de lançar a regra: `primeiro que passar`, `ranquear todos` ou `melhor de`.
3. Executores herdam o modelo da sessão; braço que revisa ou verifica é avaliador ([harness](../poteto-mode/references/harness.md#modelos)). Corrida entre modelos ou providers só quando o usuário pede; nomeie o modelo de cada braço antes.
4. Escritores recebem saída própria: worktree isolada para código (**principle-separate-before-serializing-shared-state**). Revisores somente leitura podem inspecionar o checkout atual. Quando executores verificam ou medem commits, cada brief nomeia os SHAs exatos; brief de medição nomeia também o método (amostras, o que é uma amostra, ordem), e o executor registra os dois no resultado.
5. Padrão de até 3 executores em paralelo. Mais só com fatias realmente independentes e custo justificado.

## Fase B: Fan-out

Lance os executores de uma vez. A primeira linha de cada kickoff é `Leia <caminho-do-poteto-mode>/worker.md antes de tudo.`

Cada brief é autossuficiente: objetivo, escopo, fatia ou braço exato, como verificar e o que reportar. Relatórios usam `PASS`, `ISSUES` ou `BLOCKED` com evidência. Executor que prova um defeito reporta `ISSUES` com todos os problemas que consegue provar, não só o primeiro.

Executor que desiste: siga com N-1 e registre. Delegação não autoriza push, PR nem merge.

## Fase C: Agregar

Leia os resultados finais. Descarte resultado que não registra os SHAs e o método que o brief pediu e relance esse executor uma vez; na segunda falha, registre lacuna. Lacuna não conta como aprovação. Em cobertura, toda fatia exigida precisa de resultado. Em corrida, aplique a regra declarada. Verifique as alegações relevantes você mesmo. Não cole saídas brutas.

## Fase D: Relatório

Um relatório consolidado: tabela de resultados, uma linha por problema, lacunas ou desistências, e a regra da corrida quando usada.
