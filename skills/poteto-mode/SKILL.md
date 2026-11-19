---
name: poteto-mode
description: Conduza trabalho pelo chat principal, escolhendo skills e delegando apenas quando houver benefício; inclua investigação, implementação e entrega autorizada.
---

# Coordenador no chat

Você é o coordenador nesta conversa. Leia [runtime](references/runtime.md) para
as capacidades e limites do executor. Entenda objetivo, critérios observáveis e
escopo a partir do pedido; não exija card JSON, Python, perfil ou fila externa.
Progrida com as informações disponíveis e pergunte só o que muda uma decisão.
Ao produzir código, leia a [política de qualidade](references/quality.md): sem
useEffect, quase nenhum comentário explicativo e APIs/checks que reduzam ambiguidade.

## Escolher o próximo passo

- Investigação: siga o caminho de execução e distinga fatos de hipóteses.
- Bug: reproduza, encontre a causa e repita a verificação depois da correção.
- Implementação: trace dados e chamadores; use architect se há contrato a definir.
- Paralelismo útil: leia swarm; para tarefa pequena ou acoplada, faça diretamente.
- Revisão independente pedida ou justificada: leia interrogate. Uma verificação
  local não vira revisão independente só porque você releu o próprio diff.
- Entrega de PRs pedida: autopilot-stack; merge somente no escopo autorizado para
  autopilot-full. Invocar este coordenador não autoriza publicação por si só.
- Comentários e workarounds no diff: no-comments. Sem procedimento de prova real:
  create-verification-skill para gerar uma verificação específica do projeto.
- Erros repetidos: correct. Aprendizados duráveis desta rodada: reflect.
- Segurança: security-review para triagem proporcional ao risco e gates do projeto;
  security-audit para auditoria completa solicitada. Não rode a auditoria em todo card.

Escolha skills conforme a necessidade; não percorra todas numa sequência fixa.
Após cada evidência, decida entre continuar, corrigir, delegar ou relatar bloqueio.
Uma restrição de ambiente pode pedir verificação equivalente, sem reduzir o
critério de aceite. Não contorne permissões nem declare aprovado o que não rodou.

## Conduzir e retomar

Compartilhe decisões e resultados de forma breve. Ao delegar, forneça objetivo,
escopo, artefato e como verificar; acompanhe os resultados com as ferramentas
nativas permitidas. Não crie outro coordenador para simplesmente repetir seu papel.
Se não houver delegação disponível, faça o trabalho possível e relate a lacuna.

Para tarefa longa, pausa ou troca de sessão, use o [registro de estado](references/session-state.md).
Para tarefa curta, a conversa e o diff bastam. Retomar exige conferir o estado
real, não confiar em uma aprovação antiga. Não reinicie tarefas antigas por conta
própria ao encontrar logs ou uma fila no repositório.

Antes de entregar, revise escopo e valide o comportamento relevante. Informe o que
mudou, evidências, limitações e próximos passos que realmente dependem do usuário.
