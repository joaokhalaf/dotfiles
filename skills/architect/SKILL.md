---
name: architect
description: Defina tipos, interfaces, operações de domínio e propriedade do estado antes da implementação.
---

# Architect

Leia a [política de qualidade](../poteto-mode/references/quality.md).
Projete APIs e checks que removam decisões ambíguas dos chamadores.

Trace o fluxo e mostre o uso pelo chamador antes das interfaces internas. Escolha
um dono para cada estado e uma operação de domínio para cada ação. Prefira
containerService.close({containerId, sealNumber, sealPhotoId, actor}) a espalhar
updates que cada chamador precisa validar. Centralize permissões, transições,
pedidos pendentes e auditoria na fronteira dessa operação.

Expresse estados válidos com tipos; torne internals inacessíveis por exports e
regras de importação. Compare alternativas apenas onde há decisão real. Nomeie
como o contrato será verificado. Evite abstrações genéricas que apenas escondem
a mesma ambiguidade. Use bibliotecas e convenções já adotadas pelo projeto.

## Executor e coordenação

Leia [o contrato local](../poteto-mode/references/runtime.md) antes de executar.
