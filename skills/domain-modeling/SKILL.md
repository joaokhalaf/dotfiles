---
name: domain-modeling
description: Constrói e afia o modelo de domínio do projeto, mantendo GLOSSARY.md e ADRs em docs/adr/ em pt-BR. Use ao discutir terminologia do código, escrever ou editar GLOSSARY.md, ou registrar ou editar um ADR.
---

# Modelagem de domínio

Construa e afie ativamente o modelo de domínio do projeto enquanto projeta: questione termos, invente cenários de borda e escreva glossário e decisões no momento em que se cristalizam. Só *ler* o `GLOSSARY.md` para usar o vocabulário não é esta skill; ela é para quando o modelo muda.

Glossário e ADRs são sempre escritos em pt-BR. Identificadores do código citados ficam como estão.

## Estrutura de arquivos

A maioria dos repos tem um único contexto:

```
/
├── GLOSSARY.md
├── docs/
│   └── adr/
│       ├── 0001-pedidos-com-event-sourcing.md
│       └── 0002-postgres-no-modelo-de-escrita.md
└── src/
```

Se existe `GLOSSARY-MAP.md` na raiz, o repo tem vários contextos, e o mapa aponta onde cada um vive:

```
/
├── GLOSSARY-MAP.md
├── docs/adr/                         ← decisões do sistema todo
└── src/
    ├── pedidos/
    │   ├── GLOSSARY.md
    │   └── docs/adr/                 ← decisões do contexto
    └── cobranca/
        ├── GLOSSARY.md
        └── docs/adr/
```

Crie arquivos de forma preguiçosa: só quando houver algo para escrever. Sem `GLOSSARY.md`, crie no primeiro termo resolvido. Sem `docs/adr/`, crie no primeiro ADR.

## Durante a sessão

### Confronte com o glossário

Quando o usuário usa um termo que conflita com o `GLOSSARY.md`, aponte na hora: "O glossário define 'cancelamento' como X, mas você parece querer dizer Y. Qual é?"

### Afie linguagem vaga

Para termos vagos ou sobrecarregados, proponha um termo canônico preciso: "Você diz 'conta': é o Cliente ou o Usuário? São coisas diferentes."

### Discuta cenários concretos

Quando relações do domínio estão em discussão, teste-as com cenários específicos que sondam bordas e obrigam a precisão nas fronteiras entre conceitos.

### Cruze com o código

Quando o usuário afirma como algo funciona, confira se o código concorda. Contradição: traga à tona. "O código cancela Pedidos inteiros, mas você disse que cancelamento parcial é possível. Qual está certo?"

### Atualize o GLOSSARY.md na hora

Termo resolvido: atualize o `GLOSSARY.md` ali mesmo, sem acumular. Use o [formato do glossário](GLOSSARY-FORMAT.md).

O `GLOSSARY.md` não tem nenhum detalhe de implementação. Não é spec, rascunho nem depósito de decisões de implementação. É glossário e nada mais.

### Ofereça ADRs com parcimônia

Ofereça um ADR só quando as três condições valem:

1. **Difícil de reverter**: mudar de ideia depois tem custo relevante.
2. **Surpreendente sem contexto**: um leitor futuro vai perguntar "por que fizeram assim?"
3. **Resultado de um trade-off real**: havia alternativas genuínas e uma foi escolhida por razões específicas.

Faltou uma, pule o ADR. Use o [formato de ADR](ADR-FORMAT.md).
