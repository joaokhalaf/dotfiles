---
name: figure-it-out
description: Projeta um playbook auditável quando nenhum outro serve, por exemplo numa migração grande, numa mudança ambiciosa em várias partes ou num trabalho que alguém revisa depois de se afastar. Escala o rigor à tarefa, roda um loop de hipóteses e registra as decisões. Use para /figure-it-out ou "descobre como fazer".
disable-model-invocation: true
---

# Figure it out

Quando a tarefa não combina com nenhum playbook, projete um. A entrega antes de qualquer código é o próprio fluxo: uma sequência de fases que escala o rigor à tarefa, aplica o método científico e deixa uma trilha que um humano audita depois de se afastar.

## Começo

Abra uma lista de tarefas cujo primeiro item é ler a seção Princípios do **poteto-mode**. Depois adicione as fases abaixo.

## Fase A: Enquadrar

Fundamente primeiro, depois se comprometa. Não comece antes de poder declarar:

- A definição de pronto como predicado falseável (**principle-prove-it-works**).
- Escopo quantificado: unidades e esforço aproximados, mais os bloqueios encontrados.
- O nível de rigor, com viés para cima. Portas de mão única e grande raio de impacto pedem mais; passos reversíveis de baixo risco, menos. Rigor é gates e artefatos, não "se esforçar mais".

Apresente o enquadramento e os trade-offs antes de uma execução longa. Trabalho reversível prossegue (**principle-never-block-on-the-human**), mas uma execução de várias horas merece um checkpoint.

## Fase B: Projetar o fluxo

Decomponha em unidades atômicas que entram de forma independente. Sequencie primeiro o desconhecido mais arriscado. Andaime e verificação antes de features (**principle-foundational-thinking**).

- Construa o harness de verificação antes do trabalho, com baseline capturado do estado anterior, para o check ler "valor antigo vs novo".
- Para decisões de design de mão única, use **architect** (e **arena** quando houver formatos concorrentes). Pule para trabalho mecânico de formato já concreto. Segunda arena sobre design resolvido é excesso (**principle-laziness-protocol**).
- Decida o que vai em fan-out. Paralelize só entre costuras, cada executor na sua worktree ou branch (**principle-separate-before-serializing-shared-state**). Não exagere no fan-out.
- Escreva a lista de fases projetada. Ela é o que o humano revisa.

Depois execute o projeto. Adicione os passos à lista entre as entradas das Fases C e D. Rode cada um sob a disciplina da Fase C e escreva a trilha da Fase D à medida que cada passo entra, não tudo no fim.

## Fase C: Rodar o loop

Cada unidade é um experimento. Declare a hipótese, faça a menor mudança, meça contra o predicado no artefato real, mantenha se avançou, reverta se não. Verifique cada unidade antes da próxima (**principle-sequence-verifiable-units**).

- Verifique inspecionando o artefato, nunca uma autodeclaração. Quando algo passa fácil demais, suspeite do método de observação antes do sistema.
- Trabalho delegado tem um juiz. Executor que burla o gate: resete e endureça o contrato. Gate errado: corrija o gate numa mudança própria em vez de contorná-lo.
- Veredito é VERIFICADO, NÃO VERIFICADO ou INCONCLUSIVO. Inconclusivo não é aprovação. Não esconda negativos.

## Fase D: Manter a trilha

Registre a execução via **show-me-your-work**. O trabalho daqui costuma ser ambicioso o bastante para commitar a trilha, para o revisor lê-la no PR.

## Fase E: Verificar e entregar

Confira o todo contra o predicado da Fase A no produto real, não só no harness. Codifique toda correção recorrente como gate, lint, check ou script (**principle-encode-lessons-in-structure**).

Os limites de Autonomia do **poteto-mode** continuam: push e PR só com pedido, merge só com autorização nomeando os PRs.

**Resposta:** o playbook projetado, o nível de rigor e por quê, o caminho da trilha, o que está verificado contra o predicado e o que segue aberto.
