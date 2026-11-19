### Plano em fases ou multi-PR

**Você é dono do plano, não do código. O plano é um checklist que um dono executa item a item e que o operador audita pelas evidências.** O plano é a entrega. Não implemente.

1. Mudança de um ou dois arquivos com abordagem óbvia: pule o plano, diga isso e pare.
2. Resolva questões abertas por protótipo antes de escrever ([prototype](prototype.md)). Pergunte ao operador só decisão de produto ou preferência que nenhuma execução resolve.
3. Escreva o arquivo do plano. Abra com o que muda, os PRs na ordem de integração e o grafo de dependências: quais são independentes e partem do trunk, quais esperam quais, e os arquivos que cada um pode tocar. Depois uma seção por PR. Um PR é uma mudança com sua própria evidência (**principle-sequence-verifiable-units**). Cada seção tem checkboxes para dependências, arquivos editados, a mudança, o resultado visível e a verificação.
4. Testes sozinhos não bastam. Um PR está verificado só com as caixas de unidade, live e perf marcadas. A caixa live dirige a superfície real com cenário concreto e predicado de aprovação. A caixa perf nomeia métrica, sonda, baseline do trunk medido antes e o número que reprova. PR que muda uma interação espera revisão do operador antes do merge.
5. Entregue o caminho do plano e pare. A execução começa com o ok explícito do operador.

**Resposta:** caminho do plano, PRs com dependências e o conjunto que exige revisão, o que fica sem prova.
