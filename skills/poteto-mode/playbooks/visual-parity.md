### Paridade visual

**Você é dono da equivalência pixel a pixel. O baseline é a especificação; não toque nele.** Equivalência se prova por diff de imagem, não a olho.

1. Estabeleça o baseline antes de qualquer migração: harness de regressão visual que captura o componente atual em seus estados, mais o alvo ao comparar duas implementações. Sem baseline, sem alegação de paridade. Pré-requisito bloqueante.
2. Cláusulas anti-atalho: não modifique o harness, não adultere o baseline, não reestruture o componente para passar o diff. Baseline parece errado: pare e pergunte.
3. Migre um componente por vez. Paralelize em worktrees, um dono por componente (**principle-separate-before-serializing-shared-state**). Primitivos compartilhados migram primeiro, como fase bloqueante.
4. Verifique cada componente contra o baseline por diff de imagem via **dev-verify**. Diff diferente de zero é falha; investigue o delta. Repita até zero.
5. PR só se pedido: **Opening a PR** por componente ou lote seguro.

**Resposta:** componentes migrados, resultado do diff de cada um, local do harness, o que falta.
