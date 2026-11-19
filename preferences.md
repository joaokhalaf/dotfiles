# Preferências da factory

## Confirmadas

- Entrada principal: conversar com o main no chat, como nesta sessão.
- O modelo decide o próximo passo usando poteto-mode e skills situacionais.
- Subagentes são opcionais; usar por benefício concreto, sem um agente por etapa.
- Codex em casa; Claude Code no trabalho. Terminal/Herdr/Desktop são superfícies
  possíveis conforme as ferramentas reais. Herdr não é requisito do produto.
- Sem dependências exclusivas do Cursor; preservar ferramentas e regras da sessão.
- APIs, tipos e checks devem reduzir decisões ambíguas; texto só quando necessário.
- Testar a factory nela mesma, observar problemas e adaptar com evidência.

## Aplicação

Chat: herdar modelo e configurações; trabalho direto por padrão quando adequado.
Usar persistência em Markdown para tarefas longas/pausas. PR e merge dependem do
pedido; a instalação das skills não os autoriza. Revisão humana antes de merge
é o padrão de entrega de PRs.

Runner: ferramenta auxiliar de terminal, escolhida explicitamente. Perfis home/work,
JSON, duas tentativas, seis chamadas e demais limites valem apenas nele. Seus logs
e worktrees antigos são preservados; não retomar a rodada esports sem pedido.

## Qualidade solicitada

- Proibir novas ocorrências de useEffect; não substituir por escapes equivalentes.
- Remover quase todos os comentários explicativos; obrigações externas preservadas.
- Criar APIs de domínio que escondam complexidade e checks que rejeitem caminhos errados.
- Skills no-comments e create-verification-skill adaptadas ao executor disponível.
- Enforcement em cada app deve ser implementado e demonstrado; instrução não é lint.
