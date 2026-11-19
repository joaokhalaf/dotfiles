---
name: create-verification-skill
description: Crie uma skill de verificação específica do projeto, com inicialização, driver real, mapa de funcionalidades e evidências reproduzíveis de UI, CLI, API ou biblioteca.
---

# Criar uma skill de verificação

Gere instruções para um agente que nunca viu o projeto. A geração deve partir do
código e de execução observada, sem exigir Cursor, Herdr ou um runner da factory.
Leia [runtime](../poteto-mode/references/runtime.md) e as instruções do projeto.

## Descobrir antes de escrever

Inspecione README, scripts, rotas/comandos, testes e CI. Determine superfície real,
comandos de instalação/build/start, readiness utilizável, env e autenticação,
migrações/seed, driver existente e provas observáveis. Não leia ou copie segredos.
Prefira harness do projeto: browser/Playwright para UI, PTY para TUI, HTTP para API,
chamador público/teste de contrato para biblioteca. Não instale outro stack só
porque a skill original usa uma ferramenta diferente.

Verifique isolamento: portas, dados, perfis, serviços compartilhados. Não dirija a
sessão do usuário nem produza efeitos externos não autorizados. Teste local/dry-run
precisa provar o que escreve e o que deixa de executar; não confie no nome do modo.
Se o ambiente não inicia, diagnostique. Corrija apenas no escopo autorizado; sem
acesso ou solução possível, entregue diagnóstico e rascunho marcado como não provado.

## Gerar artefatos específicos do projeto

Atualize a skill existente quando houver. Caso contrário, crie verify-<app>/SKILL.md
na pasta de skills adotada pelo projeto. Sem convenção, use skills/verify-<app>/
e referencie seu caminho no arquivo de instruções/entrada do executor do projeto.
Não prometa descoberta automática só por criar uma pasta; não use .cursor/skills.
Inclua frontmatter name/description e estas instruções concretas, sem placeholders:

- Launch: instalação/start, dados iniciais, portas, readiness utilizável e teardown.
- Doctor: check somente leitura de versão, processo/porta próprios, dados e auth;
  não confundir servidor respondendo com fluxo utilizável.
- Drive: comandos/seletores públicos reais; alternativas só quando demonstradas.
- Evidence: ação e estado final esperado, efeitos colaterais, comandos/exit codes,
  logs/capturas e localização dos artefatos, associados ao conteúdo verificado.
- Cleanup: terminar somente processos/recursos criados pela verificação; nunca
  matar por nome ou apagar dados do usuário. Evidências sobrevivem ao cleanup.
- Helpers: criar scripts somente quando repetição ou confiabilidade justificar;
  mostrar invocação, dependências e validar sua execução. Sem helpers supérfluos.

Crie features/README.md como índice e um arquivo por jornada principal identificada
(com um conjunto inicial pequeno). Cada jornada explica objetivo observável,
pré-condições, acesso pela superfície pública, ações do driver, resultado esperado
e gotchas. Dados insuficientes são falha/lacuna, nunca motivo para enfraquecer a
jornada. Não finja cobertura de todas as features ao verificar apenas uma.

## Provar antes da entrega

Execute uma vez o procedimento gerado: launch → doctor → uma jornada real →
evidência → cleanup. Depois confirme que as evidências ainda existem. Corrija e
repita o que falhar e limpe recursos de tentativas interrompidas. Mocks só nas
fronteiras que o projeto já separa; setters internos não provam o caminho do usuário.

Sem essa execução, a skill é rascunho. Em ambiente substituto, diga o que só foi
verificado nele e quais passos permanecem sem prova no destino. Informe artefatos,
jornada executada, checks, limitações e como revisar o mapa quando o app mudar.
Não dependa de maintain-verification-skill se essa skill não estiver instalada.
