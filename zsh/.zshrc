if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="powerlevel10k/powerlevel10k"

plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

alias c='clear'
alias grep="rg"

eval "$(zoxide init zsh)"
alias cd="z"

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
export FZF_DEFAULT_OPTS="--height 40% --layout=reverse --border --preview 'bat --color=always {}'"
export FZF_DEFAULT_COMMAND="fd --type f --hidden --follow --exclude .git"
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
export FZF_ALT_C_COMMAND="fd --type d --hidden --follow --exclude .git"

fzf-history() { zle -I; eval $(history | fzf --tac | sed 's/ *[0-9]* *//') }
zle -N fzf-history
bindkey '^R' fzf-history

fzf-cd() { zle -I; cd "$(fd --type d --hidden --follow --exclude .git | fzf)" }
zle -N fzf-cd
bindkey '^F' fzf-cd

alias lg="lazygit"

export NVM_DIR="$HOME/.nvm"
nvm() {
  unset -f nvm
  [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
  [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
  nvm "$@"
}

if [ -d "/usr/local/go/bin" ]; then
  export PATH=$PATH:/usr/local/go/bin
fi
if [ -d "$HOME/go/bin" ]; then
  export PATH=$PATH:$HOME/go/bin
fi

function load_composer() {
  source $ZSH/plugins/composer/composer.plugin.zsh
}

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh


eval "$(mise activate zsh)"
