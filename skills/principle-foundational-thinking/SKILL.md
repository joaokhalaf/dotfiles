---
name: principle-foundational-thinking
description: "Aplique antes de escrever lógica: escolher tipos e estruturas centrais, sequenciar andaime vs feature, perguntar o que atores concorrentes compartilham. Acerte as estruturas de dados e o código seguinte fica óbvio."
disable-model-invocation: true
---

# Foundational Thinking

Acerte o formato dos dados antes de escrever lógica. Defina os tipos centrais cedo, rastreie cada padrão de acesso e escolha estruturas que combinem com os caminhos dominantes. DRY na estrutura, não em cada linha.

Antes de compartilhar estado entre atores, pergunte o que acontece se outro ator o modificar ao mesmo tempo. Se a resposta não for "nada", isole.

Andaime primeiro. O que ajuda toda fase posterior (CI, testes, tipos compartilhados) vem antes, depois de remover código morto. Commits pequenos e de propósito único.
