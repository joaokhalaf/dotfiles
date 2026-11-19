---
name: swarm
description: Delegue fatias independentes ou avaliações separadas e consolide evidências, usando as ferramentas de agentes da sessão.
---

# Swarm

Identifique o benefício antes de delegar: paralelismo, contexto novo ou avaliação
independente. Uma tarefa pequena pode ficar com o main; não invente agentes para
cumprir uma estrutura. Respeite autorização e capacidades de delegação do executor.

Defina objetivo, critérios, dependências, escopo e resultado por agente. Para
escritores paralelos use worktrees isoladas pelo mecanismo disponível e ownership
claro; não permita edições concorrentes do mesmo arquivo no mesmo checkout.
Revisores somente leitura podem inspecionar o checkout atual. Não crie worktree
quando o executor exigir que a ferramenta de delegação cuide disso.

Use o mecanismo nativo permitido. Não passe a mesma execução a dois controladores.
Comece com até dois agentes em paralelo; reduza quando acoplamento ou consumo
não justificar. Acompanhe pelo mecanismo de espera/notificação real, registre ids
e artefatos ao precisar retomar, e preserve resultados se houver falha.

Consolide achados e evidências, verifique alegações relevantes e indique lacunas.
Se o modelo/provider escolhido não estiver disponível, relate; não substitua sem
instrução. Delegação não autoriza push, publicação ou merge.

Leia [runtime](../poteto-mode/references/runtime.md) para coordenação e permissões.
