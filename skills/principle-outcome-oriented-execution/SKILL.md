---
name: principle-outcome-oriented-execution
description: "Aplique em reescritas e migrações planejadas com fronteiras de fase explícitas. Convirja na arquitetura alvo; não preserve estados intermediários suaves com código de compatibilidade descartável."
disable-model-invocation: true
---

# Outcome-Oriented Execution

Otimize para o estado final pretendido e verificável, não para estados intermediários suaves.

**Por quê:** manter cada passo intermediário totalmente estável costuma criar código de compatibilidade temporário que vira dívida longa. Convirja na arquitetura alvo e prove a correção em fronteiras de verificação explícitas.

**Regra central:**
- Integridade do estado final acima de estabilidade transitória.
- Quebra intermediária é aceitável quando planejada, delimitada e reversível.

**Limites:**
- Use em reescritas e migrações planejadas com fronteiras de fase explícitas.
- Declare onde a quebra temporária é aceitável.
- Mantenha checks de alto sinal nas áreas tocadas durante a migração.
- Exija verificação estática e de runtime completa ao fim do plano.
