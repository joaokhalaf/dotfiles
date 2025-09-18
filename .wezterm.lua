local wezterm = require("wezterm")
local act = wezterm.action
local config = wezterm.config_builder()

config.color_scheme = 'Catppuccin Mocha'

config.front_end = "OpenGL"
config.prefer_egl = true
config.max_fps = 144
config.animation_fps = 1

config.default_cursor_style = "BlinkingBlock"
config.cursor_blink_rate = 500
config.term = "xterm-256color"

config.default_prog = { "wsl.exe", "~" }

config.font = wezterm.font("JetBrainsMono Nerd Font")
config.font_size = 16.0
config.cell_width = 0.9

config.window_background_opacity = 0.65
config.text_background_opacity = 1.00
config.window_decorations = "RESIZE"
config.window_padding = {
  left = 8,
  right = 8,
  top = 4,
  bottom = 4,
}
config.initial_cols = 100
config.window_close_confirmation = 'NeverPrompt'

config.enable_scroll_bar = true

config.scrollback_lines = 10000

config.hyperlink_rules = wezterm.default_hyperlink_rules()

config.harfbuzz_features = {"calt", "liga", "dlig", "ss01"}

config.pane_focus_follows_mouse = true

config.use_fancy_tab_bar = true
config.hide_tab_bar_if_only_one_tab = true

config.window_frame = {
  font = wezterm.font({ family = "JetBrainsMono Nerd Font", weight = "Regular" }),
  active_titlebar_bg = "#0c0b0f",
}

config.keys = {
  {
    key = 'n',
    mods = 'CTRL|SHIFT|ALT',
    action = wezterm.action.SpawnWindow,
  },
  {
    key = 'v',
    mods = 'CTRL',
    action = act.PasteFrom 'Clipboard',
  },
  {
    key = 'c',
    mods = 'CTRL',
    action = act.CopyTo 'Clipboard',
  },
}


return config
