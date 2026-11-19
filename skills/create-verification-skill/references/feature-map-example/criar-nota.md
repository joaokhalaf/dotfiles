# Criar uma nota

Criar nota permite ao usuário salvar uma nota com título pelo browser ou pela CLI, cancelar um rascunho e confirmar a nota salva numa segunda visão.

## Subfeatures

- `criar-abrir` abre um editor vazio a partir de cada ponto de entrada do browser.
- `criar-salvar` persiste título e corpo.
- `criar-cancelar` descarta um rascunho não terminado no browser.
- `criar-cli` cria a mesma nota pelo terminal.

## Como chegar (visão do usuário)

- Clicar no botão `Nova nota` na barra do browser.
- Apertar `n` no browser com o foco fora de um campo editável.
- Rodar `notes create --title <título> --body <corpo>` num terminal.

## Dirigindo com control-notes

Pré-condições:

- Notas saudável em `http://127.0.0.1:4173`.
- Nenhuma nota com título `Checklist de release`.
- `control-notes doctor` informa a URL e o diretório de dados descartável esperados.

- **Abrir editor.** Clique em `Nova nota`. Rode `control-notes browser click --role button --name "Nova nota"`. Aparece um formulário `Editor de nota` com foco no campo `Título`.
- **Preencher.** Digite título e corpo. Rode `control-notes browser fill --role textbox --name "Título" --value "Checklist de release"` e `control-notes browser fill --role textbox --name "Corpo" --value "Criar tag e publicar"`. O botão `Salvar nota` fica habilitado.
- **Salvar.** Clique em `Salvar nota`. Rode `control-notes browser click --role button --name "Salvar nota"`. Aparece o status `Nota salva` e o título mostra `Checklist de release`.
- **Confirmar persistência.** Volte à lista e reabra a nota. Rode `control-notes browser click --role link --name "Todas as notas"` e `control-notes browser click --role link --name "Checklist de release"`. O editor mostra os dois valores salvos.
- **Cancelar rascunho.** Abra uma nota nova, digite `Descartar` e clique em `Cancelar`. A lista volta sem link `Descartar`.
- **Entrada pela CLI.** Rode `control-notes cli -- notes create --title "Nota CLI" --body "Criada no terminal" --format json`. Exit code `0` e stdout com o id e o título da nota.
- **Prova.** Reabra as duas notas a partir de `Todas as notas`. Rode `control-notes browser snapshot --aria --path artifacts/criar-nota/lista.aria.txt` e `control-notes browser screenshot --path artifacts/criar-nota/lista.png`. Os artefatos mostram `Checklist de release` e `Nota CLI`.

## Pegadinhas

- Apertar `n` com foco num campo de texto digita o caractere em vez de abrir o editor.
- Títulos são aparados ao salvar. Afirme o título renderizado, não o valor do rascunho.
- O status de salvo sozinho não é prova suficiente. Reabra a nota pela lista.
- Remova `Checklist de release` e `Nota CLI` no cleanup das fixtures, mas mantenha os artefatos de prova.
