---
name: principle-type-system-discipline
description: "Aplique ao projetar tipos, revisar uma assinatura ou escrever código em linguagem estaticamente tipada. Estados ilegais irrepresentáveis, primitivos semânticos com marca, parse de dados externos na fronteira, variantes exauridas, tipos derivados de schemas autoritativos."
disable-model-invocation: true
---

# Type System Discipline

Faça o compilador rejeitar estados impossíveis, primitivos trocados e variantes não tratadas.

- **Estados ilegais irrepresentáveis.** Uniões discriminadas em vez de campos opcionais que precisam combinar.
- **Primitivos semânticos com marca.** Se dois argumentos compartilham um tipo primitivo mas significam coisas diferentes, dê a cada um seu tipo. Valide uma vez na criação.
- **Dado externo não tem tipo até ser parseado.** JSON, payloads RPC, args de CLI, config, variáveis de ambiente e linhas de banco passam por uma função de parse na fronteira que devolve o modelo tipado.
- **Exaura variantes.** Switch sobre união termina num caso que falha na compilação se uma variante nova aparecer.
- **Derive tipos de schemas autoritativos.** Quando um arquivo de schema é dono de um formato, derive o tipo dele em vez de escrever um paralelo à mão.
