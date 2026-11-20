# Homebrew
if [[ -x /home/linuxbrew/.linuxbrew/bin/brew ]]; then
  eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
fi

# History
HISTFILE="$HOME/.zsh_history"
HISTSIZE=20000
SAVEHIST=20000

setopt APPEND_HISTORY
setopt SHARE_HISTORY
setopt HIST_IGNORE_DUPS
setopt HIST_IGNORE_SPACE
setopt HIST_REDUCE_BLANKS

# Completion
autoload -Uz compinit
compinit

zstyle ':completion:*' menu select
zstyle ':completion:*' group-name ''
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path "$HOME/.cache/zsh"
zstyle ':completion:*:descriptions' format '%F{blue}%d%f'

# Navegação e edição
bindkey -e
bindkey '^I' expand-or-complete

# Zoxide
if command -v zoxide >/dev/null 2>&1; then
  eval "$(zoxide init zsh)"
fi

# FZF
if command -v fzf >/dev/null 2>&1; then
  source <(fzf --zsh)
fi

# Autosuggestions
ZSH_AUTOSUGGEST_STRATEGY=(history)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#6c7086'

AUTOSUGGESTIONS="$(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh"

if [[ -f "$AUTOSUGGESTIONS" ]]; then
  source "$AUTOSUGGESTIONS"
fi

# Aliases
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gw='git worktree list'
alias ll='ls -lah'

# Worktree por tarefa: cria ~/work/worktrees/<repo>/<tarefa> a partir do default remoto e abre no VS Code
wt() {
  if [[ -z "$1" ]]; then
    echo "uso: wt <tarefa>" >&2
    return 1
  fi
  local root dir base file
  root="$(git rev-parse --path-format=absolute --git-common-dir)" || return 1
  root="${root:h}"
  dir="$HOME/work/worktrees/${root:t}/${1//\//-}"
  if [[ ! -d "$dir" ]]; then
    git -C "$root" fetch origin --quiet || return 1
    base="$(git -C "$root" symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null || echo origin/main)"
    if git -C "$root" show-ref --verify --quiet "refs/heads/$1"; then
      git -C "$root" worktree add "$dir" "$1" || return 1
    else
      git -C "$root" worktree add --no-track -b "$1" "$dir" "$base" || return 1
    fi
    # .env* ignorados não vêm com o checkout: copia do repositório principal
    git -C "$root" ls-files -z --others --ignored --exclude-standard -- '.env*' '*/.env*' |
      while IFS= read -r -d '' file; do
        [[ "$file" == (*/|)node_modules/* ]] && continue
        mkdir -p "$dir/${file:h}" && cp -p "$root/$file" "$dir/$file" && echo "copiado: $file"
      done
  fi
  code "$dir"
}

# Fecha a tarefa: remove a worktree (recusa se houver mudança) e a branch, se já integrada
wtd() {
  if [[ -z "$1" ]]; then
    echo "uso: wtd <tarefa>" >&2
    return 1
  fi
  local root dir
  root="$(git rev-parse --path-format=absolute --git-common-dir)" || return 1
  root="${root:h}"
  dir="$HOME/work/worktrees/${root:t}/${1//\//-}"
  [[ "$PWD/" == "$dir/"* ]] && cd "$root"
  git -C "$root" worktree remove "$dir" || return 1
  git -C "$root" fetch origin --quiet
  if git -C "$root" branch --merged "$(git -C "$root" symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null || echo origin/main)" --format='%(refname:short)' | grep -qx -- "$1"; then
    git -C "$root" branch -D "$1"
  else
    echo "branch $1 mantida: não está na main remota (squash merge? apague com git branch -D $1)"
  fi
}

# Starship
eval "$(starship init zsh)"

# Syntax highlighting: carregar por último
SYNTAX_HIGHLIGHT="$(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"

if [[ -f "$SYNTAX_HIGHLIGHT" ]]; then
  source "$SYNTAX_HIGHLIGHT"
fi

# Vite+ bin (https://viteplus.dev)
. "/home/khalaf/.config/vite-plus/env"
