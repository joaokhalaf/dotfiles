### Autopilot-stack

Execute [autopilot-full](autopilot-full.md), sem merge. Exige pedido explícito de entrega de PRs; pedir a tarefa não autoriza push.

1. **No lugar do passo 5, pare em verificado.** Pare quando cada PR estiver verificado e verde no head atual e entregue ao operador. Depois da entrega, ninguém faz push sem o ok do operador.
2. **Empilhe um PR só quando ele depende de outro.** Única exceção ao passo 3: a base é a branch do PR pai, conforme [opening-a-pr](opening-a-pr.md). Cada PR faz rebase na branch do pai; a raiz da stack, no trunk. Head novo no PR de baixo reempilha os de cima; PR cujo `git patch-id` não muda mantém o veredito.

**Resposta:** cada PR com seu veredito, no lugar do que integrou.
