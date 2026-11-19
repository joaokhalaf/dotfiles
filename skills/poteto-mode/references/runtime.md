# Contrato do executor

## Conversa como entrada padrão

O chat principal conduz a tarefa. Use as ferramentas reais da sessão: arquivos,
terminal, Git, navegador e delegação quando disponíveis. Skills orientam decisões;
não fornecem ferramentas nem concedem permissões. Não exija runner, banco de fila,
JSON, Herdr ou modelos fixos para usar poteto-mode. Uma interface Desktop só pode
executar o fluxo até onde suas capacidades locais permitem.

Respeite instruções do projeto e permissões do executor. Herdr é uma integração
opcional do produto; quando as instruções desta sessão exigirem sua coordenação,
siga-as. Não conclua que ausência de Herdr permite ignorar uma exigência obrigatória.
No modo sem integração, não invente reservas ou locks: main pode trabalhar no
checkout atual, e escritores delegados precisam de isolamento/posse claros.

Use a ferramenta nativa de agentes oferecida pelo executor. Em Codex/Claude/T3,
respeite a forma disponível de spawn, worktree e espera; nunca execute CLIs de
agentes no shell para contornar o mecanismo autorizado de delegação. Herde modelo
e configurações, salvo escolha do usuário ou necessidade previamente autorizada.
Contextos separados do mesmo modelo são revisão independente, não multi-modelo.

## Coordenação externa, quando aplicável

Herdr: join na raiz real com nome, papel e HC_TERMINAL_ID quando definido;
status/inbox; reserve arquivos exatos e check antes de editar; releia mudanças
inesperadas; renove reservas; reconheça mensagens tratadas; publique evidências
e arquivos; leave ao terminar. Reserva negada ou falta de permissão bloqueia o
arquivo/ação em questão; não faça fallback para contornar. Reservas são cooperativas.

## Evidência e falhas

Valide o comportamento com os checks e a superfície do projeto. Browser pode usar
local-browser, Playwright ou driver autorizado existente, conforme as instruções
da sessão. Compilação isolada não prova comportamento. Se um comando falhar por
restrição de ambiente, registre o erro e procure equivalência técnica preservando
a mesma asserção. Exemplo: node --import tsx --test pode evitar o IPC auxiliar do
CLI tsx sem alterar os testes. Se o comando literal for critério obrigatório ou
não houver equivalência demonstrada, relate a lacuna e não marque como aprovado.

Diferencie defeito do produto, restrição do ambiente e evidência ausente. Não
consuma tentativas repetindo uma ação negada sem mudança relevante. Preserve
trabalho e evidências para retomar. Não flexibilize sandbox, gates ou permissões
como resposta automática a uma falha.

## Runner opcional de terminal

Somente quando o operador escolher esse modo, scripts/factory.py controla fila,
lock, worktrees, limites, autor e revisão por CLIs. Não inicia nem retoma por ler
esta skill. Os perfis home/work e a configuração JSON valem para esse runner;
não selecionam o modelo desta conversa ou de seus agentes nativos.

O runner informa coordination local (padrão) ou herdr. Em local o host mantém fila,
worktree dedicada, escopo e commits, sem exigir chamadas Herdr; requisitos
obrigatórios específicos do projeto continuam válidos. Em herdr, use o protocolo
externo; não faça fallback após recusa. Recover exige ausência de processos antigos.

O runner entrega verified_local, sem push/PR/merge. PRs precisam de verificação
remota no head atual. Logs e tokens não medem saldo de assinatura. O autor deixa
alterações; o host verifica escopo e cria commit. Nenhuma dessas etapas do runner
é obrigatória para uma tarefa diretamente no chat.
