# Factory conduzida pelo chat

Para desenvolver esta factory, leia `skills/poteto-mode/SKILL.md` e siga o fluxo
adequado ao pedido. O chat principal coordena; o runner Python é opcional.
Faça tarefas pequenas diretamente. Delegue quando houver trabalho independente,
necessidade de contexto novo ou revisão útil, respeitando as regras do executor.
Não abra PR nem faça merge apenas por estar usando uma skill.

Se retomar a adaptação para chat, leia `runs/chat-first.md`. As execuções antigas
do esports em `.factory/` são artefatos preservados, não uma fila a reiniciar.
Instruções de coordenação e permissões da sessão/projeto continuam aplicáveis.

Ao produzir código, aplique `skills/poteto-mode/references/quality.md`. Ela define
sem useEffect, quase nenhum comentário explicativo e restrições codificadas em
APIs/tipos/checks. As skills no-comments e create-verification-skill detalham
limpeza e prova de comportamento. Não considere o enforcement instalado nos apps
apenas porque a política existe neste repositório.

Para triagem e revisão de segurança, leia `skills/security-review/SKILL.md`.
Mudanças sensíveis recebem revisão focada; auditoria completa usa security-audit
quando solicitada. Gates são definidos por projeto; instruções não fornecem sandbox.
