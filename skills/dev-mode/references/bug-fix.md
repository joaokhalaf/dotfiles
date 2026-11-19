# Correção de bug

1. Identifique comportamento esperado e observado. Reproduza na superfície afetada.
   Se não conseguir, registre a limitação e instrumente o caminho possível; não
   apresente uma hipótese como causa confirmada.
2. Formule hipóteses e elimine-as com execução, logs, testes ou histórico relevante.
   Corrija a causa demonstrada com a menor mudança suficiente.
3. Quando houver teste local barato, escreva uma regressão que falhe pelo defeito
   antes de corrigir. Evite mocks frágeis e infraestrutura desproporcional.
4. Se a correção alterar contratos entre módulos, defina o formato e os chamadores
   antes da implementação. Não faça redesenhos sem relação com o defeito.
5. Repita a reprodução original e rode os checks relevantes. Remova instrumentação
   temporária. Relate evidência antes/depois ou a impossibilidade de obtê-la.
