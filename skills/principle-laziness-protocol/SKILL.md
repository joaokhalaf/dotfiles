---
name: principle-laziness-protocol
description: "Aplique ao refatorar, avaliar tamanho de diff, ou na tentação de adicionar abstrações, camadas ou sinais atravessando o código. Viés para deletar e para a menor mudança que resolve."
disable-model-invocation: true
---

# Laziness Protocol

Viés para deletar. A melhor mudança é a menor que resolve o problema.

- **Consolide decisões.** Não repita a mesma escolha em vários lugares. Ponha atrás de uma fonte de verdade e passe o resultado como uma flag simples.
- **Minimize o diff.** Menos linhas vencem boilerplate "elegante".
- **Sem camadas especulativas.** Abstração, parâmetro ou sinal atravessando módulos só quando um uso real o exige agora.
