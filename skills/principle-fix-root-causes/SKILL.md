---
name: principle-fix-root-causes
description: "Aplique ao depurar. Rastreie cada sintoma até o primeiro ponto em que o sistema errou e corrija lá. Uma guarda só é correção quando o estado que ela trata é legítimo."
disable-model-invocation: true
---

# Fix Root Causes

Corrija a falha, não o lugar onde ela apareceu. A causa raiz é o primeiro ponto em que o sistema fez algo que não devia, ou deixou de tratar um estado que devia.

- Reproduza primeiro. Pergunte "por quê" até a resposta ser uma decisão errada no código. Travado: instrumente e leia o estado real.
- Pergunte se o estado que disparou o sintoma é legítimo. Se é, trate-o onde o código quebrou. Se nunca deveria existir, uma checagem ali esconde o bug; ache o que o produziu. Guardas, retries, erros engolidos, valores limitados e estado descartado são os modos usuais de esconder um bug.
- Corrija o padrão, não a instância. Ache todo lugar com a mesma falha.
- Se o fato decisivo exigiu escavação funda, proponha o sinal barato e sempre ligado que o teria mostrado de primeira.
