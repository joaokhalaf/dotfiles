### Shipping

**Você é dono do que entra. Verifique cada PR de forma independente, integre só a sequência verificada a partir da raiz, depois tire as mãos da stack.**

Requer autorização explícita de merge nomeando os PRs. Aplique os gates de **security-gate** no head atual.

1. **Verifique cada PR de forma independente antes de integrar.** Um verificador por PR, avaliador (ver [harness](../references/harness.md#modelos)) em worktree própria, executa a mudança como um usuário via **dev-verify**, pai contra head, e registra `PASS`, `PASS+NOTES` ou `FAIL` no PR. Só conta veredito de quem não escreveu o código. CI verde e bot aprovando não são veredito.
2. **Integre só a sequência verificada contígua a partir da base.** Suba do PR não integrado mais baixo e pare no primeiro sem `PASS`/`PASS+NOTES`. Os de baixo são a sequência; o de cima é o teto. PR verificado acima de um não verificado espera. Um PR que não contém nem precisa daquele código pode ir para o trunk sozinho, com veredito novo.
3. **Confira que os vereditos ainda descrevem o código.** Compare `git patch-id` no SHA do veredito com o head atual. Se os patches diferem só em testes, docs ou lint, o resultado de uma lane vale quando o que ela rodou compila igual nos dois SHAs, salvo ruído (diferença que também aparece entre dois builds do mesmo SHA). A mudança em si ainda ganha checks e revisão novos. Lane sem saída de build (ex.: dev server) é reexecutada.
4. **Integre de baixo para cima, um PR por vez**, com `gh pr merge <pr> --squash`. Leia o PR de volta (`gh pr view <pr> --json state,mergedAt,baseRefName`): fila de merge e auto-merge não são merge. Integrado = merged com trunk como base. Arme `--auto` só em PR cujo veredito cobre o head atual. Depois de integrar, retarget o PR filho para o trunk, mova o patch para o resultado e faça push com `--force-with-lease`; o passo 3 decide se o veredito sobrevive.
5. **Deixe a stack em paz enquanto integra.** O movimento do passo 4 é a única mudança em branch ou base. Acompanhe até o teto ler merged. Merge travado: descubra por quê antes de mudar algo.
6. **Pare no teto.** Estender exige vereditos novos.

**Resposta:** a sequência verificada e seu teto, veredito de cada PR e quem produziu, o que entrou e como confirmou, o que a próxima lacuna precisa.
