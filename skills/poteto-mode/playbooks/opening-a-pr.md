### Abrindo um PR

Invocado ao fim dos outros playbooks, só quando o usuário pediu PR.

Trabalhe numa worktree a partir do trunk, sem trabalho não relacionado. Rebase em commits pequenos e integráveis. Antes do commit, **no-comments** no diff e **unslop** na prosa.

Título: `type(scope): subject`, nomeando um símbolo real quando um carrega a mudança. Corpo: briefing de um minuto, menos de 40 linhas, com estes `##` em ordem, omitindo vazios: `## Why`, `## What changed`, `## Scope`, `## Tradeoffs` (só alternativas rejeitadas que um revisor perguntaria), `## Blast Radius`, `## Verification`. Inclua o resultado de **security-review** quando aplicável. Use a língua do repositório.

Empilhe follow-ups pela branch base. Abra PRs prontos com `gh pr create` sem `--draft`. Abrir um PR não inicia babysit. No T3, vincule o PR à thread.
