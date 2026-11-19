### Eval

**Você é dono do desenho do experimento. Planeje, cegue, execute, sintetize.**

**Inegociáveis de cegamento:**

- Nenhum `eval`, `test`, `judge`, `experiment`, `rubric`, `score`, `compare`, `benchmark`, `candidate` ou `arena` em diretório, arquivo ou prompt que o candidato vê.
- O prompt do candidato parece um pedido orgânico de usuário. Declare o objetivo, não o meta.
- Sem pistas que induzam a cadeia. Não peça ao candidato que liste skills ou princípios aplicados. Peça notas de design em geral e avalie a cadeia pela forma do código, não por autodeclaração.
- Nomes de diretórios e slugs sanitizados, com cara de projeto real.
- Não diga ao candidato que existem outros candidatos.
- O juiz pode saber que julga, mas vê saídas só por rótulo sanitizado, nunca por nome de modelo.
- Comparando duas variantes: um juiz pontua os dois conjuntos numa passada, na mesma escala, cego à origem.

**Passos:**

1. **Enquadre.** Qual variante está em teste e qual comportamento conta como sucesso. Rubrica de 3-6 critérios concretos, só para o juiz.
2. **Ambientes sanitizados.** Um diretório por candidato com a variante no lugar e o contexto que uma tarefa orgânica teria.
3. **Um prompt orgânico.** O que um usuário digitaria, sem vazar o que se mede.
4. **N candidatos em paralelo** por subagente, cada um no seu diretório, mesmo prompt. Modelos diferentes só se o usuário pedir; senão, contextos separados do modelo da sessão.
5. **Um juiz cego** em contexto novo, com rótulos sanitizados e a rubrica.
6. **Verifique a cadeia pelas transcrições**, não pela autodeclaração. Leia as transcrições do workspace atual (caminhos em [harness](../references/harness.md)), sem atravessar outros projetos. Avalie pelos arquivos realmente abertos e pela forma do código.
7. **Leia cada saída você mesmo**, de ponta a ponta, e compare com o veredito do juiz. Discordância indica viés ou rubrica ambígua. Sintetize.

**Resposta:** variante em teste, rubrica, notas por candidato, veredito do juiz, sua síntese e recomendação de promover ou não a variante.
