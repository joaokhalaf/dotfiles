### Hillclimb

**Você é dono da métrica e da integridade do experimento. Supervisione e revise.** Para melhoria iterativa e sustentada de uma coisa mensurável contra um alvo. Correção pontual é Bug fix ou Perf issue; isto é o loop.

Disciplina central: uma mudança, uma medição, manter ou reverter. Nunca empilhe mudanças não testadas e nunca declare ganho por inspeção de código (**principle-prove-it-works**).

1. Fundamente carga e arquitetura antes de escolher a métrica. Rastreie o alvo, nomeie as dimensões realistas que mexem no resultado (tamanho de dados, histórico, estado, concorrência) e escolha um caso que reproduza a queixa do usuário. Se nenhum reproduz, corrija a reprodução antes. Depois fixe uma métrica, a direção que conta como melhor e um predicado de parada que combine alvo com piso de tentativas (ex.: "≥50% melhor que o baseline e ≥10 iterações"). Use os números do usuário quando dados.
2. Construa o harness de medição, prove sua sensibilidade e congele-o (**principle-build-the-lever**). Rode cargas contrastantes e confirme que o caso alvo reproduz o sintoma e os casos fáceis se separam. Valide com **benchmark-checklist** antes de congelar; o harness imprime contagem de erros e de trabalho feito. Congelado, um comando repetível emite a métrica com amostras suficientes (mediana de N). Registre baseline e uma execução verde do gate de regressão antes de mudar algo.
3. Abra o log de decisões via **show-me-your-work**: `decision.tsv`, uma linha por tentativa (id, hipótese, mudança, antes, depois, delta, testes, veredito, nota). Leia antes de cada tentativa. Fora da árvore (gitignored).
4. Cada hipótese nomeia um mecanismo específico do modelo de arquitetura do passo 1. Para métrica de performance, ordene pelos mantras do [perf-issue](perf-issue.md) (só a ordem, não a regra de parada).
5. Loop, uma hipótese por iteração:
   - Implemente você ou delegue com escopo estreito; supervisione o diff (**principle-guard-the-context-window**). Hipóteses independentes vivas podem ir em paralelo, cada uma na sua worktree (**principle-separate-before-serializing-shared-state**).
   - Meça antes e depois com o harness congelado e rode o gate de regressão.
   - Aceite só quando a métrica passar do ruído e o gate ficar verde. Senão reverta inteiro.
   - Um commit por correção aceita, com `git add <arquivos>`, nunca `-A`. Registre a linha, mantida ou revertida.
6. Passe do primeiro platô. Em estagnação, mude de categoria, combine quase-acertos, releia o código, tente algo radical. Correção e simplicidade vencem o número: reverta ganho que quebra comportamento; mantenha simplificação que segura o número.
7. Pare quando o predicado for atingido ou as ideias restantes forem marginais. Não relaxe o predicado; não desista com hipóteses baratas não tentadas. Travado: diga.
8. PR só se pedido: **Opening a PR** com os commits aceitos na ordem em que entraram.

**Resposta:** métrica e alvo, baseline → final com delta percentual, iterações (mantidas vs revertidas), cada correção aceita numa linha, caminho do `decision.tsv`, a melhor próxima ideia.
