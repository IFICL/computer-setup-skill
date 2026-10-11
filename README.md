# Computer Setup Skill

A reusable Codex skill for configuring shared Zsh, tmux, SSH, and GitHub tooling on macOS and Linux while preserving existing user configuration.

## Use the skill

Install the repository contents as a folder named `computer-setup-skill` under the agent's skill directory (for Codex, normally `~/.codex/skills/`). Keep `SKILL.md`, `references/`, `assets/`, and `agents/` together so relative resource links work. If the folder already exists, inspect it before replacing it.

Example request: “Use $computer-setup-skill to inspect this Mac, compare it with my reference settings, and apply the shared Zsh and tmux setup.” Specify which sections should be applied; the reference application list alone does not request installation of every app. The owner installs iTerm2 manually, and Cursor is optional.

System preferences are a dated reference checklist. The iTerm2 plist preserves global settings and profiles with the source working directory removed; it still contains some personal runtime/UI metadata. Review it before a full restore.

Maintenance requests update the files locally. Commit and push require explicit user instructions.

## Structure

- [`SKILL.md`](SKILL.md): skill entry point and operating rules
- [`references/shared-setup.md`](references/shared-setup.md): shared setup procedure
- [`references/iterm2-profile.md`](references/iterm2-profile.md): export and reuse an optional iTerm2 profile
- [`references/iterm2-default-diff.md`](references/iterm2-default-diff.md): differences from the iTerm2 3.6.11 factory profile
- [`references/macos-required-apps.md`](references/macos-required-apps.md): evolving macOS application list and usage notes
- [`references/macos-system-settings.md`](references/macos-system-settings.md): curated, privacy-conscious macOS behavior settings
- [`references/macos-python-uv.md`](references/macos-python-uv.md): optional Python environment using `IFICL/my-uv-env` and uv
- [`assets/iterm2/com.googlecode.iterm2.plist`](assets/iterm2/com.googlecode.iterm2.plist): sanitized iTerm2 settings reference with the source working directory removed
- [`assets/dotfiles/zsh-shared.zsh`](assets/dotfiles/zsh-shared.zsh): reusable Zsh highlighting settings
- [`assets/dotfiles/tmux.conf`](assets/dotfiles/tmux.conf): baseline tmux configuration
- [`agents/openai.yaml`](agents/openai.yaml): Codex interface metadata
