---
name: interrogate
description: Faça revisão independente de código, design ou skills e retenha problemas demonstrados por evidência.
---

# Interrogate

Fixe intenção, escopo e conteúdo exato. Para código commitado registre base/head;
para mudanças não commitadas use diff/hashes; para skills use solicitações realistas
aplicadas às fontes atuais. Não exija commit ou PR para revisar um arquivo local.

Separe autor e revisor quando a independência for necessária. Um revisor separado
pode bastar; múltiplos modelos entram quando pedidos ou justificados e disponíveis.
Herde configurações da sessão, salvo escolha explícita. Duas sessões do mesmo
modelo não são revisão multi-modelo. Perfis do runner não governam agentes do chat.
Se delegação faltar, identifique a revisão própria e a lacuna de independência.

Brief: tente quebrar a mudança dentro da intenção; mostre arquivo/linha, caso,
comando ou procedimento, observado e esperado. Para instruções, execute um cenário
realista sem revelar ao revisor a resposta que você espera. Não corrija durante
pedido apenas de revisão. Não retenha preferências de estilo como defeitos.

O coordenador verifica evidências e deduplica por causa. Uma falha preexistente
não é uma regressão introduzida. Mudanças no conteúdo revisado exigem avaliar a
validade do resultado anterior. Ausência de achados não prova correção; reporte
cobertura real, restrições e o que não foi verificado.

Leia [runtime](../poteto-mode/references/runtime.md).

Para candidatos de segurança, aplique [security-review](../security-review/SKILL.md):
fronteira e impacto demonstrados, tentativa independente de refutação, execução
somente com os controles upstream e pendências sem aprovação fictícia.
