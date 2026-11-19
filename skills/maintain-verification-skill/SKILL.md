---
name: maintain-verification-skill
description: Passada periódica que mantém honestos a skill de verificação do projeto e seu mapa de features, com leitores de código em paralelo por feature, uma sessão ao vivo dirigindo todas as features e no máximo um PR de correções provadas. Use para /maintain-verification-skill ou "audita a skill de verificação".
disable-model-invocation: true
---

# Manter uma skill de verificação

Um mapa de features apodrece no momento em que o app muda. Esta é a manutenção de uma skill gerada por **create-verification-skill** (ou qualquer skill de verificação local com mapa de features). A unidade de rigor é a feature, não cada frase: cubra todo arquivo de feature pelo código e exercite toda feature ao vivo, sem executar cada marcador.

## Resultados

Escolha um e diga qual:

- **clean:** toda feature teve cobertura de código e ao vivo; nada a entregar. Sem branch, sem PR.
- **changed:** correções provadas de doc, harness ou mapa, numa branch local. PR só se o usuário pediu.
- **blocked:** a cobertura não terminou ou uma correção provada não pôde ser entregue com segurança. Diga exatamente o que bloqueou.

## Escopo de edição

Edite só o diretório da própria skill de verificação (SKILL.md, `features/` e scripts de harness dela). Nunca edite código de produto durante a passada: comportamento que o mapa descreve e o app não faz mais é deriva de doc (corrija o mapa) ou regressão de produto (reporte, não disfarce na doc).

## Passada

0. **Localize o alvo.** Ache a skill de verificação: a skill local cujo corpo tem seções de launch e drive e um mapa de features (normalmente `.claude/skills/verify-*/`). Várias candidatas: pergunte qual. Nenhuma: pare e aponte **create-verification-skill** em vez de inventar um alvo.
1. **Higiene do índice.** Leia o README do mapa e liste os arquivos irmãos. Corrija entradas faltando, sobrando, duplicadas ou mortas.
2. **Onda de código.** Um subagente somente leitura por arquivo de feature, em paralelo. Cada um explica "como esta feature visível funciona?" pelo código, aponta provável deriva com citações e devolve uma receita de verificação ao vivo. Eles nunca dirigem o app nem editam arquivos. Formato: resumo da feature / pontos de entrada no código / deriva provável ou nenhuma / uma receita.
3. **Reconciliar.** Todo arquivo de feature tem um resumo devolvido. Junte receitas sobrepostas no menor número prático de estados do app. Confira por amostragem a deriva citada; não reprove alegações limpas. Varra mudanças recentes atrás de superfícies visíveis ausentes do mapa; exija um caminho concreto no código antes de chamá-la de ausente.
4. **Passada ao vivo.** Obrigatória mesmo com código limpo. O coordenador dirige tudo, seguindo o modelo de launch da própria skill: uma instância longa dirigida em série para servidores e UIs, ou uma sessão isolada nova por direção para CLIs de vida curta. Exercite toda feature pelo menos uma vez e mantenha três invariantes a passada inteira, qualquer que seja a falha:
   1. Nunca dirija uma instância sem doctor desde a última surpresa: doctor antes da primeira direção, em cada sessão nova quando sessões são a unidade, e de novo depois de qualquer direção que falhou. Onde o doctor não enxerga a falha (UI travada num processo saudável), resete para um estado conhecido ou relance.
   2. A evidência capturada sobrevive a todo cleanup, conferida no local nomeado, não presumida.
   3. Nada que uma direção iniciou sobrevive à sua utilidade: resíduo de iteração falha é limpo, esteja a sessão travada, encerrada ou compartilhada (numa instância compartilhada, limpe o resíduo, não a instância).

   Falha de doctor causada por deriva da skill é deriva: corrija dentro do escopo e tente uma vez (reinicie só o que a correção invalidou) antes de chamar a passada de `blocked`. Feature inalcançável é `verificada-inalcançável` só com a pré-condição concreta (auth, permissão, SO, estado externo) e a rota tentada; se o mapa omite essa pré-condição, é deriva. Correção de harness feita na triagem é dirigida ao vivo de novo antes de entrar. O teardown final acontece depois da última direção, inclusive as reprovas.
5. **Triagem.** Descrição de usuário errada ou ausente: deriva de doc, corrija. Comportamento que funciona mas o harness não dirige: lacuna de harness, corrija (scripts executáveis, invocação documentada no corpo da skill). Comportamento do app realmente quebrado: lacuna de produto; registre para o usuário, fora destas correções.
6. **Entregar ou parar.** Em changed: releia cada arquivo alterado e faça commits pequenos; PR só com pedido. Em clean ou blocked: sem commits; reporte o resultado e a cobertura com honestidade.

Guarde notas curtas da passada (features cobertas, pré-condições inalcançáveis, deriva confirmada, resultado) num local de rascunho, fora do commit.
