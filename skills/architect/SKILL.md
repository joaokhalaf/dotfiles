---
name: architect
description: Esboça tipos, assinaturas e estrutura de módulos antes do código e acompanha enquanto a implementação preenche. Use para /architect, "projeta isso", ou trabalho não trivial em que ir direto ao código fixaria o formato errado.
disable-model-invocation: true
---

# Architect

Antes de escrever código, rastreie todo sistema que a mudança toca: chamadores, tipos, fluxo de dados, quem é dono de cada estado. Depois esboce **dois formatos diferentes** (tipos, assinaturas, fronteiras de módulo) e escolha aquele em que cada estado tem um dono, cada tarefa tem um jeito de ser feita e o chamador precisa saber o mínimo. Se workarounds se repetem, redesenhe em vez de remendar.

- Mostre primeiro como o chamador usa a mudança; depois as interfaces internas.
- Uma operação de domínio por ação. Prefira `containerService.close({containerId, sealNumber, sealPhotoId, actor})` a espalhar updates que cada chamador precisa validar. Permissões, transições, pendências e auditoria ficam na fronteira dessa operação.
- Estados válidos expressos em tipos; internos inacessíveis por exports e regras de importação; dados externos validados na fronteira (**principle-type-system-discipline**, **principle-boundary-discipline**).
- Compare alternativas só onde há decisão real. Evite camadas e wrappers que só deslocam a mesma ambiguidade. Use as bibliotecas e convenções do projeto.
- Nomeie como o contrato será verificado.
- Aplique a [política de qualidade](../poteto-mode/references/quality.md).

Design grande ou contestado: use **arena** em vez de esboçar sozinho. Pedido só de desenho: entregue a proposta antes de implementar.
