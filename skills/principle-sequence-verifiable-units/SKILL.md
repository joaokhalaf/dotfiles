---
name: principle-sequence-verifiable-units
description: "Aplique a trabalho em vários passos (varreduras, migrações, séries de edições parecidas) e a como empilhar commits e PRs. Quebre em unidades pequenas que terminam num estado verificável, confira cada uma antes da próxima e ordene a entrega para a sequência se provar ao revisor."
disable-model-invocation: true
---

# Sequence work into verifiable units

Ordene o trabalho em unidades pequenas que terminam num estado verificável, e não avance até a atual estar verde.

Numa varredura, migração ou série de edições parecidas, cada unidade é um colchete: estado bom conhecido, uma mudança, rode o check, prossiga. Rode o check por unidade mesmo quando uma ferramenta faz as edições.

Entregue na ordem que prova o trabalho: o teste falhando primeiro, depois a correção. A subtração antes do reshape. O baseline antes do tratamento. Cada commit se sustenta sozinho.
