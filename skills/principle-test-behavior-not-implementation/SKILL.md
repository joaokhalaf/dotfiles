---
name: principle-test-behavior-not-implementation
description: "Aplique ao escrever, mudar ou manter um teste. Afirme o que os usuários do código observam, para o teste falhar quando esse comportamento quebra e continuar passando quando só os internos mudam."
disable-model-invocation: true
---

# Test Behavior, Not Implementation

Um teste é uma afirmação sobre o que os usuários do código observam pela interface: valores de retorno, erros, estado que podem ler de volta e efeitos em sistemas externos. Helpers privados, ordem interna de chamadas e dados intermediários são implementação.

Julgue cada teste contra duas edições imaginárias:

- **Quebre o comportamento** (valor errado, efeito pulado ou duplicado). Se o teste ainda passa, não prova nada. Causas usuais: asserção frouxa, valor esperado calculado pelo próprio código testado, asserção sobre dados que o teste mesmo construiu.
- **Mude os internos** mantendo todo resultado observável. Se o teste falha, está preso à implementação.

Mantenha o teste que pega a primeira edição e sobrevive à segunda. Reescreva ou delete o resto. Dirija o código pela interface pública com entrada concreta e derive o valor esperado do requisito. O que um serviço externo recebe é comportamento; chamada a helper interno não é. Combine "isto nunca acontece" com um caso em que acontece. Afirme o tipo de erro em que os chamadores ramificam, não a mensagem.
