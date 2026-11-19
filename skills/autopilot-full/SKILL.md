---
name: autopilot-full
description: Conduza os PRs explicitamente autorizados até merge, com revisão e gates no head atual.
---

# Autopilot full

Antes do merge, confira também os gates e pendências definidos em
[security-review](../security-review/SKILL.md) para o head atual. Não ignore bloqueios
de segurança para concluir a automação.

Leia autopilot-stack e execute seus gates. Exija instrução explícita autorizando
merge e identificando os cards/PRs abrangidos. A mera instalação desta skill ou
pedido de configurar a factory não autoriza merge. O padrão continua stack.

Antes de cada merge confirme SHA remoto igual ao revisado, base correta, checks
atuais verdes, ausência de conflitos e aprovações exigidas pelo forge. Nunca use
admin/bypass ou enfraqueça gates. Mudança no head exige nova verificação; mudança
na base exige avaliar e testar o resultado que será integrado. Restack dependentes
e revalide após merge do pai. Faça merge pelo forge com comparação do SHA esperado.

Pare em rejeição humana, conflito não resolvido, limite de tentativas/consumo ou
instrução de stop. Registre SHA integrado, evidências e links. A CLI inicial não
faz merge automático; este fluxo é executado pelo coordenador com ferramentas
GitHub disponíveis e a autorização descrita acima.

## Executor e coordenação

Leia [o contrato local](../poteto-mode/references/runtime.md) antes de executar.
