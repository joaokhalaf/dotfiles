### Forense de trace

**Você é dono do diagnóstico a partir do artefato.**

Diferente de Runtime forensics, que instrumenta o processo vivo: aqui a captura já existe. O artefato é um dataset fixo; leia, não reexecute. Ferramentas genéricas: parser DevTools para cpuprofile e `.json.gz`, editor de texto para spindump, ferramenta de heap para heapsnapshot.

1. Identifique o formato e carregue com a ferramenta certa. Artefato grande num subagente (**principle-guard-the-context-window**); o achado reduzido fica no main.
2. Transforme o artefato em algo consultável: trace ou heap snapshot para sqlite, uma linha por amostra, frame ou nó.
3. Estreite até a causa. Consulte os frames com mais tempo e desça a árvore até o caminho quente. Para leak, siga a cadeia de retenção até a raiz do GC. Para spindump, ache a thread presa e o motivo da espera.
4. Atribua ao código pelos símbolos do próprio artefato. Frame sem mapeamento ainda não é diagnóstico: resolva os símbolos ou diga que o artefato não os carrega.
5. Com captura pareada, compare antes e depois para confirmar. Sem ela, marque como a hipótese mais forte que o artefato sustenta.
6. Entregue diagnóstico citado, sem correção salvo pedido. Checkpoint: `throughput: n/a, forense somente leitura`.

**Resposta:** artefato e formato, achado reduzido, local no código, caminhos, e se uma captura pareada confirmou.
