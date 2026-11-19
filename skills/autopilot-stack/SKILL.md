---
name: autopilot-stack
description: Conduza tarefas até PRs verificados para revisão humana, sem merge, pelo coordenador no chat.
---

# Autopilot stack

Use quando o pedido incluir entrega de PRs. Aplique somente aos itens autorizados;
esta skill não transforma uma tarefa local em autorização de push/PR. Não faça
merge. Confira repo, base, credenciais, checks e critérios necessários à entrega.

Mantenha os itens no plano do chat ou em Markdown para retomada; JSON e runner
não são requisitos. Identifique dependências. O main pode implementar um item;
use swarm só quando delegar trouxer benefício. Isole escritores paralelos em
worktrees e use architect quando houver contratos relevantes.

Antes de publicar, execute checks relevantes e prova comportamental. Faça revisão
proporcional, recorrendo a interrogate quando precisar de independência. Registre
o conteúdo verificado, faça commits no escopo autorizado e abra PR com evidências.
Confirme head remoto e CI: ausente/pendente não é verde. Use o mecanismo do executor
para acompanhar checks; não invente espera ou aprovação.

Pare nos PRs verificados para revisão humana. Não continue empurrando mudanças
após a entrega sem instrução. PRs independentes partem da base apropriada; empilhe
somente dependências reais e revalide filhos após restack. Preserve registros e
worktrees não entregues. Se o usuário escolheu runner, seus limites/configuração
valem nessa execução; não os imponha a toda conversa.

Leia [runtime](../poteto-mode/references/runtime.md).

Aplique [security-review](../security-review/SKILL.md) conforme o risco. Inclua no
PR o escopo revisado, SHA, resultados dos gates do projeto e lacunas. PR aberto
com bloqueio explícito não equivale a entrega verificada.
