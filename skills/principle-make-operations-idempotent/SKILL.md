---
name: principle-make-operations-idempotent
description: "Aplique ao projetar comandos, etapas de ciclo de vida ou loops de processamento sujeitos a crashes, reinícios e retries. Convirja ao mesmo estado final independente de execuções parciais anteriores."
disable-model-invocation: true
---

# Make Operations Idempotent

Projete toda operação que muda estado para convergir ao estado correto não importa quantas vezes rode nem onde a execução anterior parou.

Derive cada passo do estado que existe, não do que a execução anterior pretendia. Leia o estado atual, compare com o objetivo e aplique só a diferença.

Tudo que uma execução deixa para trás (lock, arquivo temporário, registro meio escrito, job reivindicado) precisa ser reconhecível como velho pela próxima execução, por evidência que valha onde quer que a anterior tenha parado. Escreva num caminho temporário e renomeie para o lugar.

O teste: o que acontece se rodar duas vezes? E se a execução anterior caiu em cada ponto possível? Se a resposta depende do que ficou para trás, adicione um passo de reconciliação.
