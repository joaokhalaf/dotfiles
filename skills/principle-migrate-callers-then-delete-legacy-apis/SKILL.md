---
name: principle-migrate-callers-then-delete-legacy-apis
description: "Aplique ao introduzir uma API interna nova enquanto chamadores antigos existem. Migre os chamadores e delete a API antiga na mesma onda, em vez de manter camadas de compatibilidade."
disable-model-invocation: true
---

# Migrate Callers Then Delete Legacy APIs

Ao introduzir uma API interna nova, migre todos os chamadores e delete a antiga na mesma onda. Sem shims, aliases ou caminhos paralelos.

- Atualize os testes para afirmar o contrato novo e delete testes que só protegem detalhes de implementação anteriores.
- Confira cada rename nos arquivos reais, inclusive strings, docs e referências.

**Quando se aplica:**
- Nenhum usuário externo depende de compatibilidade retroativa.
- O projeto absorve mudanças incompatíveis coordenadas.
- A API nova faz parte de uma simplificação ou refactor.
