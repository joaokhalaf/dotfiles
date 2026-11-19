---
name: benchmark-checklist
description: Valida uma medição de performance (limitante, tuning, limites físicos, erros, repetibilidade, relevância e se o trabalho rodou) antes de reportar ou agir. Use ao rodar um benchmark ou reportar um speedup, regressão, latência ou throughput medido.
---

# Checklist de benchmark

Use ao produzir um número de performance: antes e depois de um PR, alegação de regressão, harness de hillclimb, escolha de biblioteca ou configuração. Responda cada pergunta com evidência de uma execução, não com palpite sobre o código.

Para uma estimativa rápida que o usuário pediu, uma execução basta. Ainda confira as perguntas 4 e 7 e diga que foi uma execução. Pule o resto, salvo se a execução parecer errada. Escolha entre opções nunca é estimativa rápida.

## Antes de rodar

- Escreva a alegação que espera fazer, nas palavras que entregaria ("export 30% mais rápido no p50 com o dataset de 60 mil linhas"). As perguntas testam essa frase.
- Leia o script de medição. Anote o que ele cronometra, conta e ignora.
- Confira carga com `uptime` e núcleos com `nproc`. Máquina ocupada: descubra o que está rodando. Se não puder parar, intercale os lados para os dois verem o mesmo ruído e diga isso no relatório. No WSL, processos do Windows também disputam a CPU.

## As perguntas

1. **Por que não o dobro?** Nomeie o limitante. Faça profile numa execução que você não reporta, porque profilers deixam o trabalho mais lento. Use CPU por processo (`top`, `pidstat`), profiler de runtime (`node --cpu-prof`, `py-spy`, `perf`), espera de I/O e contagem de syscalls (`strace -c`), e mapeie o ponto quente ao código. Observe o gerador de carga: se ele satura primeiro, você mediu o gerador. Se uma mudança não moveu o número, o limitante explica por quê; ache-o antes de chamar a mudança de inútil.
2. **Foi ajustado?** Rode cada lado como produção roda: builds de release, flags e env de produção, batching e transações, pools de conexão, caches tão quentes ou frios quanto em produção, mesmas versões e dados. Se um lado roda com defaults, você comparou configurações, não implementações. Limitante que é configuração (commit por linha, build de debug, índice faltando) significa lado não ajustado: ajuste e meça de novo antes de escolher vencedor. Sem poder ajustar, não escolha vencedor daquela execução.
3. **Quebrou limites?** Faça a conta. Bytes por segundo contra banda de disco e rede; operações por segundo vezes custo por operação contra os núcleos; tempo economizado contra o tempo da parte alterada. Remover uma parte que leva 10% da execução deixa a execução no máximo ~11% mais rápida. Resultado além do limite mediu outra coisa: cache, no-op ou bug.
4. **Deu erro?** Conte falhas e respostas não sucesso, e confira que as saídas estão corretas, não só presentes. Rejeições costumam ser rápidas; timeouts e retries, lentos. Se o script não conta erros, adicione a contagem.
5. **Reproduz?** Rode cada lado pelo menos 5 vezes, alternando (A, B, A, B…) para aquecimento, inicialização preguiçosa, caches e deriva não favorecerem nenhum. Reporte mediana e faixa. Diferença menor que a variação entre execuções é diferença não mensurável. Em casos apertados, use teste de soma de postos ou a estatística do próprio harness.
6. **Importa?** Ao lado de qualquer resultado micro, meça o caminho ponta a ponta que o usuário espera, com tamanhos de dados e concorrência realistas, e reporte o micro como fração do todo. Um helper que leva 1% de uma requisição deixa a requisição no máximo 1% mais rápida.
7. **Aconteceu mesmo?** Confirme que o trabalho rodou dentro da região cronometrada: a requisição chegou ao servidor, as linhas foram escritas, os bytes lidos, o código usou o resultado. Código preguiçoso (geradores não iterados, promises não aguardadas, resultados que o JIT descarta) e timeouts produzem números para trabalho que não aconteceu.

## Relatório

- Comece pelo veredito: mais rápido, mais lento, sem diferença mensurável ou inconclusivo.
- Dê o número com unidade, número de execuções, faixa e limitante. Ex.: "p50 41 ms → 33 ms, mediana de 7 execuções por lado, faixa 32 a 35 ms depois, limitado por parse de JSON em um núcleo."
- Veredito inconclusivo quando você alega diferença mas não nomeia o limitante, quando um lado rodou sem ajuste, ou quando não conferiu as perguntas 4 e 7. Nomeie a lacuna.
- Corpo de PR com um número principal. Execuções, faixa e evidência do limitante vão em artefato ligado.

## Outros usos

- Valide o baseline do playbook perf-issue do **poteto-mode** antes de planejar a partir dele, e cada número depois.
- Valide o harness do playbook hillclimb antes de congelá-lo. O harness congelado imprime contagem de erros e de trabalho, então cada manter-ou-reverter confere as perguntas 4 e 7 de graça.
