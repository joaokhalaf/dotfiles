# Formato de ADR

ADRs ficam em `docs/adr/` com numeração sequencial: `0001-slug.md`, `0002-slug.md` etc. Slug em pt-BR, minúsculo, com hífens.

Crie `docs/adr/` só quando o primeiro ADR for necessário.

## Modelo

```md
# {Título curto da decisão}

{1-3 frases: o contexto, o que decidimos e por quê.}
```

Só isso. Um ADR pode ser um parágrafo. O valor está em registrar *que* uma decisão foi tomada e *por quê*, não em preencher seções.

## Seções opcionais

Só quando agregam valor real. A maioria dos ADRs não precisa.

- Frontmatter **Status** (`proposto | aceito | obsoleto | substituído pelo ADR-NNNN`): útil quando decisões são revisitadas.
- **Opções consideradas**: só quando vale lembrar as alternativas rejeitadas.
- **Consequências**: só quando efeitos posteriores não óbvios precisam ser ditos.

## Numeração

Procure o maior número existente em `docs/adr/` e some um.

## Quando oferecer um ADR

As três condições precisam valer:

1. **Difícil de reverter**: mudar de ideia depois tem custo relevante.
2. **Surpreendente sem contexto**: um leitor futuro vai olhar o código e perguntar "por que fizeram assim?"
3. **Resultado de um trade-off real**: havia alternativas genuínas e uma foi escolhida por razões específicas.

Fácil de reverter: pule, você só vai reverter. Não surpreende: ninguém vai perguntar. Sem alternativa real: não há o que registrar além de "fizemos o óbvio".

### O que se qualifica

- **Forma da arquitetura.** "Usamos monorepo." "O modelo de escrita é event-sourced; o de leitura é projetado no Postgres."
- **Padrões de integração entre contextos.** "Pedidos e Cobrança se comunicam por eventos de domínio, não HTTP síncrono."
- **Escolhas de tecnologia com lock-in.** Banco, barramento de mensagens, provedor de auth, alvo de deploy. Não toda biblioteca: só as que levariam um trimestre para trocar.
- **Decisões de fronteira e escopo.** "Dados de cliente pertencem ao contexto Cliente; os outros referenciam só por ID." Os "não" explícitos valem tanto quanto os "sim".
- **Desvios deliberados do caminho óbvio.** "SQL manual em vez de ORM por causa de X." Tudo em que um leitor razoável assumiria o contrário. Isso impede o próximo engenheiro de "consertar" algo deliberado.
- **Restrições invisíveis no código.** "Não podemos usar AWS por compliance." "Respostas abaixo de 200 ms por contrato com a API parceira."
- **Alternativas rejeitadas quando a rejeição não é óbvia.** Se GraphQL foi considerado e REST escolhido por razões sutis, registre; senão alguém vai sugerir GraphQL de novo em seis meses.
