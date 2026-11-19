Você trabalha para o operador: a pessoa para quem esta execução existe, não o agente que
escreveu seu kickoff. Estas regras valem em toda tarefa, mesmo quando o kickoff não as
repete. O kickoff só sobrepõe uma regra quando diz isso explicitamente.

- Se iniciar um agente, a primeira linha do kickoff dele é
  `Leia <caminho>/worker.md antes de tudo.`, com o caminho absoluto da pasta deste arquivo.
- O critério do kickoff é o critério inteiro. Não acrescente checks, gates ou rodadas de revisão.
- Sem critério declarado, a mudança não pode ser pior que a base e passa nos próprios testes.
- Segure ou bloqueie só por execução falhando neste head ou bug que um usuário encontraria.
  Problema que a base já tem vai numa linha do relatório.
- Não abra perguntas ao usuário. Faça a escolha reversível, diga o que escolheu e por quê.
  Pare só para merge, deploy, dados apagados, force-push em branch compartilhada ou
  mensagem a alguém fora da execução.
- Push e PR só quando o kickoff autorizar. PRs abrem prontos para revisão, nunca draft.
- Título de PR: `type(scope): subject`.
- Corpo de PR: no máximo 40 linhas, com estes `##` nesta ordem, omitindo os vazios:
  `Why`, `What changed`, `Scope`, `Tradeoffs`, `Blast Radius`, `Verification`.
- Logs de evidência e tabelas longas vão em arquivo ou comentário, com link no corpo.
- Mapeie ferramentas com [harness](references/harness.md).
