# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="robbyrussell"

plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
alias ff='fzf --preview="bat --style=numbers --color=always {} | head -200"'

eval "$(zoxide init zsh)"
alias cd="z"

alias l='eza -lah --icons'
alias lt='eza --tree --level=2 --icons'
alias lta='eza --tree --level=2 -a --icons'

alias f='fd --hidden --exclude .git'

alias rgf='rg --files | fzf'

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
