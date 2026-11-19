### Protótipo

**Você é dono da decisão de design, não do código. O protótipo é um instrumento descartável. A construção real segue Feature.**

O único playbook em que "menor mudança" e a barra de verificação se invertem. Velocidade acima de polimento, sem planejamento. O rigor está em escolher o design certo barato. Proponha variações que o usuário não pediu; jogue uma abordagem fora e tente outra.

1. Delimite a decisão que o protótipo existe para tomar: layout, interação, densidade ou, numa bifurcação empírica, comportamento, timing ou abordagem. Sem decisão, sem protótipo: rote para Feature.
2. Reúna referências quando o espaço de design está aberto (prior art, temas, paletas, layouts) e deixe o usuário escolher direções antes de construir. Pule quando a direção já está dada.
3. Construa descartável num diretório scratch isolado, fora do código de produção. Para decisão visual, HTML/CSS/JS puro ou a stack mais leve, deps via CDN, servidor com reload. Para decisão de comportamento ou timing, o menor script que exercita a questão. Sem framework de produção, testes ou abstrações.
4. Comparando alternativas, coloque-as atrás de um seletor (botões ou tecla), cada variante rotulada (**principle-exhaust-the-design-space**).
5. Verifique na superfície. Visual: screenshot de cada variante via **dev-verify** e dirija a interação. Comportamento ou timing: observe registrando timing, imprimindo saída ou olhando o render. A observação é o teste.
6. Apresente alternativas, trade-offs e recomendação. A saída é a decisão mais o artefato descartável. Passe a direção escolhida para **Feature** (ou `architect`).

**Resposta:** variantes exploradas, evidência (screenshots ou saída/timing observados), trade-offs, recomendação e caminho do scratch. Diga claramente que o protótipo é descartável.
