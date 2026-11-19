---
name: dev-verify
description: Prova uma mudança na superfície real (browser, terminal, API ou chamador de biblioteca) e reporta evidência e limitações. Use para validar uma mudança, "testa isso no browser", "roda e confere", reproduzir um bug na UI/CLI, ou quando um playbook pede verificação na superfície.
---

# Verificação na superfície real

Prove o comportamento no artefato real, não num proxy (**principle-prove-it-works**). Compilação, tipos e lint não provam comportamento.

## Escolher o driver

1. **Skill de verificação do projeto.** Se existe `.claude/skills/verify-*/` (ou outra citada no AGENTS.md do projeto), siga o launch, doctor, drive, evidence e cleanup dela e o mapa de features. Ela vence qualquer receita genérica.
2. **Sem skill do projeto**, use o harness que o repo já tem (Playwright, specs, scripts de teste) e, na falta, o genérico:
   - Web local: MCP `local-browser` com `session` igual ao nome do workspace; fallback CLI `local-browser --task <workspace>`.
   - CLI/TUI: o binário real num terminal; PTY ou tmux quando há interação.
   - API: requisições reais contra o servidor local.
   - Biblioteca: chamador público ou teste de contrato.
3. Projeto sem jeito scriptado de verificar e trabalho recorrente: proponha **create-verification-skill**.

## Executar

- Leia scripts e instruções do projeto. Escolha checks proporcionais ao risco: teste direcionado, tipos e lint quando relevantes, e a superfície alterada.
- Suba o app você mesmo, em portas e diretórios de dados isolados. Nunca dirija a sessão do usuário nem use produção como fixture. Pronto significa utilizável, não só um processo respondendo.
- Exercite o caminho real do usuário, não setters internos nem endpoints só de teste. Inclua os erros relevantes, não só o caminho feliz.
- Em bug, compare reprodução antes e depois na mesma superfície.
- Dry-run ou modo de teste: confirme pelo que observa (arquivos, rede, refs git) o que ele realmente pula.
- Não crie testes triviais que só espelham a implementação (**principle-test-behavior-not-implementation**).

## Evidência

- A ação e o estado resultante, não só a tela final: screenshot, snapshot de acessibilidade, transcrição de terminal com comando, saída e exit code, corpo de resposta.
- Efeitos colaterais além do visível: arquivos escritos, linhas no banco, mensagens enviadas.
- Artefatos num local nomeado que sobrevive ao cleanup.

## Cleanup e relatório

Encerre só os processos e recursos que você iniciou; nunca mate por nome nem apague dados do usuário. Reporte comandos e resultados distinguindo aprovado, reprovado e não executado, com os caminhos da evidência. "Inconclusivo" ou superfície errada não é aprovação. Não declare teste visual feito sem ter rodado o navegador.
