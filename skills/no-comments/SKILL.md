---
name: no-comments
description: Lança o Comment Sicko no diff, corrige os achados aceitos e oferece codificar restrições alegadas em comentários. Use para /no-comments ou com a mudança pronta, antes da revisão do avaliador.
disable-model-invocation: true
---

# No comments

Lance o Comment Sicko e aja sobre os achados aceitos. Confie na perspectiva nova dele. Leia a [política de qualidade](../poteto-mode/references/quality.md).

## Escopo

Os arquivos ou o diff do chamador. Senão, o diff atual contra a branch base (padrão `main`), incluindo a árvore de trabalho e arquivos novos. Não faça limpeza do repositório inteiro.

## Passos

1. Lance um subagente com escrita no checkout (ou worktree com as mudanças copiadas) cujo kickoff é `Leia <caminho>/references/comment-sicko.md e assuma esse papel.` mais o escopo. Não repita as regras dele. Sem delegação disponível, aplique você mesmo as regras e diga que não houve perspectiva nova.
2. Inspecione o relatório e o diff dele. Rejeite edições de código de aplicação, fugas de escopo, remoções protegidas por exceção, razões de `MUST KILL` mal declaradas, e flags que tratam código intencional mantido como culpado. Flags de reshape sobre surpresas do nosso código continuam acionáveis; não restaure esses comentários. Um "manter" sobrevive só com prova de que trata de algo que não podemos mudar. Audite supressões de lint e TypeScript no escopo que ele perdeu; supressões de correção ou segurança continuam `MUST KILL`. Restaure remoções só com a exceção exata e prova no escopo. Antes de aceitar kills ou keeps finos de `IMPORTANT` ou "não remova", rastreie o símbolo ou rode **why** nele. Kill ambíguo: não restaure. Keep refutado ou ainda ambíguo: apague. Reverta e relance uma vez um relatório rejeitado, nomeando a falha. Segunda rejeição: reporte em aberto e falhe o `/no-comments`.
3. Corrija direto os flags triviais aceitos: apague o caminho morto, remova o parâmetro, use a API real. Se alguma correção precisa de formato, rode **architect** uma vez para o conjunto aceito e o código ao redor. Pare no esboço; o passo 4 implementa.
4. Implemente a menor correção de causa raiz dentro do escopo. Remova todo workaround nomeado. Causa raiz fora do escopo: entregue a menor correção no escopo e reporte o resto em aberto. **principle-fix-root-causes** e **principle-redesign-from-first-principles** orientam a intenção; nenhum autoriza ampliar o escopo. Nunca acrescente guardas de sintoma.
5. Comentários de restrição dizem "não remova", "não mude o texto" ou "fale com X antes de mudar". Mantenha os que tratam de algo que não podemos mudar. Ofereça o tipo, check de runtime, teste ou lint mais barato no escopo e espere aprovação (em execução sem supervisão, só com pré-aprovação do chamador). Aprovado: codifique, depois apague. Senão: apague, reporte a restrição em aberto e esboce o trabalho fora do escopo.
6. Rode os checks relevantes e confira o diff: comportamento preservado.
7. Reporte: quantidade de remoções, comentários restaurados, relançamentos, esboço do architect, correções, ofertas de codificação, codificações feitas, restrições não impostas e outro trabalho aberto.
