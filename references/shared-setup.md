# Shared command-line setup

Use this procedure on both macOS and Linux. Detect the current system and preserve existing configuration instead of assuming a clean machine.

## Zsh and Oh My Zsh

### Prerequisites and Oh My Zsh installation

Check `uname -s`, `command -v zsh git curl`, and `zsh --version`. On Linux, inspect `/etc/os-release` before selecting a package manager. macOS includes Zsh; a missing Git may require Apple's Command Line Tools (`xcode-select --install`, followed by user completion of the installation dialog). Install missing Linux prerequisites with the distribution's package manager, for example `sudo apt-get update` then `sudo apt-get install zsh git curl` on Debian/Ubuntu.

Before installation, locate and back up the active startup file, using a timestamped copy such as:

```zsh
setup_rc="${ZDOTDIR:-$HOME}/.zshrc"
if [[ -f "$setup_rc" ]]; then
  cp -p "$setup_rc" "$setup_rc.backup-$(date +%Y%m%d-%H%M%S)"
fi
```

For a missing Oh My Zsh installation, download the official installer into a temporary directory, inspect it, then run it while preserving the existing startup file and login shell:

```zsh
setup_tmp=$(mktemp -d)
curl -fL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh \
  -o "$setup_tmp/install-oh-my-zsh.sh"
# Inspect the downloaded script before the next command.
KEEP_ZSHRC=yes CHSH=no RUNZSH=no sh "$setup_tmp/install-oh-my-zsh.sh"
```

Run the installer only after a successful download and inspection. If an Oh My Zsh directory already exists, check for `oh-my-zsh.sh` rather than rerunning the installer over it. An existing preserved `.zshrc` may need the `ZSH` assignment and source line shown below. For a non-default `ZDOTDIR` or Oh My Zsh location, inspect the installer behavior and adapt paths explicitly.

Official source: [Oh My Zsh installation](https://github.com/ohmyzsh/ohmyzsh#basic-installation).

1. Confirm that `zsh` is installed. If it is missing, use the detected system package manager and show the planned install command before running it.
2. Check whether Oh My Zsh already exists at `${ZSH:-$HOME/.oh-my-zsh}`.
3. If it is absent, use the current installer from the official Oh My Zsh repository. Explain that the installer downloads and runs a remote script, and obtain authorization before executing it.
4. Download the two plugins using the commands below, skipping any destination that already exists. Inspect an existing installation before changing it.
5. Edit the existing plugin list in the active Zsh startup file, normally `~/.zshrc` or `${ZDOTDIR}/.zshrc` when `ZDOTDIR` is set. Preserve existing plugins, add each new name only once, and put `zsh-syntax-highlighting` last.
6. Keep the plugin list **before** `source "$ZSH/oh-my-zsh.sh"`. Put the shared highlighting settings **after** that line. Merge settings from [`../assets/dotfiles/zsh-shared.zsh`](../assets/dotfiles/zsh-shared.zsh) without duplicating an existing block.
7. Check syntax and open a fresh interactive Zsh session to verify both plugins. Do not change the user's login shell unless requested.

### Download the plugins

Run these in Zsh after confirming Oh My Zsh is installed:

```zsh
git clone https://github.com/zsh-users/zsh-autosuggestions \
  "${ZSH_CUSTOM:-${ZSH:-$HOME/.oh-my-zsh}/custom}/plugins/zsh-autosuggestions"

git clone https://github.com/zsh-users/zsh-syntax-highlighting \
  "${ZSH_CUSTOM:-${ZSH:-$HOME/.oh-my-zsh}/custom}/plugins/zsh-syntax-highlighting"
```

`ZSH_CUSTOM` takes precedence; otherwise the plugins belong under the current Oh My Zsh installation's `custom/plugins` directory. For an installation using a custom path, confirm that path before cloning.

### Activate plugins in `.zshrc`

Back up the startup file before editing it. Update its existing `plugins=(...)` declaration rather than appending a second declaration. The following is an example of the required order; retain any other plugins and the existing `ZSH` path:

```zsh
export ZSH="$HOME/.oh-my-zsh"  # Retain an existing custom installation path.

plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
)

source "$ZSH/oh-my-zsh.sh"

# Shared zsh-syntax-highlighting preferences
typeset -A ZSH_HIGHLIGHT_STYLES
ZSH_HIGHLIGHT_STYLES[suffix-alias]=fg=123,underline
ZSH_HIGHLIGHT_STYLES[precommand]=fg=123,underline
ZSH_HIGHLIGHT_STYLES[arg0]=fg=123
ZSH_HIGHLIGHT_STYLES[path]='fg=229,underline'
```

Oh My Zsh loads the named plugins when its startup script is sourced. Do not also source the plugins individually, because that would load them twice. If other configuration defines Zsh line-editor widgets after Oh My Zsh loads, review the syntax-highlighting documentation for the appropriate loading order.

### Verify activation

Check syntax without executing the startup file:

```zsh
zsh -n "${ZDOTDIR:-$HOME}/.zshrc"
```

Then open a new terminal tab (or run `zsh` to start a fresh interactive shell). Syntax checking alone does not prove the plugins loaded correctly.

- Type the beginning of a command in shell history: a dimmed suggestion should appear. Press Right Arrow at the end of the line to accept it.
- Type a command and a filesystem path: syntax highlighting should appear; path highlighting uses the shared style above.
- If a plugin is reported as missing, compare its directory name and location with the plugin list and the configured `ZSH_CUSTOM` path.

Official installation instructions: [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md) and [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md).

### Maintain or recover the shell setup

Oh My Zsh updates and custom plugin updates are separate. When an update is requested, use `omz update` in an initialized interactive Zsh for the framework. For each custom plugin, inspect its Git remote and working tree first; if the checkout is clean and its upstream is correct, use `git -C /absolute/plugin/path pull --ff-only`. Record the previous commit before updating. Stop on local changes or divergent history rather than resetting them.

If a new terminal fails to start normally, launch `zsh -f` to bypass user startup files, restore the timestamped `.zshrc` backup, run `zsh -n /absolute/path/to/.zshrc`, then test a fresh interactive session. If there was no original startup file, remove only the added configuration block. Do not delete the user's shell history or other configuration while recovering.

## tmux

1. Check for `tmux` before installing it.
2. If missing, select the command from the detected platform:
   - macOS with Homebrew: `brew install tmux`
   - Debian or Ubuntu: `sudo apt-get install tmux`
   - Fedora: `sudo dnf install tmux`
   - Arch Linux: `sudo pacman -S tmux`
3. If `~/.tmux.conf` does not exist, copy the baseline from [`../assets/dotfiles/tmux.conf`](../assets/dotfiles/tmux.conf).
4. If it exists, show a diff and merge only the requested settings. Never replace it silently.
5. Validate the candidate in an isolated tmux server using the procedure below before loading it into a user's session.

### Install, validate, and apply the configuration

Check `tmux -V`. On macOS, confirm `command -v brew` before using Homebrew; if it is absent, resolve the package-manager prerequisite first. Do not silently install a second package manager.

From the skill repository root, copy the asset to a temporary candidate file, or merge it with the existing configuration into that candidate. Back up an existing `~/.tmux.conf` before applying the reviewed candidate. The asset enables mouse support, quiet notifications, 256-color terminal behavior, and modern key/passthrough features.

Validate with a unique server name and a live temporary session:

```bash
setup_socket="setup-skill-$$"
tmux -L "$setup_socket" -f /absolute/path/to/candidate.conf \
  new-session -d -s validation /bin/sleep 60
tmux -L "$setup_socket" source-file /absolute/path/to/candidate.conf
tmux -L "$setup_socket" show-options -g mouse
tmux -L "$setup_socket" show-options -g default-terminal
tmux -L "$setup_socket" kill-server
```

Inspect startup output/messages for configuration errors; successful server startup alone is insufficient. If the installed tmux rejects `allow-passthrough`, `extended-keys`, or `terminal-features`, upgrade tmux or omit unsupported optional settings from the candidate and repeat validation. Never kill the user's existing tmux server during verification.

Check that the temporary server is reachable before running later commands. If even `/dev/null` as the configuration cannot start an isolated server, report an environment/runtime validation failure and stop; it does not establish that the asset is invalid. An explicit `source-file` makes configuration errors visible to the validating client.

If no config exists, copy the reviewed candidate to `~/.tmux.conf`. Otherwise apply the reviewed merge. To reload an existing session, use `tmux source-file "$HOME/.tmux.conf"`; terminal/key changes may require a new session. Test mouse pane selection and resizing. Recover by restoring the saved file and reloading it.

The stored `xterm-256color` value preserves the owner's preference. For another machine, check `infocmp tmux-256color` and the remote host's terminfo before choosing a different terminal type. See the [tmux FAQ](https://github.com/tmux/tmux/wiki/FAQ).

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

### Configure and verify SSH access

Check `git --version`, `ssh -V`, `ssh-add -l`, and `ls -la "$HOME/.ssh"` when the directory exists. An absent agent or empty key list is a setup condition, not proof that no key exists. Inspect only public keys with `ssh-keygen -lf /path/to/key.pub`.

For a new key, replace the example comment with the user's chosen value and confirm that neither destination file exists:

```bash
mkdir -p "$HOME/.ssh"
chmod 700 "$HOME/.ssh"
ssh-keygen -t ed25519 -C 'YOUR_GITHUB_EMAIL' -f "$HOME/.ssh/id_ed25519_github"
```

Let the user enter a passphrase in the interactive prompt. Do not put it in shell arguments or record it. Record the new key's fingerprint, not its private contents.

Reuse the current SSH agent when available; start one with `eval "$(ssh-agent -s)"` only if needed. Add the selected key:

- macOS: `ssh-add --apple-use-keychain "$HOME/.ssh/id_ed25519_github"` to store the chosen passphrase in Keychain, if desired; use ordinary `ssh-add` if persistence is not wanted.
- Linux: `ssh-add "$HOME/.ssh/id_ed25519_github"`. Agent persistence depends on the desktop/session manager; do not promise persistence across logins.

Merge a GitHub block into `~/.ssh/config`, checking existing `Host github.com` and `Host *` rules first. Replace the IdentityFile with the actual selected key:

```sshconfig
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_github
  AddKeysToAgent yes
  IdentitiesOnly yes
```

On macOS, add `UseKeychain yes` within this block only if Keychain persistence is wanted. Do not add that Apple-specific option on Linux. Keep config permissions at `600`; do not modify unrelated hosts or discard existing multi-account aliases.

Copy the `.pub` file's contents into GitHub **Settings → SSH and GPG keys → New SSH key**, choosing an authentication key. The user may perform this account action themselves. Check the server fingerprint against [GitHub's published fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints) before accepting an unfamiliar host key.

Configure the chosen Git identity (use `--local` inside a project if a global identity is unwanted):

```bash
git config --global user.name 'YOUR_NAME'
git config --global user.email 'YOUR_CHOSEN_EMAIL'
git config --global --get user.name
git config --global --get user.email
ssh -T git@github.com
```

A successful GitHub response identifies the account and says shell access is unavailable; exit status `1` is expected. On `Permission denied (publickey)`, check `ssh-add -l`, `ssh -G github.com` for the selected identity, and that the matching public key belongs to the intended account. Never disable host-key checking to resolve a failure. For a repository check, use `git ls-remote git@github.com:OWNER/REPOSITORY.git` with a real repository the user can access.

Recovery: restore the saved SSH config, remove a newly added agent identity with `ssh-add -d /path/to/key`, and ask before removing a key from GitHub or deleting local key files.

Official source: [GitHub SSH key setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
