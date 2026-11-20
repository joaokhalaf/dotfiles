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

# Starship
eval "$(starship init zsh)"

# Syntax highlighting: carregar por último
SYNTAX_HIGHLIGHT="$(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"

if [[ -f "$SYNTAX_HIGHLIGHT" ]]; then
  source "$SYNTAX_HIGHLIGHT"
fi

# Vite+ bin (https://viteplus.dev)
. "/home/khalaf/.config/vite-plus/env"
