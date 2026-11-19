---
name: grilling
description: Entrevista o usuário sem trégua sobre um plano, decisão ou ideia até chegar a um entendimento comum, em rodadas de perguntas numeradas com resposta recomendada. Use quando o usuário quer testar o próprio raciocínio, diz "grill", "me questiona", "me sabatina", ou quando o poteto-mode abre uma tarefa.
---

# Grilling

Entreviste o usuário sem trégua até chegar a um entendimento comum. Mapeie como uma *árvore de decisões*: cada decisão se ramifica nas decisões que dependem dela.

Trabalhe a árvore em *rodadas*. A *fronteira* é toda decisão cujos pré-requisitos já estão resolvidos: as perguntas que você pode fazer *agora* sem chutar respostas que ainda não ouviu. Pergunte a fronteira inteira numa rodada: numere cada pergunta e dê sua resposta recomendada. Espere as respostas antes da próxima rodada.

Formato de uma rodada:

```
**P1. <título da pergunta>**: <corpo, pode ter vários parágrafos e alternativas>

→ <sua resposta recomendada>

---

**P2. <título da pergunta>**: <corpo>

→ <sua resposta recomendada>
```

Formule cada pergunta para que "sim" aceite a recomendação. "Sim para todas" aceita a rodada inteira.

Cada rodada respondida remodela a árvore: decisões resolvidas empurram a fronteira e destravam as que dependiam delas. Recalcule a fronteira e faça a próxima rodada. Pergunta cuja resposta depende de outra ainda aberta nesta rodada vai para uma rodada *posterior*.

Descobrir *fatos* é trabalho seu, nunca do usuário. Quando uma pergunta precisa de um fato do ambiente (arquivos, código, histórico, ferramentas), descubra você mesmo; se for volumoso, mande um subagente com contexto novo. Não bloqueie por isso: uma exploração em andamento é um pré-requisito não resolvido, então só as perguntas que dependem dela esperam; faça o resto da fronteira agora. As *decisões* são do usuário: apresente cada uma e espere.

Pedido claro tem fronteira pequena: uma rodada curta confirmando objetivo, escopo e critério de pronto basta. Não invente perguntas para encher a rodada.

A sessão termina quando a fronteira esvazia: todo ramo visitado, nada assumido em silêncio. Feche com um resumo das decisões tomadas e não aja antes de o usuário confirmar o entendimento comum.

Subagentes e execuções sem humano (worker do **poteto-mode**) não fazem grilling.
