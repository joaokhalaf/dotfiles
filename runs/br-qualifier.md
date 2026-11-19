# Rodada real — qualificatório brasileiro de Valorant

## Pedido e autorização

Usuário pediu testar a factory criando o qualificatório e entregando tudo até abrir
PRs. Confirmou escopo somente Brasil, VCT Americas Kickoff 2027. Push/PR autorizados;
merge não solicitado. Main conduz pelo chat, sem runner Python.

## Base e entregas

Repo /home/khalaf/work/esports-simulator, base master 32a5e9569f37c1eea936b715942b0db583151755.
Gates de qualidade anteriormente locais foram commitados em 8c28f0e0c52577e458fcd9affbe5a300a6bd5d73,
branch chore/factory-quality-gates. PR https://github.com/joaokhalaf/esports-simulator/pull/15
aberto sobre master; CI em andamento na última consulta. Primeiro push recusado
por privacidade de email, resolvido no próprio commit usando noreply GitHub,
sem alterar privacidade da conta.

Feature na branch feat/valorant-brazil-qualifier, dependente do PR15. Um único
agente escritor brazil_qualifier_owner no checkout compartilhado. Tentativa de
worktree via delegate_task recusada por vínculo do projeto da conversa; nenhum
child foi iniciado pela chamada recusada. Main não altera arquivos da feature
enquanto o owner trabalha. Revisão será em contexto separado e somente leitura.

## Arquitetura e critérios

BrazilDraft somente palpites/version, roster curado fixo, reutiliza simulateAmericas.
Rota dedicada /simulacoes/brasil, acesso na sidebar/calendário; manter Worlds e
simulador genérico Americas. Lista de 16: 6Q1 +4Q2 +6 convidados. Resultados reais
travados, W.O. sem placar inventado. Simular suíço/playoffs até campeão/vice;
persistência e desfazer via eventos, sem useEffect. Fontes/data visíveis e futuro
claramente simulado. Não criar NA/LATAM/LCQ ou scraping/live neste escopo.

## Fontes e ambiente

Consulta 17/11/2026. Riot anuncia suíço 20–22nov, playoffs 26–29nov/3–6dez:
https://valorantesports.com/pt-BR/news/2027-vct-americas-kickoff-brazil-qualifiers
Q2 concluída e resultados/W.O.:
https://www.vlr.gg/event/3187/vct-2027-america-kickoff-brazil-open-qualifier
Lista atual dos participantes:
https://www.vlr.gg/event/3183/vct-2027-america-kickoff-brazil-qualifier-playoffs/swiss-stage
https://www.thespike.gg/br/valorant/news/valorant-playoffs-qualify-vct-americas-kickoff-times/9250
Não atribuir convites BR à matéria NA do Esportnow nem à lista antiga de 30/10.

Docker ausente. Harness Cloudflare existente oferece Miniflare/D1 efêmero e
Playwright sem Postgres. Browser local obrigatório conforme instruções da sessão.
Checks do código e nova jornada precisam ser executados; não confundir CI pendente
com aprovado. Rodada antiga em .factory e worktree de homepage permanecem intactas.

## Entrega e evidências

PR15 qualidade: https://github.com/joaokhalaf/esports-simulator/pull/15
Head atualizado93a78046e2b5f4a93c5bb38b61b0749c23d6a15d; CI remoto SUCCESS.
Revisor quality_gate_review reproduziu escapes com destructuring de chave string e
alias envolvido em satisfies; main corrigiu ambos com regressões (19/19 testes).
Baseline legada não foi aumentada e arquivos da feature não entraram nesse commit.

PR16 funcionalidade: https://github.com/joaokhalaf/esports-simulator/pull/16
Head f7412039024505b8e84cb3d8bb135decea069c58, base chore/factory-quality-gates.
Merge PR15 primeiro, depois retarget PR16 para master; nenhum merge foi executado.
Na última consulta CI remoto PR16 estava IN_PROGRESS; ainda não declarar verde.

Owner brazil_qualifier_owner entregou sete arquivos de domínio, UI, documentação
e testes. pnpm ci passou (19 policies,20 avisos CSS prévios); pnpm test26 passaram,
1 integração PostgreSQL pulada localmente; web check-types/build e Cloudflare build
passaram. Chromium dedicado:3/3 E2E contra Worker+Miniflare/D1 passaram. Foi necessário
instalar browser no cache e reutilizar libs locais do browser via LD_LIBRARY_PATH;
não houve sudo nem alteração de gates. Sem Docker neste ambiente.

Revisor brazil_feature_review em contexto separado não encontrou bug concreto:
4/4 testes e1000 cenários aleatórios comprovaram20 séries suíças,8 classificados,
campeão/vice distintos, roundtrip e invalidação por remoção de resultados.
Não se apresentou como revisão multi-modelo; ambos herdaram o modelo do executor.

Main executou local-browser: simulou suíço (20 palpites salvos), playoffs até
Elevate/ARRANCA DREAMS no cenário aleatório, reload preservando resultado,
reset e undo restaurando, W.O. de Master Bank visível e sem botões de edição.
Viewport390: document.scrollWidth=390 e innerWidth=390, sem overflow horizontal.
Screenshot local /tmp/valorant-brazil-mobile.png inspecionada. Nenhum pageerror
capturado. Console do Vite mostrou aviso de script em componente React associado
ao ThemeProvider global já existente; não foi tratado como prova de ausência de
avisos nem expandido para refatoração fora do pedido. Browser e servidor3211
criados pelo main foram encerrados; harness do owner também foi limpo.

## Estado e próximo passo

Os dois PRs estão abertos, sem merge. CI de PR16 ainda em andamento na última
consulta; acompanhar pelo mecanismo de watch do executor, corrigindo falhas reais.
Rodada antiga da factory e worktree de homepage preservadas.

## Observação da factory

O main escolheu fluxo e escopo pelo chat, delegou um owner, revisou de forma
independente e corrigiu achados demonstrados; não executou o runner Python.
A ferramenta de worktree não aceitou outro projeto nesta conversa, então foi
usado único escritor de feature no checkout, com main limitado a scripts reservados
separadamente. Esse é um limite observado do executor, não promessa de isolamento.
