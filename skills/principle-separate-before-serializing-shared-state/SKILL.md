---
name: principle-separate-before-serializing-shared-state
description: "Aplique quando atores concorrentes podem escrever no mesmo arquivo, branch, chave ou objeto de estado. Elimine o compartilhamento primeiro; serialize estruturalmente só quando um escritor único é uma invariante real."
disable-model-invocation: true
---

# Separate Before Serializing Shared State

Quando atores concorrentes podem escrever o mesmo arquivo, branch, chave ou objeto, pergunte primeiro se precisam de um objeto compartilhado ou estão publicando fatos independentes. Por padrão, dê a cada ator seu próprio arquivo, chave, branch, worktree ou diretório de estado, e junte só onde o estado é lido. Dois workers escrevendo cada um seu campo num mesmo `state.json` ainda é mutação compartilhada.

Só quando um alvo de escrita compartilhado é invariante real, serialize o acesso estruturalmente (lockfile, escritor único, fases sequenciais, compare-and-swap). Instruções não são controle de concorrência, e "precisamos de um lock" é um cheiro a verificar primeiro. Reservas do Herdr são cooperativas, não exclusão garantida pelo SO.
