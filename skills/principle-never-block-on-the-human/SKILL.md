---
name: principle-never-block-on-the-human
description: "Aplique na tentação de perguntar \"posso fazer X?\" sobre trabalho reversível."
disable-model-invocation: true
---

# Never Block on the Human

O humano supervisiona de forma assíncrona. Agentes precisam ficar desbloqueados. Tome decisões razoáveis, prossiga e deixe o humano corrigir depois. Como mudanças de código são reversíveis e revisáveis, uma decisão errada costuma custar menos que bloquear.

- Faça, depois apresente. Não pergunte "posso fazer X?". Faça X e explique por quê.
- Torne o sistema autocorretivo. Notou um problema: registre e corrija na próxima rodada.
- Ações reversíveis (escrever código, editar notas, dividir tarefas, commits locais) prosseguem sem bloquear.
- Push, PR e respostas em threads de review exigem pedido explícito do usuário. Merge, deploy, force-push, apagar dados e mensagens externas exigem confirmação.
- A direção de produto vem do humano. A execução não bloqueia.
