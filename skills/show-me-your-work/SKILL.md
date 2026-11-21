---
name: show-me-your-work
description: Mantém uma trilha de decisões revisável em trabalho longo ou sem supervisão. Usa um log TSV com uma linha por decisão (o quê, por quê, evidência, resultado). O log fica local por padrão e é commitado quando o revisor precisa da trilha. Use para /show-me-your-work, execuções autônomas ou em fases, ou trabalho que alguém revisa depois de se afastar.
disable-model-invocation: true
---

# Show me your work

Mantenha um único log canônico.

## Formato

Um arquivo TSV, uma linha por decisão. Células numa linha só. Evidência é ponteiro, não prosa.

Copie `references/decision-log-template.tsv` (a linha de cabeçalho) para começar. Colunas:

- **ts.** Timestamp ISO8601.
- **phase.** A fase ou frente de trabalho.
- **decision.** O que foi escolhido ou feito, numa linha.
- **why.** A razão em palavras simples. Se um princípio motivou, diga em linguagem comum, não como etiqueta.
- **evidence.** Link ou caminho que prova: SHA de commit, número de PR, `arquivo:linha`, caminho de artefato, trace ou screenshot. Nunca um parágrafo.
- **result.** Resultado ou estado do predicado: `testes verdes`, `revertido`, `pixel-diff 0`, `INCONCLUSIVO`, `aberto`.

Exemplo, em linguagem simples para o revisor ler de relance:

```
ts	phase	decision	why	evidence	result
2026-05-24T09:02:00Z	frame	contei o trabalho primeiro, ~100 componentes e ~75 horas	queria saber o tamanho antes de uma execução longa	commit 3a9f1c2	5 pendências para resolver antes de começar
2026-05-24T09:40:00Z	harness	capturei screenshots da versão antiga antes de mudar algo	para comparar antigo e novo e pegar mudança visual	scripts/snapshot.sh, baseline/	120 screenshots de referência
2026-05-24T11:15:00Z	widget	migrei os estilos do widget sem mudar a aparência	mudança pequena e resultado idêntico	commit 7c21e0a, pixel-diff 0	idêntico, testes passam
2026-05-24T12:30:00Z	widget	descartei o trabalho de um subagente porque os screenshots estavam em branco	conferi os arquivos reais em vez de confiar no resumo	worktree resetada	revertido, instruções apertadas
```

## Registrando uma linha

Escreva cada entrada como contaria a um colega o que fez. Palavras simples, ações concretas, sem jargão (**unslop** vale para o log).

Use `scripts/log.sh <log> <phase> <decision> <why> <evidence> <result>`. Ele carimba `ts`, escreve o cabeçalho no primeiro uso, remove tabs e quebras de linha, e prefixa com aspa simples células que começam com `=`, `+`, `-` ou `@`. Um `printf` direto também serve, com o mesmo cuidado quando as células vêm de texto gerado ou do usuário.

Registre pontos de decisão e checkpoints, não cada ação: bifurcação escolhida, unidade concluída com o resultado da verificação, pivô ou reversão com o gatilho, bloqueio, gate corrigido. Em loops, uma linha por iteração. Pule o trivial.

Uma execução é uma conversa de agente, incluindo turnos posteriores e resumos dela. Retomada, agente substituto ou chat novo começam outra execução. Quando uma execução adiciona a um log que já tem linhas, sua primeira linha tem phase `start`, e também sua primeira linha depois do `start` de outra execução. Por isso, ao voltar a um log num turno posterior, leia as últimas linhas para ver se outra execução escreveu. A linha `start` nomeia a faixa de `ts` das linhas anteriores que esta execução não escreveu, e a evidência identifica esta execução (id da sessão ou thread). `start` não tem outro uso.

## Onde fica

Por padrão o log é artefato de trabalho, fora do git: `decisions.tsv` no diretório de trabalho, ou `.audit/<slug>.tsv` quando várias frentes rodam ao mesmo tempo.

Faça commit só quando o trabalho for ambicioso a ponto de o revisor precisar da trilha para confiar no resultado.

## Regras

- Só acrescentar. Decisão errada ganha uma linha nova que a substitui. Nunca edite nem apague histórico.
- Prefira evidência produzida por scripts commitados a verificações manuais avulsas (**principle-encode-lessons-in-structure**).

## Auditar o log contra a transcrição

Ao fim da execução, antes de entregar, confira se o log disse a verdade. Leia a transcrição desta execução (caminhos no harness do **poteto-mode**; só deste workspace). Percorra as linhas desta execução contra o que aconteceu. Cada trecho começa numa linha `start` desta execução, ou na primeira linha se esta execução criou o log, e termina no próximo `start` de outra execução:

- Toda linha corresponde a uma decisão ou ação real.
- A evidência de cada linha resolve e mostra o que a linha alega.
- Bifurcação, pivô ou abordagem abandonada que moldou o trabalho e não está registrada é lacuna: adicione.

Corrija o log, não a história. A auditoria nunca edita nem remove linhas, nem inventadas. Linha sem decisão ou ação real, ou com alegação ou evidência errada, ganha uma linha que a substitui com o que aconteceu e um ponteiro que resolve.

## Revisão da trilha por outro modelo

Antes de entregar, peça a um avaliador (outro modelo Claude, effort um nível acima; ver harness do **poteto-mode**) que leia a trilha e a transcrição e aponte o que o usuário deve olhar. Não é refazer o trabalho; é procurar o que está fraco ou arriscado:

- Decisões com evidência fraca ou ausente.
- Verificações puladas ou alegadas sem prova na transcrição.
- Escolhas arriscadas em retrospecto (prematuras, que ampliam escopo, que mascaram sintoma).
- Lacunas que o usuário perderia numa leitura rápida.

Toda resposta de execução com trilha termina com uma seção "Atenção". Primeira linha: `revisado por <modelo/effort>`. Depois, cada apontamento ligado a linhas ou momentos específicos. "Nenhum apontamento" é válido; omitir o revisor não é.

## Lendo a trilha

De cima para baixo, seguindo os ponteiros de evidência, conferindo por amostragem. O GitHub mostra um TSV commitado como tabela. No terminal: `column -s$'\t' -t decisions.tsv`.

## Compondo com outras skills

Outras skills mandam sua trilha para cá em vez de inventar uma. Referencie pelo nome e deixe esta skill ser dona do formato.
