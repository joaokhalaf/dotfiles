---
name: principle-prove-it-works
description: "Aplique ao terminar uma tarefa, antes de declarar pronto. Verifique no artefato real (rode a feature, leia o valor real, inspecione o diff), não num proxy, autodeclaração ou \"compila\"."
disable-model-invocation: true
---

# Prove It Works

Verifique cada saída conferindo a coisa real diretamente: rode a feature, leia o valor real, inspecione o diff. Proxies (mtime de arquivo, autodeclaração, saída em cache, "compila") não contam. Quando um check falha, suspeite do método de observação antes do sistema.

Escreva o check como script quando puder. Um script determinístico que refaz a comparação vence uma olhada única. Deixe a saída onde o humano veja e faça commit só quando a trilha precisar ser auditável depois.

Diferencie aprovado, reprovado e não executado. Check que não rodou não conta como aprovação.
