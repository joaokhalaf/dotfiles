---
name: principle-model-the-domain
description: "Aplique ao escrever lógica com estado, ou quando o código ramifica muito ou repete uma suposição de formato em vários arquivos."
disable-model-invocation: true
---

# Model the Domain

Codifique o domínio numa estrutura de dados em vez de espalhá-lo em condicionais. A estrutura certa torna estados inválidos irrepresentáveis e apaga ramos.

Use máquina de estados em vez de booleanos ou checagens de fase espalhados, modelo tipado em vez de parâmetros soltos, mapa, registro ou união discriminada em vez de ramos espalhados por arquivos, reducer em vez de mutações ad hoc, e índice, fila ou coleção normalizada onde o padrão de acesso pede.

Não force. Mantenha código simples quando o formato é claro, local e improvável de crescer, e desconfie de abstração que adiciona indireção sem remover ramos ou estados inválidos.

Sinal de que você pulou isto: uma feature que cresce um if/else em mais um ramo, ou um segundo booleano que precisa ficar em sincronia com o primeiro.
