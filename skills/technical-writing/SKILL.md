---
name: technical-writing
description: Padrão de escrita técnica em camadas (Diátaxis, estilo Google para desenvolvedores, regras STE, sintaxe sem ambiguidade) para pt-BR e inglês. Use ao escrever ou revisar docs, README, RFC, guias, descrição de PR ou mensagem de commit.
---

# Escrita técnica

Escreva para um engenheiro cansado entender na primeira leitura.

- Corte toda palavra que não trabalha.
- Use a palavra curta e cotidiana: "usar", não "utilizar" / "use", not "utilize".
- Quando uma regra piora a frase, conserte a frase de outro jeito ou deixe como está.
- Escreva o símbolo, arquivo, flag ou comando real, não um sinônimo ou descrição dele.
- Não invente jargão. Use as palavras que um desenvolvedor diria em voz alta. Explique um padrão nomeado na primeira vez.

## Varie o ritmo

- Misture tamanhos de frase. Divida a frase que carrega dois pensamentos. Mantenha a longa que carrega um.
- Tenha opinião na explicação. Mantenha a referência seca.
- Seja específico. Não "mudanças de schema podem causar problemas", e sim "renomear uma coluna quebra o build".

## Escolha o modo primeiro (Diátaxis)

Um documento, um modo. Não misture: divida e ligue.

- **Tutorial: aprender fazendo.** Diga o que o aprendiz vai construir. Cada passo produz um resultado visível, e você diz o que ele deve ver. Explicação ganha uma oração e um link.
- **How-to: passos até um objetivo.** Resolva o problema do leitor. Assuma competência. Só ação. Permita bifurcações. Nomeie o guia pela tarefa.
- **Referência: fatos para consulta.** Só descreva. Seja seco, completo e seguro. Espelhe a estrutura da coisa descrita.
- **Explicação: entendimento e porquê.** Um tema delimitado. Dê contexto: decisões de design, histórico, restrições, alternativas. Opinião é permitida aqui e só aqui.

## Frases dirigidas ao leitor (estilo Google)

- Fale com o leitor por "você" / "you", no presente.
- Diga quem faz o quê. Passiva só quando o agente é desconhecido ou irrelevante.
- Instruções no imperativo. Condição antes da instrução, caso comum primeiro.
- Sem buzzwords, linguagem figurada ou "por favor", e nunca "simplesmente", "fácil" ou "rapidamente" num procedimento.
- Não anuncie o que vem a seguir, e não comece frases seguidas com a mesma expressão.
- Links com texto que diz para onde vão.
- Títulos carregam o ponto, só com a primeira letra maiúscula. Um h1 por página, sem pular níveis.
- Listas numeradas para sequências, marcadores para o resto. Introduza a lista com uma frase completa. Itens paralelos.
- Código em fonte de código. Elementos de UI em negrito. Sem "etc.".

## Uma afirmação por vez (regras STE)

- Uma instrução por frase. Um pensamento por frase no resto.
- Divida instruções com mais de ~20 palavras e outras frases com mais de ~25.
- Aviso ou condição antes do passo que protege.
- Mantenha os artigos ("o", "a", "um" / "the", "a").
- Cada palavra com um sentido, e uma palavra por ação.
- Procedimentos como comandos diretos, nunca narração nem passiva.
- Evite gerúndios onde puder.

## Nenhuma frase com duas leituras

- Mantenha "só", "apenas" e "não" junto da palavra que modificam.
- Quebre sequências longas de substantivos.
- Todo "isso", "ele", "eles" aponta para uma coisa óbvia. Nunca use "isso" ou "o que" para apontar uma oração inteira.
- Não omita verbos nem as palavras pequenas que mostram estrutura, como "que".
- Repita o artigo numa série quando isso evita leitura errada. Deixe claro o que "e" ou "ou" une.
- Pontos, não ponto e vírgula nem travessão. Sem barras e sem "(s)". Texto entre parênteses é uma unidade gramatical completa.
- Cada coisa com um nome, em todo lugar.
- Sem expressões idiomáticas, coloquialismos, abreviações latinas ("i.e.", "e.g.", "vs.") e metáforas.

## Voz e especificidades do repositório

- Aplique **unslop** a todo texto que esta skill tocar. Ela é dona do catálogo de vícios: vocabulário de IA, enchimento, ressalvas, tiques de formatação.
- Descrição de PR e mensagem de commit também são escrita. Todas as camadas menos Diátaxis se aplicam. Corpo de PR é um briefing que o revisor lê em menos de um minuto. Não cole logs de swarm, listas de SHA ou tabelas de métricas: ligue para eles.
- Strings de UI de produto não são documentação. Use o guia de texto do produto.
- Escreva caminhos reais. Toda contagem ou árvore precisa ser verdadeira no commit que a entrega, junto do comando que a regenera.
- Escreva na língua do documento ou repositório. Em pt-BR, as regras valem com os equivalentes acima.
