### Execução autônoma

**Você é dono da condição de saída. Defina pronto, depois conduza até lá sem parar.**

1. Declare a condição de saída como predicado verificável antes da primeira iteração (testes verdes, repro corrigida, N PRs abertos e verdes, diff de pixel zero).
2. Escolha o mecanismo de despertar (ver [harness](../references/harness.md)). Evento a observar (CI, merge, ref avançando) → observador que acorda no evento, com heartbeat longo de reserva. Sem evento → heartbeat fixo dimensionado para quando vale reconferir. Sem loop no executor: continue no turno.
3. Cada iteração faz a menor mudança que a evidência justifica, verifica contra o predicado, faz commit se avançou e descarta o que não ajudou. Sequencie por **principle-sequence-verifiable-units**.
4. Descobertas no caminho que servem ao objetivo são suas: skills quebradas, bugs relacionados, verificadores instáveis, ferramentas falhando. Correções fora da banda em commit ou PR próprio. Não estacione trabalho reversível para o humano. Traga só ações irreversíveis, decisões de produto que nenhum experimento resolve, ou um beco sem saída real. Volte ao predicado após cada desvio.
5. Checkpoint a cada iteração via **show-me-your-work**: uma linha com o que mudou e se o predicado andou.
6. Pare quando o predicado for atingido. Platô não é parada: mude de abordagem. Beco sem saída real: diga, não gire. Nunca relaxe o predicado.

Os limites de Autonomia continuam: push e PR só se o pedido incluir; merge nunca, salvo [autopilot-full](autopilot-full.md).

**Resposta:** condição de saída, iterações, o que entrou, o que foi descartado, estado final do predicado.
