### Refactoring

**Você é dono do contrato. A estrutura muda; o comportamento não.** Diferente de Feature, que adiciona comportamento, e de Bug fix, que o corrige.

Se a limpeza revelar feature faltando ou bug real, separe e entregue primeiro a mudança estrutural contra o contrato fixado. Redesenho é permitido, mas nomeie e rote para Feature. Trabalho estrutural grande ou transversal vai para **figure-it-out**.

1. Fixe o contrato de comportamento primeiro. Rastreie o subsistema e escreva teste de caracterização, snapshot ou harness de equivalência antes de mover estrutura. Sem cobertura, escreva o pino antes. Tipos e lint não são pino.
2. Nomeie a estrutura que falta (**principle-model-the-domain**). Código simples fica quando o formato já é claro e local. O reshape deve apagar ramos ou estados inválidos, não adicionar indireção.
3. Nomeie o formato alvo: layout de módulos, tipos e grafo de chamadas como se construído hoje (**principle-foundational-thinking**, **principle-redesign-from-first-principles**). Atravessa fronteira de função → **architect**.
4. Subtraia antes de adicionar: código morto, wrappers de um chamador, validadores redundantes, referências órfãs (**principle-subtract-before-you-add**). Entra a menor mudança que atinge o alvo (**principle-laziness-protocol**). Limpeza especulativa é revertida.
5. Mova em passos pequenos que preservam comportamento, mantendo o pino verde. Em reshape de API, migre todos os chamadores e delete a API antiga na mesma onda (**principle-migrate-callers-then-delete-legacy-apis**). Sem shims nem caminhos paralelos. Confira cada rename nos arquivos reais: renames erram usos em strings, prosa e referências. Edições mecânicas podem ser delegadas com escopo específico.
6. Prove comportamento inalterado no artefato real (**principle-prove-it-works**). Em reshapes maiores, rode checagem de equivalência: script que compara saídas antigas e novas, baseline gravado reexecutado ou smoke na superfície via **dev-verify**.
7. Confirme que vale manter. A medida é carga de leitura reduzida (**principle-minimize-reader-load**). Se o diff não reduz carga em lugar nenhum, reverta.
8. Commits pequenos e ordenados: subtração, reshape, limpeza (**principle-sequence-verifiable-units**). PR só se pedido: **Opening a PR**.

**Resposta:** a estrutura que mudou, o pino, a prova de equivalência, o delta de carga de leitura, o que entrou e o que foi revertido. Nenhum comportamento novo.
