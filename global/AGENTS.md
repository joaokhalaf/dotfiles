
## Local browser validation
Use the `local-browser` MCP server to navigate and validate local web apps. Tool `browser` supports open, snapshot, click, fill, press, hover, scroll, screenshot, console, errors, get, reload and eval. Start the app server first. Use the workspace name as `session` to isolate tasks; reuse that name across providers to share a browser. CLI fallback: `/home/khalaf/.local/bin/local-browser --task <workspace> open http://localhost:<port>` then `snapshot -i`, `click @ref`, `fill @ref text`, `screenshot /absolute/path.png`. This runs Chromium in WSL.

## Engineering workflow
For engineering work (code changes, debugging, investigation of a codebase, reviews, plans, PRs), read and follow `/home/khalaf/work/dotfiles/skills/poteto-mode/SKILL.md` before acting; it starts with the grilling interview and routes to a playbook. Subagents follow `/home/khalaf/work/dotfiles/skills/poteto-mode/worker.md` instead. Casual conversation and questions unrelated to a codebase do not trigger it.
