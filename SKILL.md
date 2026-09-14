---
name: computer-setup-skill
description: Set up a reusable Zsh, tmux, SSH, and GitHub command-line environment on macOS or Linux. Use when configuring a new workstation or repairing this shared shell setup; do not overwrite existing dotfiles or SSH keys without approval.
---

# Workstation Setup

Configure the requested parts of a macOS or Linux command-line environment while preserving the user's existing setup.

## Workflow

1. Identify the operating system, package manager, shell, and which requested tools are already installed.
2. Read [references/shared-setup.md](references/shared-setup.md) for the shared Zsh, tmux, SSH, and GitHub procedure.
   On macOS, also read [references/iterm2-profile.md](references/iterm2-profile.md) when the user wants to reproduce or import the reference iTerm2 profile.
   Read [references/macos-required-apps.md](references/macos-required-apps.md) when recommending or reviewing the owner's required macOS applications.
3. Show the proposed changes before modifying an existing dotfile. Back up files before any approved replacement or substantial rewrite.
4. Run only the requested setup sections. Installation, remote downloads, SSH-key creation, and GitHub authentication require the user's authorization at the point where they will occur.
5. Verify installed commands and configuration syntax where the relevant tool supports it. Report manual steps that remain.

## Resources

- Copy or merge [assets/dotfiles/zsh-shared.zsh](assets/dotfiles/zsh-shared.zsh) for the shared Zsh highlighting preferences.
- Use [assets/dotfiles/tmux.conf](assets/dotfiles/tmux.conf) as the baseline tmux configuration.
- On macOS, use [assets/iterm2/com.googlecode.iterm2.plist](assets/iterm2/com.googlecode.iterm2.plist) as the optional reference for iTerm2 global and profile settings. Review it before import and never assume its commands, fonts, identifiers, or other machine-specific values are portable.
- Treat the macOS application list as owner preferences that may grow over time. Verify changing details such as compatibility and installation commands against each official source before acting.
