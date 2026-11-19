---
name: create-verification-skill
description: Gera uma skill de verificação local do projeto que dirige o app como um usuário faz, em qualquer linguagem, framework ou plataforma. Use para /create-verification-skill, "cria uma skill de controle para este repo", ou quando o projeto não tem jeito scriptado de provar comportamento de UI, CLI ou serviço.
disable-model-invocation: true
---

# Criar uma skill de verificação

Todo projeto sério precisa de um jeito scriptado de dirigir o app real e provar comportamento: subir, exercitar uma feature como um usuário e capturar evidência. Esta skill gera isso como skill local do projeto, sob medida para o repo. O leitor é o próximo agente, não um humano: ele vai ler a frio, no meio de uma tarefa, sem nunca ter visto o app.

## 1. Entreviste o repo, não o usuário

Responda pelo código e pergunte ao usuário só o que não dá para observar. Não leia nem copie segredos.

- **Superfície:** o que o usuário toca? UI web, CLI/TUI, app desktop, API, mobile, biblioteca? Com várias, escolha a principal e anote as outras.
- **Execução:** como o app sobe localmente? Prefira o comando de dev documentado do próprio repo (scripts do package, Makefile, README). Anote portas, variáveis de ambiente, dados iniciais, auth.
- **Direção:** como um agente interage programaticamente? Harnesses existentes primeiro: specs Playwright/Cypress, scripts expect, helpers PTY, endpoints via curl, porta de debug. Só depois uma receita genérica: MCP `local-browser` ou CDP para web e Electron, tmux/PTY para CLI/TUI, HTTP puro para serviços. Não instale outra stack só porque o upstream usa uma ferramenta diferente.
- **Observação:** que evidência dá para capturar? Screenshots, transcrições de terminal, corpos de resposta, logs, exit codes, estado do banco.
- **Isolamento:** duas instâncias rodam lado a lado (portas, diretórios de dados, perfis)? Se não, diga isso na skill gerada: recusar dirigir duas vezes uma instância compartilhada é melhor que corromper a sessão do usuário. Nunca dirija a sessão do usuário nem produza efeitos externos não autorizados.

Se o checkout não compila ou não sobe como está, corrija primeiro dentro do escopo autorizado, ou reporte com precisão, antes de gerar: skill escrita contra uma base quebrada ensina passos errados. Quando um recurso irrelevante ausente bloqueia o start (diretório estático que a API nunca serve, config de exemplo), a skill gerada pode criá-lo, marcado como andaime de verificação, e removê-lo no cleanup.

## 2. Gere a skill

Atualize a skill de verificação existente quando houver. Senão, escreva `.claude/skills/verify-<app>/SKILL.md` no projeto, e acrescente ao `AGENTS.md` do projeto uma linha apontando para esse caminho, para o Codex e o OpenCode a acharem. Frontmatter YAML com `name: verify-<app>` e uma `description` que nomeia o app, a superfície e quando usar; sem frontmatter a skill não registra. Seções, cada uma baseada no que a entrevista achou, sem placeholders:

- **Launch:** o comando exato que sobe o app para verificação e como saber que está pronto (linha de log, prompt). O launch alcança estado utilizável a partir de um diretório de dados vazio, com migrações e dados iniciais. Pronto significa utilizável, não só um processo respondendo: um health check de banco pode passar enquanto os scripts de init ainda rodam. Inclua teardown. Para CLI ou TUI de vida curta não há servidor: launch é compilar o binário (ou instalar deps) uma vez e iniciar cada direção na sua própria sessão PTY ou tmux isolada.
- **Doctor:** um check somente leitura que responde "vale dirigir esta instância?": processo no ar, versão/build certos, porta é nossa, auth válida. O agente roda isto primeiro sempre que algo parecer estranho.
- **Drive:** a receita do harness com seletores e comandos reais deste repo, não exemplos. Prefira handles estáveis (labels ARIA, data attributes, strings de prompt, rotas) a coordenadas e ordem de tab.
- **Evidence:** o que capturar como prova e para onde vai. Padrões de prova: exercite o caminho real do usuário, não setters internos nem endpoints só de teste; capture a ação e o estado resultante, não só a tela final; verifique efeitos colaterais (arquivos escritos, linhas inseridas, mensagens enviadas) além do visível; mocks só onde uma fronteira de produção já isola o sistema externo. Quando o caminho seguro é dry-run ou modo de teste, verifique o que ele realmente pula observando (arquivos, rede, refs git), sem confiar no nome: alguns dry-runs ainda acessam a rede ou abrem um browser.
- **Cleanup:** como derrubar as instâncias que a execução criou. Nunca mate por nome de processo; mate o que você iniciou. Cleanup remove instâncias e estado de rascunho, nunca a evidência: os artefatos de prova sobrevivem ao teardown, num local que a skill nomeia.
- **Helpers:** todo script que a skill traz é executável e sua invocação aparece no corpo da skill. Helper que o leitor precisa desmontar para entender não é helper. Só crie helpers quando repetição ou confiabilidade justificar.

## 3. Semeie o mapa de features

Crie `.claude/skills/verify-<app>/features/README.md` mais um arquivo por feature visível ao usuário que você identificar (as 3-5 principais para começar, a partir de rotas, comandos, menus ou docs). Siga o formato de [feature-map-example](references/feature-map-example/README.md): um README índice e um arquivo por feature. Cada arquivo responde, do ponto de vista do usuário: o que é a feature, como chegar nela, como dirigi-la com o harness e qual estado final observável prova que funciona. Os quatro H2 são `Subfeatures`, `Como chegar (visão do usuário)`, `Dirigindo com <harness>` e `Pegadinhas`. Se os dados iniciais não têm uma pré-condição de que uma jornada precisa, a jornada reporta falha e o motivo vai em `Pegadinhas`. Nunca enfraqueça a jornada para passar. O mapa é a fonte mantida de verificação do repo; uma prova que dirige um único ponto de entrada conveniente está incompleta quando o mapa lista outros.

## 4. Prove a skill gerada antes de entregar

Rode as próprias instruções dela uma vez de ponta a ponta: launch, doctor, dirigir UMA feature mapeada, capturar evidência, cleanup. Depois do cleanup, confirme que a evidência ainda existe no local nomeado; cleanup que come a prova reprova este passo. Corrija o que falhar e rode o cleanup gerado depois de cada iteração falha também, para tentativas quebradas não deixarem processos e portas para trás. Skill gerada que nunca rodou é rascunho, não entrega. Se você provou num substituto do alvo real (container no lugar de uma VM nova, stack local no lugar de remota), liste cada passo de setup que o substituto fez e o alvo não fará; esses passos ficam sem prova até uma execução no alvo real.

## 5. Ofereça a manutenção

Aponte **maintain-verification-skill** para manter o mapa honesto conforme o app muda. Sugira cadência só se o usuário pedir.
