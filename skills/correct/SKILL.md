---
name: correct
description: Transforme erros recorrentes demonstrados em APIs, tipos, lint e checks que evitem sua repetição.
---

# Correct

Encontre classes de erros no histórico de correções, reverts, reviews e execuções.
Use evidências do projeto; não invente recorrência. Prefira, nesta ordem:
1. API de domínio ou arquitetura que elimine o caminho errado.
2. Tipos/exports que impeçam estado ou acesso inválido.
3. Lint/CI com mensagem indicando o caminho correto.
4. Teste de comportamento que falhe pelo erro.
5. Documentação para decisões que ainda exigem julgamento.

Prove que o novo gate rejeita o caso errado e aceita o correto; rode o mesmo
comando usado na CI. Não relaxe um gate para conseguir verde.

Aplique a [política de qualidade](../poteto-mode/references/quality.md): banir novas
ocorrências de useEffect com AST lint no projeto React; oferecer operações de
domínio e alternativas existentes; eliminar comentários explicativos via
[no-comments](../no-comments/SKILL.md). Não abra exceções automaticamente nem
reescreva legado fora do escopo. As regras e seus checks precisam concordar.

Mantenha uma tabela regra → enforcement → comando → evidência no projeto.
Mude o escopo necessário ao problema; sem commits ou PRs fora da autorização.

## Executor e coordenação

Leia [o contrato local](../poteto-mode/references/runtime.md) antes de executar.
