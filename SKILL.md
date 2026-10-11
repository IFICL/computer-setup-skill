---
name: computer-setup-skill
description: Set up Zsh, tmux, SSH, and GitHub on macOS or Linux, and reproduce the owner's macOS application, iTerm2, and system preferences. Use for new-computer setup or repairs to this environment.
---

# Workstation Setup

Configure the requested parts of a macOS or Linux command-line environment while preserving the user's existing setup.

## Workflow

1. Identify the operating system, package manager, shell, and which requested tools are already installed.
2. Read [references/shared-setup.md](references/shared-setup.md) for the shared Zsh, tmux, SSH, and GitHub procedure.
   On macOS, also read [references/iterm2-profile.md](references/iterm2-profile.md) when the user wants to reproduce or import the reference iTerm2 profile.
   Read [references/macos-required-apps.md](references/macos-required-apps.md) when recommending or reviewing the owner's required macOS applications.
   Read [references/macos-system-settings.md](references/macos-system-settings.md) when comparing or reproducing the owner's macOS behavior preferences.
   Read [references/macos-python-uv.md](references/macos-python-uv.md) only when the user requests the optional macOS Python environment backed by `IFICL/my-uv-env`.
3. Show the proposed changes before modifying an existing dotfile. Back up files before any approved replacement or substantial rewrite.
4. Run only the requested setup sections. Use the authorization already provided by the user; ask only for missing choices or additional authority, such as replacing existing configuration or granting protected permissions.
5. Verify installed commands and configuration syntax where the relevant tool supports it. Report manual steps that remain.
6. Report each requested item as completed, already configured, skipped by choice, or blocked with its specific reason. Commit or push only when the user explicitly requests that action.

## Resources

- Copy or merge [assets/dotfiles/zsh-shared.zsh](assets/dotfiles/zsh-shared.zsh) for the shared Zsh highlighting preferences.
- Use [assets/dotfiles/tmux.conf](assets/dotfiles/tmux.conf) as the baseline tmux configuration.
- On macOS, use [assets/iterm2/com.googlecode.iterm2.plist](assets/iterm2/com.googlecode.iterm2.plist) as the optional reference for iTerm2 global and profile settings. Review it before import and never assume its commands, fonts, identifiers, or other machine-specific values are portable.
- Treat the macOS application list as owner preferences that may grow over time. Verify changing details such as compatibility and installation commands against each official source before acting.
- Treat the macOS system settings as a descriptive reference, not an executable script. Confirm every system change and avoid copying device-specific state, paths, accounts, privacy permissions, or recent-history data.
