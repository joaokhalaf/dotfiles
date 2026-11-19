---
name: tdd
description: Correção de bug com teste falhando primeiro. Use só quando o usuário pede TDD, um teste falhando ou um teste de regressão, ou quando o bug tem um alvo de teste local óbvio e barato. Não use quando o caminho de teste é incerto, caro, de integração pesada ou não pedido.
---

# TDD para correção de bug

Ao corrigir um bug com caminho de teste claro e barato, torne o comportamento quebrado executável antes de mudar o código de produção. O objetivo é um teste de regressão focado que falha antes da correção e passa depois.

Não force um teste impraticável. Se o teste exigiria harness amplo, mocks frágeis, infraestrutura end-to-end lenta, estado só de produção, reprodução vaga ou mudança grande de fixtures não relacionadas, não adicione teste novo e use a verificação útil mais próxima.

## Fluxo

1. **Entenda o bug.** Comportamento pretendido, comportamento atual, caminho afetado e a menor reprodução observável.
2. **Escolha o check executável mais estreito.** Prefira o teste unitário, de componente, integração ou regressão já usado naquele caminho. Sem caminho prático óbvio, não crie um do zero só para cumprir o fluxo.
3. **Escreva o teste falhando primeiro.** O menor teste focado que teria pegado o bug. Ele codifica o comportamento pretendido, não espelha a implementação atual (**principle-test-behavior-not-implementation**).
4. **Rode o teste novo antes de corrigir.** Confirme que falha pela razão pretendida. Se passa ou falha por outra razão, corrija o teste ou a reprodução antes de mexer na implementação.
5. **Corrija o bug.** A menor mudança de produção que satisfaz o comportamento pretendido, preservando contratos vizinhos.
6. **Rode o teste de novo.** Confirme que agora passa.

## Quando o teste falhando é impraticável

Use o check de regressão executável mais próximo: script direcionado, comando de reprodução manual, automação de browser, comparação de snapshot, asserção em log ou check de integração focado.

Prefira nenhum teste novo a um teste ruim. Teste ruim: testa principalmente mocks, codifica detalhes de implementação, depende de timing ou estado global não relacionado, exige infraestrutura cara para uma correção pequena, ou seria apagado logo depois de provar a correção.

## Limites

- Não mude testes só para combinar com uma implementação errada.
- Não enfraqueça asserções existentes, salvo quando o comportamento esperado mudou de fato e a razão é clara.
- Mantenha o teste focado no bug. Evite mexer em fixtures amplas ou expandir cobertura sem relação.
- Bug intermitente: torne o teste determinístico onde possível e registre o sinal que está sendo travado.
- Bug que revela uma classe maior de falhas: entregue primeiro a regressão focada, depois considere cobertura irmã.

## Resposta final

Reporte a evidência, não só o resultado:

- O teste ou check que falhou antes e a falha que produziu.
- A execução que passou depois e as validações vizinhas feitas.
- Se não foi possível demonstrar a falha antes, diga por quê e descreva o check de regressão usado no lugar.
