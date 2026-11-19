---
name: unslop
description: Tira vícios de texto de IA de qualquer prosa em pt-BR ou inglês. Use ao escrever ou revisar README, docs, descrição de PR, commit, mensagem, post ou resposta longa, ou quando pedirem para deixar um texto menos "com cara de IA" / remove AI tells / unslop.
---

# Unslop

Edite o texto para remover padrões de IA. Procure os padrões abaixo e reescreva.
Preserve o sentido e o tom pretendido. As regras valem para pt-BR e inglês.

Os números das regras são ids estáveis citados por outras skills. Regra removida deixa lacuna.

3. Sem orações finais em gerúndio que não acrescentam fato ("garantindo…", "destacando…" / "ensuring…", "highlighting…").
5. Sem atribuições vagas ("especialistas afirmam" / "experts believe"). Nomeie a fonte ou apague.
7. Sem vocabulário de IA. pt-BR: além disso, crucial, fundamental, robusto, aprimorar, potencializar, alavancar, fomentar, vale ressaltar, mergulhar, cenário, panorama, jornada, vibrante, pilar. EN: additionally, crucial, delve, enhance, foster, landscape, pivotal, showcase, testament, underscore, vibrant.
8. Diga "é" ou "tem", não "serve como", "se destaca como", "conta com", "apresenta" / "serves as", "stands as", "boasts", "features".
9. Sem "não só X, mas também Y" / "not just X, but Y". Diga o ponto.
10. Não force ideias em trios.
11. Um nome por coisa. Repita o nome.
12. Sem "de X a Y" / "from X to Y", salvo quando X e Y estão numa escala real.
13. Sem travessão, meia-risca ou hífen usado como travessão, e sem parênteses no lugar deles. Use ponto ou vírgula.
14. Dois-pontos antes de uma lista ou exemplo, nunca no meio da frase como conector.
15. Não ponha em negrito todo nome próprio ou sigla.
16. Sem rótulo em negrito com dois-pontos que repete a linha ("**Performance:** a performance melhorou…"). Abertura em negrito que termina em ponto e traz detalhe novo é aceitável.
17. Títulos com só a primeira letra maiúscula (sentence case).
18. Sem emojis decorativos.
19. Aspas retas.
20. Sem frases de chatbot ("Espero ter ajudado!", "Fico à disposição", "Me avise se…" / "I hope this helps!", "Let me know if…").
22. Sem abertura de elogio ou concordância ("Ótima pergunta!", "Perfeito!" / "Great question!"). Responda direto.
23. Corte enchimento. "A fim de" vira "para"; apague "é importante notar que" / "in order to" → "to", "it is important to note that".
24. No máximo uma ressalva: "pode" / "may".
25. Sem conclusões genéricas. Declare planos ou fatos específicos.
26. Sem substantivos-metáfora abstratos: substrato, alavanca, vetor, nexo, primitivo, superfície, andaime, paradigma, catraca, norte, flywheel / substrate, wedge, vector, nexus, primitive, harness, surface, scaffolding, paradigm, ratchet, north star, flywheel. Use a palavra concreta.
27. Diga o que faz, não como parece. Nomeie o mecanismo ou o número. Corte frase que caberia sem mudança na documentação de outro projeto.
28. Uma ideia por frase. Divida a frase que o leitor precisa reler.
29. Voz ativa. Nomeie o agente, salvo quando é desconhecido ou irrelevante.
30. Corte advérbios ou use um verbo mais forte. Dê o número.
31. Use a palavra simples: "usar", não "utilizar" ou "lançar mão de" / "use", not "utilize" or "leverage".
32. Sem metáfora, aforismo, código personificado ou verbo figurado onde existe expressão literal.
33. Escreva frases inteiras, com artigos e verbos. Escreva por extenso setas e abreviações.

Termos técnicos com nome próprio (nomes de ferramentas, APIs, flags) seguem a grafia original; as regras 7 e 26 não se aplicam a um identificador real do código, como `harness.md` ou `surface`.
