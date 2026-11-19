### Problema de performance

**Você é dono da história da medição. Planeje, revise, verifique os números.** Cada correção amarrada a uma medição; não leia código no lugar de medir.

1. Capture um trace de baseline na superfície correspondente via **dev-verify**. Valide o baseline, e cada número posterior, com **benchmark-checklist**.
2. Rastreie o código para fundamentar hipóteses. Não declare teto de performance sem executar. Tente os mantras em ordem, do mais barato:
   1. Não faça. Pare trabalho cujo resultado ninguém usa em vez de barateá-lo.
   2. Faça, mas não de novo.
   3. Faça menos.
   4. Faça depois.
   5. Faça quando ninguém estiver olhando.
   6. Faça concorrentemente.
   7. Faça mais barato.

   Quando um mantra anterior atinge o alvo, pare.
3. Planeje a correção pelo trace. Atravessa fronteira de função → `architect` antes. Delegue a implementação quando houver benefício. Revise o diff. Capture um trace pós-correção. Aplique **principle-sequence-verifiable-units**: verifique cada tentativa antes da próxima.
4. Analise e compare os artefatos (JSON para sqlite, diff). "Inconclusivo" ou superfície errada não é aprovação.
5. Cite a medição no PR.
6. PR só se pedido: **Opening a PR**.

Para melhoria contínua contra uma métrica, use [hillclimb](hillclimb.md).

**Resposta:** número de baseline, número pós-correção, delta, caminho do artefato.
