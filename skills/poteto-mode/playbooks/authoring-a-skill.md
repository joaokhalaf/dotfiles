### Escrevendo ou modificando uma skill

**Você é dono da voz da skill.**

1. Edite as fontes em `~/work/home-dev-setup/skills/`, nunca cópias instaladas ou cache de plugin. No Claude Code, a skill `skill-creator` ajuda em estrutura e evals.
2. Valide: frontmatter com `name` e `description`, `disable-model-invocation` decidido, arquivos referenciados existem, links entre skills resolvem (`python3 scripts/check_skills.py`, quando existir).
3. Casos de teste se for estrutural; pule se for subjetivo. Mudança de comportamento relevante → [eval](eval.md).
4. Commit na factory. PR só se pedido.

Na dúvida, delete. Mantenha só prosa que muda uma decisão. Diga para fazer a coisa e pule o motivo; explique só quando a regra confunde sem ele. Tom proporcional ao escopo. Aponte para fontes estruturais (tipos, READMEs, config) segundo **principle-encode-lessons-in-structure**. Delegue a outras skills por caminho; não repita. Fluxo recorrente não capturado → proponha uma skill nova.

**Resposta:** resumo da skill, decisões de design, notas de validação.
