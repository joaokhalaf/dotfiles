---
name: interrogate
description: Revisão adversarial de uma mudança ou design. Adversários tentam quebrar, e só sobrevive o achado provado por execução. Use para "interrogate", "revisão adversarial", "multi-model review", "desafia isso", "stress test", "acha os pontos cegos", "destrói isso", ou revisão de diff.
disable-model-invocation: true
---

# Interrogate

Adversários tentam quebrar uma mudança ou um design. Um achado sobrevive só quando uma execução o prova. Reporte os achados; não aplique correções.

## Enquadrar

O escopo é o que o usuário nomeia. Senão, o diff da branch desde a base de merge até a árvore de trabalho, incluindo arquivos não rastreados (`git status`; registre hashes do que não está commitado). Reafirme a intenção com suas palavras, a partir da mensagem do usuário, dos commits e da descrição do PR. Intenção obscura: pergunte.

## Escolher o modo

- **Leve:** mudança pequena ou sem delegação disponível. Você mesmo revisa: leia instruções do projeto, diff e chamadores afetados; priorize correção, contratos, erros, concorrência e impacto nos consumidores. Diga que é revisão própria, sem independência.
- **Completo:** mudança relevante ou pedido explícito. Use as Fases A (passos 3 e 4) e B do **arena** com estas mudanças: assentos no modelo da sessão mais outro provider disponível (ex.: Codex via T3); copie as mudanças não commitadas para cada worktree; em vez da tarefa da arena, dê a cada adversário o escopo, a intenção e este brief:

> Quebre esta mudança. Prove cada achado com uma execução contra o código real: teste falhando, script de repro ou saída de comando mostrando o comportamento errado. Para design ou plano, rode um protótipo ou sonde a árvore atual. Mantenha as repros na sua worktree. Reporte cada achado com título, comando exato, a saída que ele imprimiu e a saída que a intenção exige. Deixe de fora tudo que não executou: estilo, nomes, estrutura e riscos que dependem de mudança futura. Nenhum achado é um resultado válido.

## Verificar

Reexecute o comando de cada achado (**principle-prove-it-works**). Mantenha o achado quando a saída mostra a falha e a falha quebra a intenção. Descarte o resto. Junte achados com a mesma causa raiz. Falha que a base já tinha não é regressão introduzida.

Pule as Fases C, D e E do arena: adversários acham falhas diferentes, então o veredito mantém todo achado verificado, não a lista de um adversário.

Candidato de segurança: siga **security-gate** (fronteira e impacto demonstrados, refutação independente).

## Saída

- **Intenção:** a reafirmação.
- **Achados:** para cada achado verificado, arquivo/linha, comando, saída, como quebra a intenção e quais adversários acharam. "Nenhum achado verificado" quando nada sobrevive.
- **Descartados:** por adversário, quantos e por quê.
- **Cobertura:** modo usado, providers dos assentos, o que não foi verificado. Ausência de achados não prova correção.
