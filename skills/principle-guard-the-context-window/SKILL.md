---
name: principle-guard-the-context-window
description: "Aplique quando o contexto está enchendo: saídas grandes, arquivos longos, leituras repetidas, planejamento de fan-out. Volume vai para subagentes; o main guarda resumos, não payloads brutos."
disable-model-invocation: true
---

# Guard the Context Window

**Por quê:** estourar o contexto degrada o raciocínio, cria artefatos de compressão e trava o progresso.

**Padrão:**
- **Volume vai para subagentes.** Logs, transcrições, artefatos e buscas amplas são lidos fora do main; volta só o achado reduzido.
- **Leia o necessário.** Faixas de linhas, buscas direcionadas, saída filtrada (`| tail`, `| head`, `jq`). Não releia o que já está no contexto.
- **Dimensione fases e limite escopo.** Limite arquivos por fase, defina orçamento de turnos, conte o custo dos mecanismos.
- **Resultados duráveis vão para arquivo.** Planos, logs de decisão e notas de retomada ficam em disco e são referenciados por caminho.
