# Formato do GLOSSARY.md

## Estrutura

```md
# {Nome do contexto}

{Uma ou duas frases sobre o que é este contexto e por que existe.}

## Linguagem

**Pedido**:
{Uma ou duas frases descrevendo o termo.}
_Evitar_: compra, transação

**Fatura**:
Pedido de pagamento enviado ao cliente depois da entrega.
_Evitar_: conta, cobrança

**Cliente**:
Pessoa ou organização que faz pedidos.
_Evitar_: comprador, usuário, conta
```

## Regras

- **Tenha opinião.** Quando várias palavras existem para o mesmo conceito, escolha a melhor e liste as outras em `_Evitar_`.
- **Definições curtas.** No máximo uma ou duas frases. Defina o que a coisa É, não o que faz.
- **Só termos específicos deste contexto.** Conceitos gerais de programação (timeouts, tipos de erro, utilitários) ficam de fora, mesmo que o projeto os use muito. Antes de adicionar, pergunte: é um conceito único deste contexto ou geral de programação? Só o primeiro entra.
- **Agrupe termos em subtítulos** quando surgirem grupos naturais. Se todos pertencem a uma área coesa, lista plana basta.

## Um contexto ou vários

**Um contexto (a maioria):** um `GLOSSARY.md` na raiz.

**Vários contextos:** um `GLOSSARY-MAP.md` na raiz lista os contextos, onde vivem e como se relacionam:

```md
# Mapa de glossários

## Contextos

- [Pedidos](./src/pedidos/GLOSSARY.md): recebe e acompanha pedidos de clientes
- [Cobrança](./src/cobranca/GLOSSARY.md): gera faturas e processa pagamentos
- [Expedição](./src/expedicao/GLOSSARY.md): separação no armazém e envio

## Relações

- **Pedidos → Expedição**: Pedidos emite eventos `OrderPlaced`; Expedição os consome para iniciar a separação.
- **Expedição → Cobrança**: Expedição emite `ShipmentDispatched`; Cobrança os consome para gerar faturas.
- **Pedidos ↔ Cobrança**: tipos compartilhados `CustomerId` e `Money`.
```

Como inferir a estrutura:

- Existe `GLOSSARY-MAP.md`: leia para achar os contextos.
- Existe só um `GLOSSARY.md` na raiz: um contexto.
- Nenhum dos dois: crie o `GLOSSARY.md` na raiz quando o primeiro termo se resolver.

Com vários contextos, infira a qual o tema atual pertence. Se não estiver claro, pergunte.
