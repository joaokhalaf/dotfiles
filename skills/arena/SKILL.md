---
name: arena
description: Coloca N candidatos em paralelo na mesma tarefa, escolhe uma base e enxerta nela as melhores partes dos perdedores. Use para /arena, "joga na arena", ou quando uma única tentativa num artefato não trivial fixaria o formato errado.
disable-model-invocation: true
---

# Arena

Abra uma lista de tarefas com uma entrada por fase (Enquadrar, Fan-out, Juiz cruzado, Escolher, Enxertar, Verificar) antes de lançar qualquer coisa. Mapeie ferramentas com o harness do **poteto-mode** (`../poteto-mode/references/harness.md`).

## Fase A: Enquadrar

Todo candidato recebe o mesmo prompt; o prompt é o contrato.

1. Declare o artefato que cada candidato produz.
2. Derive a rubrica: 3-6 critérios concretos e avaliáveis do que é sucesso *nesta* tarefa. É a ferramenta de quem escolhe na Fase D. Candidatos veem só a tarefa.
3. Escolha os candidatos. Padrão: três subagentes no modelo da sessão. Invocar `/arena` autoriza usar outro provider disponível num assento (ex.: Codex via `delegate_task` no T3) para diversidade real. Sem outro provider, diga que a diversidade é só de contexto. Mais assentos para direções de design múltiplas.
4. Cada candidato tem seu próprio local de saída: worktree git quando possível, senão `<scratch>/arena-<slug>/candidato-<n>/` (**principle-separate-before-serializing-shared-state**).

## Fase B: Fan-out

Lance os N subagentes de uma vez, cada um com a tarefa, o caminho do material compartilhado, seu caminho de saída e a instrução de produzir o artefato mais uma justificativa curta nomeando as alternativas consideradas e o que rejeitou. A primeira linha de cada kickoff segue o **poteto-mode**: `Leia <caminho>/worker.md antes de tudo.`

Candidato sem saída: siga com N-1 e registre a desistência.

## Fase C: Juiz cruzado

Depois que todos terminarem, lance um juiz somente leitura. Preferência: um provider diferente do seu (ex.: Codex via T3). Sem isso, um contexto novo do modelo da sessão, e diga que o juiz é do mesmo vendor. Enquanto você lê na Fase D, o juiz pontua cada candidato, por rótulo de caminho, em cada critério, e recomenda uma base.

## Fase D: Escolher a base

Leia cada candidato inteiro antes de escolher. Pontue pela rubrica, critério a critério, não por impressão geral, e compare com o juiz. Concordância confirma a escolha. Discordância indica viés ou rubrica ambígua: leia as duas justificativas antes de decidir.

Escolha a base que um mantenedor futuro estende mais fácil sem quebrar invariantes. Empate: prefira a fronteira mais limpa ou a API menor (**principle-laziness-protocol**).

## Fase E: Enxertar

Percorra cada perdedor uma vez mais pelo que vale portar para a base, normalmente uma ou duas coisas por candidato. Incorpore cada enxerto à mão (**principle-redesign-from-first-principles**), para o resultado ficar coerente sob um modelo mental. Não cole mecanicamente.

Se os candidatos convergem num formato, é concordância forte: registre e entregue o consenso, sem enxerto. Se divergem muito, a Fase A ficou subespecificada: reenquadre e rode de novo em vez de fazer média.

## Fase F: Verificar

Verifique o artefato sintetizado como qualquer saída (**principle-prove-it-works**). Problema que a arena não viu: ou a Fase A estava errada (reenquadre e rode de novo) ou um candidato pegou e você perdeu o enxerto (volte à Fase E). Não disfarce.

## Saídas

Um artefato sintetizado, com nota curta ao lado: a base e por quê, o veredito do juiz e de que provider ele era, cada enxerto com seu candidato de origem, o que foi rejeitado e por quê, convergência ou desistências, e o resultado da verificação.
