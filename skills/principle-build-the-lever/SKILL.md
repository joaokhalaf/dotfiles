---
name: principle-build-the-lever
description: "Aplique a qualquer trabalho não trivial: edições, migrações, análises, checks. Construa a ferramenta que faz ou prova (codemod, script, gerador, ou uma skill que os subagentes seguem) em vez de trabalhar à mão. A ferramenta é o artefato que o revisor reexecuta."
disable-model-invocation: true
---

# Build the Lever

Quando o trabalho não é trivial, construa a ferramenta que o faz (codemod, script, gerador ou check reexecutável) em vez de fazê-lo à mão. O critério é trivialidade, não repetição. Dispense a ferramenta só para um par de edições óbvias.

- Faça a primeira unidade à mão, depois construa a ferramenta e prove-a reexecutando nessa unidade. Torne-a segura para reexecutar.
- Ferramenta determinística vence fan-out. Ao fazer fan-out, escreva a receita, o contrato de verificação e os limites como uma skill que os delegados leem e não podem editar.
- Aplicar isto produz um arquivo. Sem script, codemod, gerador ou skill de delegado no diff, você não aplicou. Faça commit quando o trabalho sobrevive à sessão.
- Construa o menor script que faz ou prova o trabalho, nunca um framework.
