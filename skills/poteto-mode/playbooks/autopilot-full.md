### Autopilot-full

**Você é dono dos vereditos, nunca dos PRs. Um dono leva cada PR do build ao merge, e nada integra até um verificador que não escreveu o código provar o código que entra.**

Exige instrução explícita autorizando merge e nomeando os itens. Pedir o plano não é autorização. Itens fora da fila param em merge-ready.

1. **Gates do operador primeiro**, inclusive os de **security-gate** no head atual. Nunca use admin, bypass ou enfraqueça gates.
2. **Um dono por PR**, subagente em worktree isolada, que constrói, abre o PR por [opening-a-pr](opening-a-pr.md), prova a mudança no artefato real, faz babysit até verde por [babysit](babysit.md) e integra quando os passos 4 e 5 liberam. Onde o babysit manda reportar rebase, o dono faz rebase da própria branch e publica com `git push --force-with-lease`.
   Abra o PR cedo para CI e bots rodarem junto. O código está pronto só depois de **no-comments** e **unslop**. Então rebase no trunk atual e reporte o head pronto antes da autoprova. Rode os checks do repo nos caminhos tocados antes de cada push que precise de verificador.
   Registre ids de subagentes, estado e trilha por **show-me-your-work**, para outro dono retomar. Force-push só na própria branch, com `--force-with-lease` no SHA que você publicou por último; push que você não fez → pare e reporte.
3. **Donos em paralelo a partir do trunk, sem empilhar**, para cada PR integrar sozinho.
4. **Verificação por swarm uma vez**, no head pronto, via **swarm**: verificadores independentes reexecutam gates, provam o comportamento crítico na superfície real via **dev-verify** e auditam o diff. Swarm completo de novo só para comportamento novo, redesenho ou diff grande; rebase, conflito ou correção pequena ganham um verificador; mudança só de texto, nenhum.
   Bloqueie só por problema demonstrável: execução falhando no head, ou doc que o PR deixou errada. Problema que a base já tem não bloqueia, salvo se o PR o copia ou passa a alcançá-lo.
5. **O dono integra só o que você verificou, testado no trunk onde vai entrar.** CI verde sozinho nunca autoriza merge. Antes do merge, busque o trunk e avalie se as mudanças afetam o patch: conflito, arquivo tocado pelos dois lados ou mudança nos checks → rebase e espere CI; trunk mudou chamador ou dependência → rode os checks do patch no resultado. Senão, integre. Um terceiro rebase após o preparo → segure e reporte.
6. **Camada raiz.** Qualquer afrouxamento de gate (orçamento, allowlist) exige prova de um verificador e sua contra-assinatura. Check desabilitado ou soft-fail sempre sai. Nunca dê nem contorne aprovação exigida pelo forge.
7. **Pare imediatamente no stop do operador.** Todo dono recebe ordem de zero escritas, reporta onde está e mantém o brief até ser liberado.

**Resposta:** estado e veredito de cada PR, o que integrou, contra-assinaturas e por quê, gates pendentes do operador, follow-ups estacionados, com links.
