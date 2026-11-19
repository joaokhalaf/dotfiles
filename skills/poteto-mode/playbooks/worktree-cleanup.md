### Limpeza de worktrees

1. Fotografe e audite. Registre `df -h /` e rode `scripts/worktree-audit.sh [-b <ref-base>] [repo]` (**principle-build-the-lever**). Sem `-b`, `MERGED` compara com `origin/HEAD`; passe `-b origin/<branch>` quando os PRs miram outra branch. Os caminhos vêm de `git worktree list`, nunca digitados à mão: worktrees do T3, do Claude Code (`.claude/worktrees`) e manuais vivem em lugares diferentes. O script classifica por tamanho, idade, estado de merge, trabalho não commitado e PR, e sugere um balde.
2. O balde é conselho, não permissão. Threads fixadas e ativas são o artefato real (**principle-prove-it-works**). Obtenha esse conjunto do usuário ou da lista de threads (`t3_worktree_list` no T3) e cruze cada candidato.
3. Verifique uso antes de apagar. Para qualquer dúvida, confira se alguma thread ou agente ativo usa a worktree.
4. Pause em perda irreversível. `wip:N` são N edições rastreadas não commitadas: mostre o diff e obtenha decisão. Remover worktree limpa é recuperável pela branch; trabalho não commitado não. `scratch:N` é descartável não rastreado: nomeie os arquivos. Limpa, integrada e sem uso prossegue; `wip` e em uso pausam.
5. Pode o conjunto confirmado: `git worktree remove --force <caminho>` por caminho. Se o diretório sobrar por artefatos ignorados, `rm -rf` nele e depois `git worktree prune`. Branches sobrevivem. Confirme com `df -h /` e liste de novo.
6. Outros recuperadores, só os que o usuário não pediu para manter: caches de pacotes (pnpm, bun, npm, uv, cargo), `node_modules` de worktrees removidas, imagens Docker órfãs.

Este é o playbook que apaga estado do usuário sem revisão de código; os gates acima são a revisão.

**Resposta:** `df -h /` antes e depois com espaço recuperado, worktrees podadas e uma razão por linha para cada uma mantida (em uso por qual thread, ou trabalho não commitado).
