# Origem

Cloudflare security-audit-skill:
https://github.com/cloudflare/security-audit-skill
Commit fixado: c1c8a8c1471069fb0e188eeaff69b8e8db6564a8, consultado em 2026-11-17.
Os 20 arquivos de skills/security-audit foram importados sem alterações, com MIT
upstream em skills/security-audit/LICENSE. security-review e sua política por
projeto são integração local; não substituem os requisitos da auditoria upstream.
Atualizações são manuais, revisando também scripts antes de executá-los.

Base: https://github.com/cursor/plugins/tree/main/pstack
Commit consultado: e1cc03121a0e71129a4fb730d7c5528a0a3e43c8, em 2026-11-17.
MIT de Lauren Tan preservada em LICENSE.

Adaptações locais de poteto-mode, architect, swarm, interrogate, autopilot-stack,
autopilot-full, correct, reflect e princípios de reprodução/verificação. São versões
condensadas e reescritas para Codex/Claude Code/Herdr, não o pacote upstream integral.
O runner SQLite, seus testes e o instalador são locais.

Removidos: Cursor Automations/Benny, cloud agents, Bugbot, /loop, cursor-team-kit,
control-ui/control-cli e slugs fixos de outros provedores. Substituições: worktrees
locais, ferramentas reais do executor, local-browser e verificações do projeto.

Mudanças deliberadas: stack como padrão, merge somente autorizado; concorrência,
tentativas e chamadas limitadas; sem fallback silencioso de modelo; avaliações
vinculadas ao SHA; evolução estrutural antes de aumentar instruções. Runner não faz
push/PR/merge; entrega local ao coordenador, que verifica o forge antes do handoff.
Não há atualização automática de upstream. Revisar manualmente futuras importações.

Providers Codex e Claude são adapters locais independentes das skills. Perfil home
usa Codex; work usa Claude. Nenhuma dependência de login Claude no perfil home.

Adaptações de qualidade consultadas em 2026-11-17:
- https://github.com/cursor/plugins/tree/main/pstack/skills/no-comments
- https://github.com/cursor/plugins/tree/main/pstack/skills/create-verification-skill

Versões locais condensadas: sem Comment Sicko obrigatório, APIs Task ou diretório
.cursor. Geração usa o driver e a pasta de skills do projeto e exige prova real.
Licença upstream continua preservada em LICENSE.

## poteto-mode completo (2026-11-19)

Fonte: https://github.com/cursor/plugins/tree/main/pstack/skills/poteto-mode,
commit 0b46ec399d55f2829e88822998f53b84944837d3.
SKILL.md, worker.md e os 22 playbooks traduzidos para pt-BR e adaptados. Mudanças
deliberadas: autonomia sem push/PR/merge implícitos; subagentes por benefício e
herdando o modelo; cursor-team-kit trocado por no-comments/unslop e dev-verify;
Origin, Graphite, Bugbot e cloud agents removidos; references/harness.md mapeia
Claude Code, Codex, OpenCode e T3. scripts/worktree-audit.sh portado para
transcrições do Claude Code e do Codex. watch-pr não foi portado (gh/T3 cobrem).
Os 24 skills principle-* do mesmo commit foram traduzidos para pt-BR. Nos que
tinham a regra só na description, ela foi trazida para o corpo. Adaptados:
never-block-on-the-human segue a autonomia local (push/PR só com pedido);
guard-the-context-window e type-system-discipline ganharam os itens que o upstream
só citava na description; typescript-best-practices não foi referenciado.
Skills de apoio do mesmo commit, traduzidas e adaptadas: technical-writing, why,
tdd, benchmark-checklist e unslop (model-invocable, pt-BR + inglês); arena,
show-me-your-work (log.sh e template copiados sem alteração) e figure-it-out
(só invocação). arena e a revisão do show-me-your-work usam outro provider via T3
quando disponível, senão contexto novo do mesmo modelo, declarado.

## grilling (2026-11-19)

Fonte: https://github.com/mattpocock/skills, commit
abeeaf95660ba9e8b7c753eb38f441ca707a8823, MIT (Matt Pocock). grilling, grill-me,
grill-with-docs e domain-modeling (com GLOSSARY-FORMAT e ADR-FORMAT) traduzidos
para pt-BR; glossário e ADRs sempre em pt-BR. grilling vira o primeiro passo do
poteto-mode. agents/openai.yaml (allow_implicit_invocation: false) é gerado por
scripts/check_skills.py --fix para toda skill com disable-model-invocation.

## Skills de método (2026-11-19)

Do commit 0b46ec3 do pstack: architect (fundido com dev-architect), swarm,
interrogate (fundido com dev-review como modo leve), no-comments (Comment Sicko
como references/comment-sicko.md lido por subagente, sem agente customizado),
correct, reflect (edita as fontes da factory), create-verification-skill (exemplo de
mapa reduzido a uma feature, em pt-BR) e maintain-verification-skill. autopilot-stack
e autopilot-full viraram atalhos para os playbooks do poteto-mode.
