---
name: correct
description: Acha os erros que agentes repetem neste repo e torna cada um impossível. Arquitetura primeiro, depois tipos, depois lint cuja mensagem nomeia a correção, depois teste, e docs por último. Prova que cada check falha num erro passado real. Use para /correct ou quando o usuário corrige o mesmo erro de novo.
disable-model-invocation: true
---

# Correct

O operador continua corrigindo agentes neste repo pelos mesmos erros. Mude o repo para o próximo agente não conseguir cometê-los.

Assuma que todo colaborador é um agente que só vê os arquivos que abriu, copia o exemplo mais próximo e segue o caminho mais curto que compila. Projete o repo para que uma mudança que parece certa vista de um arquivo esteja certa para o repo inteiro.

## Achar as classes de erro

Leia commits recentes, reverts, comentários de review, arquivos de instrução de agentes e comentários que explicam workarounds. Agrupe os erros em classes. Uma classe conta quando aconteceu duas vezes. Não invente recorrência.

## Corrigir cada classe no nível mais alto que funciona

1. **Eliminar com arquitetura.** Cada estado com um dono, cada tarefa com um jeito suportado. Esconda internos para o import errado falhar. Troque listas sincronizadas à mão por uma fonte de verdade. Apague jeitos antigos e código morto que um agente copiaria.
2. **Impor com tipos, para o estado ruim não poder ser escrito.** Se código ruim ainda compila, adicione lint ou check de CI cujo erro nomeia o arquivo, tipo ou função a usar no lugar. Padrão já comum: falhe só quando a mudança acrescenta mais.
3. **Testar o comportamento.** Corrija ou apague teste que continua passando quando o comportamento que checa quebra, ou que falha quando só os internos mudam (**principle-test-behavior-not-implementation**).
4. **Docs ou regras de agente por último, só para decisões de julgamento.** Nada falha quando um agente as ignora.

A [política de qualidade](../poteto-mode/references/quality.md) é o caso de referência: proibir novos `useEffect` num projeto React é uma regra AST de lint que aponta a alternativa do projeto, não uma linha no AGENTS.md.

## Corrigir e provar

Corrija agora as classes mais frequentes, um commit cada. Prove que cada check novo falha num erro passado real e aceita o caminho correto. Rode o mesmo comando localmente e na CI. Exceções ficam na linha ofensora com motivo, data de expiração e aprovação humana. Não relaxe um gate para ficar verde.

## Manter a tabela de regras

Mantenha no arquivo de instruções de agentes do projeto uma tabela regra → o que a impõe → comando. Quando o operador corrigir você, corrija o erro e adicione a regra. Se a regra já estava lá e nada a impõe, é repetição: corrija no nível mais alto na mesma mudança. Remova a regra quando o erro não puder mais acontecer.

Commits só no escopo pedido; push e PR só com pedido.

**Resposta:** cada classe com sua evidência, o nível escolhido e por que um nível mais alto não funcionou.
