---
name: dev-verify
description: Valide uma mudança no comportamento observável e reporte evidências e limitações reais.
---

# Verificação

Encontre os scripts e instruções existentes do projeto. Escolha checks adequados
ao risco: teste direcionado, tipos/lint quando relevantes e execução da superfície
alterada. Não crie testes triviais que apenas espelhem a implementação.

Para app web local, inicie o servidor e use o driver existente do projeto. Se usar local-browser, use o nome do workspace
como session. Navegue no fluxo afetado e examine erros de runtime. Sem esse MCP, use o CLI local-browser quando instalado ou outro driver de browser disponível; não declare teste
visual realizado sem executar o navegador. Para CLI/TUI, rode o caminho real em
terminal; para biblioteca, use teste de contrato ou chamador representativo.

Em bug, compare reprodução antes/depois quando possível. Verifique erros relevantes,
não apenas o caminho feliz. Não execute operações destrutivas nem use produção
como fixture sem autorização. Registre comandos e resultados; diferencie aprovado,
reprovado e não executado. Encerre os servidores temporários que você iniciou.
