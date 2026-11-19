---
name: why
description: Responde "por que X funciona assim?", "por que escolhemos Y?", motivação de design, origem de regressões, postmortems e limites definidos por dados, a partir do histórico (commits, PRs, issues), com citações. Use para perguntas de motivação e histórico, não de comportamento em runtime.
---

# Why

Responda pelo registro, não pelo código: leia os commits e discussões de PR que introduziram o alvo e cada mudança posterior (`git log --follow -p`, `git blame`, `gh pr view`, `gh issue view`), e outras fontes se a trilha for fraca. Cite o que os autores escreveram, marque suas inferências como inferências e diga o que o registro não responde.

Para "como isto funciona em runtime", use o playbook investigation do **poteto-mode**.
