---
name: no-comments
description: Remova comentários explicativos e workarounds do diff e converta restrições em APIs, tipos ou checks, preservando obrigações externas.
---

# No comments

Leia a [política de qualidade](../poteto-mode/references/quality.md). Use os arquivos
pedidos; sem escopo explícito, examine somente o diff atual, incluindo arquivos
novos. Não faça uma limpeza de todo o repositório por estar usando esta skill.

1. Leia cada comentário com o código e seus chamadores. Remova narrativa, código
   comentado morto e justificativas para workarounds evitáveis. Se nomes, tipos ou
   estrutura precisarem explicar o comportamento, corrija o código dentro do escopo.
2. Para “não remova”, “sempre faça X” ou “esta ordem importa”, busque a razão e
   transforme a restrição em API, tipo, teste ou gate executável. Não apague a única
   informação sobre uma restrição real antes de preservá-la no mecanismo correto.
3. Preserve cabeçalhos de licença, avisos obrigatórios, exemplos de documentação
   pública necessários e diretivas exigidas pelas ferramentas. Em restrição externa
   que não controlamos, retenha só a explicação curta com evidência e origem.
4. Inspecione suppressions de lint/tipos. Remova causas e supressões quando viável;
   não adicione ou amplie suppressions para conseguir verde. Se uma solução exige
   ampliar escopo, reporte o problema e o trabalho necessário, sem expandir sozinho.
5. Rode os checks relevantes e examine o diff para confirmar comportamento preservado.
   Para mudanças só em texto não invente testes de runtime; para mudanças em código
   comprove o contrato observável. Informe remoções, preservações com razão,
   mecanismos criados e restrições ainda não impostas.

Um revisor independente pode ajudar em uma limpeza extensa; não é obrigatório
criar Comment Sicko ou usar APIs de agentes do Cursor. Use as ferramentas permitidas
pela sessão e identifique revisão própria quando não houver independência.

Leia [runtime](../poteto-mode/references/runtime.md) para execução e coordenação.
