# Mapa de verificação do Notas

Este diretório é a fonte mantida para verificar o comportamento visível ao usuário do Notas. Leia o índice antes de dirigir o app e use o arquivo da feature correspondente como receita.

## Pré-condições base

- Suba o Notas em `http://127.0.0.1:4173` com um diretório de dados descartável.
- Defina `NOTES_DATA_DIR=/tmp/notes-verify-$RUN_ID` para execuções concorrentes não compartilharem estado.
- Crie as notas iniciais `Plano trimestral` e `Lista de compras`.
- Ponha `control-notes` e a CLI `notes` no `PATH`.
- Rode `control-notes doctor` e exija a URL, o diretório de dados e a revisão de build esperados.
- Nunca dirija uma instância que esta execução de verificação não iniciou.

## Convenções de direção

- Comece toda receita do estado base, salvo quando as pré-condições dizem outra coisa.
- Prefira papéis ARIA e nomes acessíveis a seletores CSS ou posição no DOM.
- Trate todo comando como literal. Mantenha nomes entre aspas e flags inalterados.
- Ações de browser via `control-notes browser`.
- Ações de terminal via `control-notes cli -- <comando>`.
- Restaure os dados iniciais depois de uma mutação. Não remova artefatos de prova no cleanup.

## Prova e relato de pulos

- Capture a ação do usuário e o estado resultante, não só a tela final.
- Prova de UI inclui snapshot ARIA e screenshot com a identidade do app visível.
- Prova de CLI inclui comando, stdout, stderr e exit code.
- Prova de mutação inclui uma segunda visão somente leitura do valor gravado.
- Registre o id da feature e o ponto de entrada usado em cada artefato.
- Reporte caminho inalcançável com o comando tentado e a pré-condição não atendida.
- Não reporte um ponto de entrada pulado como verificado por outro caminho.

## Contrato de cada feature

Cada arquivo de feature começa com um H1 e um parágrafo descrevendo o comportamento visível. Depois usa exatamente quatro H2, nesta ordem:

1. `Subfeatures` lista ids curtos, uma linha por comportamento.
2. `Como chegar (visão do usuário)` lista todo ponto de entrada do usuário.
3. `Dirigindo com <harness>` começa com `Pré-condições:` e usa marcadores rotulados que pareiam cada ação do usuário com um comando exato e um resultado observável.
4. `Pegadinhas` lista armadilhas que podem desperdiçar ou invalidar uma verificação.

Mantenha detalhes de implementação fora do mapa. Nomeie só caminhos do usuário, handles estáveis, estado necessário, comandos e prova observável.

## Features

- [Criar uma nota](criar-nota.md) cobre criação por browser e CLI, cancelamento, persistência e cleanup.
