# Shared command-line setup

Use this procedure on both macOS and Linux. Detect the current system and preserve existing configuration instead of assuming a clean machine.

## Zsh and Oh My Zsh

1. Confirm that `zsh` is installed. If it is missing, use the detected system package manager and show the planned install command before running it.
2. Check whether Oh My Zsh already exists at `${ZSH:-$HOME/.oh-my-zsh}`.
3. If it is absent, use the current installer from the official Oh My Zsh repository. Explain that the installer downloads and runs a remote script, and obtain authorization before executing it.
4. Install these plugins under `${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/` when absent:
   - `zsh-syntax-highlighting`
   - `zsh-autosuggestions`
5. Merge both plugin names into the existing `plugins=(...)` declaration in `.zshrc`. Preserve every existing plugin and avoid adding duplicates.
6. Append the contents of [`../assets/dotfiles/zsh-shared.zsh`](../assets/dotfiles/zsh-shared.zsh) if equivalent settings are not already present.
7. Start a disposable interactive Zsh session or use an available syntax check. Do not replace the user's current login shell unless requested.

## tmux

1. Check for `tmux` before installing it.
2. If missing, select the command from the detected platform:
   - macOS with Homebrew: `brew install tmux`
   - Debian or Ubuntu: `sudo apt-get install tmux`
   - Fedora: `sudo dnf install tmux`
   - Arch Linux: `sudo pacman -S tmux`
3. If `~/.tmux.conf` does not exist, copy the baseline from [`../assets/dotfiles/tmux.conf`](../assets/dotfiles/tmux.conf).
4. If it exists, show a diff and merge only the requested settings. Never replace it silently.
5. When tmux is installed, validate with `tmux -f <candidate-file> -L setup-skill start-server \; show-options -g` and stop the temporary server afterward.

Package indexes and installation commands vary. Verify current platform guidance when accuracy depends on changing external documentation.

## SSH and GitHub

1. Inspect `~/.ssh` without displaying private-key contents. List only filenames, permissions, and public-key fingerprints when useful.
2. Reuse an appropriate existing key when the user chooses it. Never overwrite an existing private key.
3. If a new key is needed, prefer Ed25519 unless the destination has a known compatibility constraint. Ask for the email/comment and output path before generation.
4. Start or reuse `ssh-agent` and add the selected key as appropriate for the operating system.
5. Display the public key and explain that it must be added to the user's GitHub account. Do not upload it or change the account without explicit authorization.
6. Configure Git identity only after collecting the intended name and email. Do not guess them from machine state.
7. Test GitHub authentication with `ssh -T git@github.com`. Explain that GitHub commonly returns a non-zero status even after successful authentication; judge success from the message as well as the exit code.

Never print, copy, transmit, commit, or otherwise expose private-key material.
