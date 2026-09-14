# Computer Setup Skill

A reusable Codex skill for configuring shared Zsh, tmux, SSH, and GitHub tooling on macOS and Linux while preserving existing user configuration.

## Structure

- [`SKILL.md`](SKILL.md): skill entry point and operating rules
- [`references/shared-setup.md`](references/shared-setup.md): shared setup procedure
- [`references/iterm2-profile.md`](references/iterm2-profile.md): export and reuse an optional iTerm2 profile
- [`references/iterm2-default-diff.md`](references/iterm2-default-diff.md): differences from the iTerm2 3.6.11 factory profile
- [`references/macos-required-apps.md`](references/macos-required-apps.md): evolving macOS application list and usage notes
- [`assets/iterm2/com.googlecode.iterm2.plist`](assets/iterm2/com.googlecode.iterm2.plist): sanitized iTerm2 settings reference with the source working directory removed
- [`assets/dotfiles/zsh-shared.zsh`](assets/dotfiles/zsh-shared.zsh): reusable Zsh highlighting settings
- [`assets/dotfiles/tmux.conf`](assets/dotfiles/tmux.conf): baseline tmux configuration
- [`agents/openai.yaml`](agents/openai.yaml): Codex interface metadata
