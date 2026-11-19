---
name: principle-explain-the-number
description: "Aplique antes de medir, e antes de confiar, reportar ou agir sobre um número medido: speedup, regressão, throughput, latência ou resultado de eval. Ache o que o limita e descarte que ele mediu outra coisa."
disable-model-invocation: true
---

# Explain the Number

- **Escreva a decisão antes de rodar.** Nomeie o resultado que a mudaria e o piso de ruído. Pare quando a variação entre execuções for maior que o efeito.
- **Pergunte "por que não o dobro?"** Nomeie o recurso ou caminho de código que limita o resultado, a partir de um profile ou contadores coletados durante a execução. Palpite lendo código não é limitante.
- **Liste o que mais o número poderia estar medindo** (erros, trabalho pulado ou em cache, código que nunca rodou, um lado não ajustado, ruído, uma parte pequena demais para importar) e descarte cada item com evidência.
- **Mantenha contagem de execuções, variação e limitante junto do número.**

Para número de performance, rode **benchmark-checklist**. Para resultado de eval, pergunte se toda execução fez a tarefa, se a diferença se mantém entre tentativas e modelos, e se o cenário importa.
