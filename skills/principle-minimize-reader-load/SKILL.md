---
name: principle-minimize-reader-load
description: "Aplique ao revisar ou moldar código difícil de seguir. Conte as camadas entre pergunta e resposta e o estado oculto na cabeça do leitor; colapse wrappers de um chamador e encolha o escopo mutável."
disable-model-invocation: true
---

# Minimize Reader Load

Carga de leitura é o trabalho que um leitor faz para entender o código. Tem dois eixos independentes: camadas a percorrer entre a pergunta e a resposta, e estado oculto ou mutável a guardar na cabeça. Proteja os dois.

- Colapse camadas que só repassam: wrappers com um chamador, adapters sem segunda implementação, métodos de passagem. Faça inline.
- Encolha o escopo do estado: retorno em vez de mutação, local em vez de campo, campo em vez de estado de módulo, estado de módulo em vez de global. Derive em vez de sincronizar.
- Nomeie uma invariante uma vez, na fronteira, não em cada consumidor.

O teste: um leitor novo responde "de onde vem X?" e "o que pode mudar X?" em menos de 30 segundos? Se não, corte camadas ou corte estado.
