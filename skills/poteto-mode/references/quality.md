# Qualidade por estrutura e checks

Preferência explícita do usuário para o código produzido pela factory: reduzir
decisões ambíguas por meio de APIs e verificações automáticas. Não basta escrever
uma instrução e assumir que ela será obedecida.

## React: sem useEffect

Não introduza useEffect, React.useEffect, aliases ou reexports que contornem a
proibição. Não substitua mecanicamente por useLayoutEffect ou outro hook apenas
para esconder o mesmo efeito. Derive valores no render; trate ações em handlers;
use loaders/query/cache já adotados para dados e APIs próprias para subscriptions.
Se houver integração externa que realmente precise de um efeito, exponha essa
necessidade como decisão pendente, sem abrir uma exceção por conta própria.

Ao configurar enforcement em um projeto React, prefira regra AST de lint que
rejeite imports, aliases e acessos ao hook e aponte a alternativa do projeto.
Prove com um caso proibido e um permitido e rode a mesma regra na CI. Não use
regex como prova de cobertura semântica. Código legado fora do escopo não é
permissão para uma migração ampla: não acrescente ocorrências; registre as antigas.
Se não há React no projeto, a regra não exige instalar ferramentas de React.

## Comentários explicativos: quase nenhum

O padrão é código sem comentários explicativos. Não narre o código, não justifique
workarounds e não use comentários para transferir ao próximo agente uma regra
que API, tipo ou teste pode impor. Use [no-comments](../../no-comments/SKILL.md)
no diff relevante. “99%” indica esse rigor; não é meta contábil para apagar texto.
Preserve licenças/avisos obrigatórios e diretivas necessárias às ferramentas;
diretivas de supressão não viram exceção para esconder defeitos. Uma restrição
externa irredutível pode precisar de explicação curta, com fonte e razão concreta.

## APIs que escondem complexidade

Ofereça operações de domínio em vez de permitir que cada agente monte updates e
validações. Uma operação close centraliza permissão, transição, pendências e
auditoria; o chamador fornece os dados necessários. Tipos e exports devem limitar
acesso direto às estruturas internas. A operação deve ser idempotente quando o
domínio exigir, não uma abstração genérica que apenas desloca condicionais.

Ordem preferida: API/arquitetura → tipos/exports → lint/CI → testes de comportamento
→ instruções para o que ainda exige julgamento. Para cada restrição implementada
registre regra, mecanismo, comando e evidência de rejeição/aceitação. Não afrouxe
gates para passar. Ao adicionar estas skills à factory, não alegue que o lint já
foi instalado nos aplicativos; esse enforcement depende de mudança no projeto.

Se falta um procedimento reproduzível para provar o comportamento real, use
[create-verification-skill](../../create-verification-skill/SKILL.md). Uma skill
é orientação; os comandos e provas do projeto são o enforcement observável.
