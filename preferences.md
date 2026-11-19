# Preferências

## Confirmadas

- Entrada principal: conversar com o main no chat.
- Funciona igual em Claude Code, Codex e OpenCode. Nenhum provider é o padrão;
  regras e skills se adaptam ao que estiver em uso. Diferenças entre eles ficam
  em `skills/poteto-mode/references/harness.md`, nunca espalhadas pelas skills.
- Terminal, Herdr, T3 Code e Desktop são superfícies possíveis conforme as
  ferramentas reais. Herdr só é exigido dentro do Herdr.
- Sem dependências exclusivas do Cursor; preservar ferramentas e regras da sessão.
- Em engenharia, o poteto-mode está sempre ativo e começa pelo grilling. Glossário
  e ADRs sempre em pt-BR.
- Subagentes por benefício concreto, herdando o modelo da sessão.
- APIs, tipos e checks devem reduzir decisões ambíguas; texto só quando necessário.
- Testar as práticas neste próprio repo, observar problemas e adaptar com evidência.

## Aplicação

Chat: herdar modelo e configurações; trabalho direto por padrão quando adequado.
Push, PR e respostas a review só com pedido. Merge só com autorização nomeando os
PRs. Revisão humana antes de merge é o padrão.

Sem runner nem fila: as boas práticas entram pelas instruções globais e pelas
skills, no começo de cada trabalho. Nada precisa ser executado à parte.

## Qualidade solicitada

- Proibir novas ocorrências de useEffect; não substituir por escapes equivalentes.
- Remover quase todos os comentários explicativos; obrigações externas preservadas.
- Criar APIs de domínio que escondam complexidade e checks que rejeitem caminhos errados.
- Enforcement em cada app deve ser implementado e demonstrado; instrução não é lint.
