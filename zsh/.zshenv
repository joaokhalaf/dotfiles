. "$HOME/.cargo/env"
export PATH="$HOME/.local/bin:$PATH"

# Vite+ bin (https://viteplus.dev)
. "/home/khalaf/.config/vite-plus/env"

# Ajustes desta máquina, fora do repo (ex.: plano do Claude)
[[ -f "$HOME/.zshenv.local" ]] && . "$HOME/.zshenv.local"
