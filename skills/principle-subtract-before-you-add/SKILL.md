---
name: principle-subtract-before-you-add
description: "Aplique ao sequenciar uma adição, refactor ou reescrita. Remova código morto, validadores redundantes e referências vazias primeiro, depois construa sobre a base mais simples."
disable-model-invocation: true
---

# Subtract Before You Add

Ao evoluir um sistema, remova complexidade primeiro, depois construa. Subtração é o padrão.

Torne simplificação um investimento contínuo. Deixe o design um pouco mais simples e capaz, atrás da mesma superfície ou de uma menor, do que o encontrou.

- Remoção antes de construção.
- Corte antes de polir: chegue ao mínimo antes de investir em qualidade.
- Projete para o uso observado, não para casos de borda especulativos.
- Sem validadores, parsers ou guardas especulativos além do que a especificação exige.
- Simplifique prompts: remova instruções redundantes e templates excessivos.
- Referência sem conteúdo novo é deletada, não deixada como stub.
