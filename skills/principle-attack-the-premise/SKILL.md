---
name: principle-attack-the-premise
description: "Aplique quando duas ou mais correções com a mesma premissa falharam no mesmo gate. Escreva a premissa e teste-a antes de outra correção que a assuma."
disable-model-invocation: true
---

# Attack the Premise

Quando duas ou mais correções com a mesma premissa falharam no mesmo gate, suspeite da premissa, não das correções.

- Escreva a premissa: a frase que toda correção fracassada assumiu.
- Teste-a antes da próxima correção. Ache uma observação que daria resultado diferente se a premissa fosse falsa, e faça-a. Olhe como as falhas se distribuem, não só o tamanho delas.
- Se a evidência contradiz a premissa, procure o que as falhas têm em comum que ela não previu. Se uma parte sempre cai do lado perdedor, mude o que a coloca lá em vez de adicionar um mecanismo que limpa depois.

Não comece a próxima correção antes de escrever e testar a premissa.
