### Bug fix

**Você é dono desta tarefa. Planeje, revise, verifique.** Delegue investigação ou correção quando houver benefício (ver Subagentes); fique na liderança.

Seja científico. Cada linha entregue tem origem em evidência de runtime. Cinto-e-suspensório que "pode ajudar" é hipótese, não correção, e não entra. Quando a evidência refuta uma hipótese, reverta o que ela motivou. Entra a menor mudança que a evidência justifica.

1. Reproduza você mesmo na superfície correspondente via **dev-verify**, mesmo quando um protocolo de debug manda pedir ao usuário. Peça ao usuário só com razão específica de que a superfície não alcança o alvo, e só depois de ir até onde ela vai. Se não reproduzir direto, sintetize o gatilho, aperte as condições ou instrumente até disparar.
2. Busca binária da causa. Forme as hipóteses candidatas e elimine até sobrar uma. Alimente-as com um trace do subsistema e a skill **why** para histórico de regressão. Em cada passo, escolha o corte que elimina mais espaço, obtenha evidência de runtime, elimine. Estado do programa obscuro: instrumente e leia enquanto roda. Não chute. Confirme o *mecanismo* sobrevivente com evidência antes do `architect` ou de um `interrogate`.
3. Planeje a correção. Atravessa fronteira de função → `architect` antes. Delegue a implementação com escopo específico quando isso trouxer benefício.
4. Verifique na mesma superfície. A reprodução original agora passa. "Inconclusivo" ou superfície errada não é aprovação; sinalize. Teste unitário mostra comportamento de ramo, não ausência do bug.
5. Ordene os commits para a reprodução falhando entrar antes da correção no histórico. Veja **tdd** para o ritmo teste-falhando-primeiro quando houver caminho local barato; pule quando o teste for caro, integração pesada ou incerto. Este é o caso canônico de **principle-sequence-verifiable-units**.
6. PR só se pedido: **Opening a PR**.

**Resposta:** o que estava quebrado, causa raiz, correção, como verificou. Cole a saída da reprodução falhando e depois passando, literal.
