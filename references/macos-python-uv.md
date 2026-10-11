# Optional macOS Python environment with uv

Use this workflow when the owner requests their Python environment. Source of truth: [IFICL/my-uv-env](https://github.com/IFICL/my-uv-env), not a copied dependency list in this skill.

Inspected on 2026-10-11 at commit `5e21597`: `.python-version` selects Python 3.12, `pyproject.toml` requires Python >=3.12, and `uv.lock` is tracked. Runtime packages include NumPy, pandas, SciPy, scikit-learn, matplotlib, torch, torchvision, and tqdm. The default development group includes ipykernel, pytest, and ruff. Re-read these files at setup time because they may change.

## 1. Inspect prerequisites and choose a location

Check `uname -m`, `sw_vers`, `git --version`, `command -v uv`, and, if present, `uv --version`. Use a native shell for the Mac's architecture rather than mixing Rosetta and Apple-silicon packages unintentionally.

Use `~/my-uv-env` as the suggested checkout location, or the user's chosen directory. If that location exists, inspect its Git remote and working tree before reusing it. Do not clone over another project or discard local modifications. Private-repository access may require the SSH setup in [shared-setup.md](shared-setup.md).

## 2. Install uv if missing

If Homebrew is already available:

```bash
brew install uv
uv --version
```

Otherwise use the [official standalone installer](https://docs.astral.sh/uv/getting-started/installation/):

```bash
setup_tmp=$(mktemp -d)
curl -fL https://astral.sh/uv/install.sh -o "$setup_tmp/install-uv.sh"
# Inspect the downloaded installer, then run it after a successful download.
sh "$setup_tmp/install-uv.sh"
```

Follow its reported PATH instructions and open a new shell. If `uv` is still unavailable, check its reported installation directory (normally `~/.local/bin`). Merge the necessary PATH entry once into the active startup file; do not replace existing PATH configuration. Verify `command -v uv` and `uv --version` before proceeding. Use one installation method consistently.

## 3. Clone and synchronize

For a new checkout:

```bash
git clone git@github.com:IFICL/my-uv-env.git "$HOME/my-uv-env"
cd "$HOME/my-uv-env"
```

For an existing checkout, verify the remote is the intended repository and inspect `git status --short`. When updating is requested and the working tree is clean, use `git pull --ff-only`. Stop to resolve local changes or divergent history if necessary.

Inspect the current README, `.python-version`, `pyproject.toml`, and `uv.lock`, then run from the checkout:

```bash
uv sync --locked
```

This creates or synchronizes the project's `.venv`, includes the default development group, and refuses to update an out-of-date lockfile. uv can download a compatible Python when one is unavailable. Expect Python/package downloads and enough disk space for large packages such as PyTorch. Do not use `sudo` or modify the macOS system Python.

If the lockfile is missing or stale, explain the inconsistency before using `uv lock` or unlocked `uv sync`, because those can change the environment definition. If a package lacks a compatible macOS wheel or fails to build, report the package, Python version, and architecture; do not silently change dependency constraints or omit packages. The repository contains CPU/macOS packages; CUDA instructions for Linux do not apply. MPS availability depends on the actual Mac and installed PyTorch.

## 4. Verify and use the environment

Run without updating the lockfile:

```bash
uv run --locked python -c 'import sys; print(sys.version); print(sys.executable)'
uv run --locked myenv
uv run --locked python -c 'import numpy, pandas, scipy, sklearn, matplotlib, torch, torchvision, tqdm; print("Imports OK"); print("MPS available:", torch.backends.mps.is_available())'
git status --short
```

The interpreter should belong to this checkout's `.venv`, the project command currently prints `Hello from myenv!`, and imports should succeed. A false MPS result is not by itself a setup failure. Confirm that synchronization did not alter tracked environment files.

Manual activation in the current shell:

```bash
source .venv/bin/activate
python --version
deactivate
```

From another directory, use the actual checkout path:

```bash
uv run --locked --directory "$HOME/my-uv-env" python
```

### Activate automatically in new Zsh sessions

The owner wants this environment activated automatically. After `uv sync --locked` succeeds and `.venv/bin/activate` exists, back up the active Zsh startup file (`${ZDOTDIR:-$HOME}/.zshrc`) and merge the following block once, after Oh My Zsh and other environment initialization:

```zsh
# env
if [[ -f "$HOME/my-uv-env/.venv/bin/activate" ]]; then
    source "$HOME/my-uv-env/.venv/bin/activate"
fi
```

If the checkout uses a different location, substitute that actual path in both lines. Update an existing equivalent block rather than appending duplicates. Review any existing Conda, pyenv, or other automatic activation so that competing environment initialization does not override the selected interpreter.

Run `zsh -n "${ZDOTDIR:-$HOME}/.zshrc"`, then open a fresh Zsh terminal tab. Verify `echo "$VIRTUAL_ENV"` points to the checkout's `.venv` and `python -c 'import sys; print(sys.executable)'` uses its interpreter. The file guard allows the shell to start normally before the environment exists. `deactivate` leaves the environment for the current session; a new Zsh session activates it again.

Keep other projects' virtual environments separate: activate their own environment or use their `uv run` commands when working on them. In VS Code or Cursor, select this checkout's `.venv/bin/python` only for the workspace that should use it. For notebooks, select the corresponding Python environment/kernel; installing ipykernel does not automatically select it in the editor.

## 5. Maintain or recover

To reproduce a newly pulled definition, run `uv sync --locked` again. Exact synchronization can remove packages installed manually into `.venv`, so declare persistent dependencies with `uv add PACKAGE` or `uv add --dev PACKAGE` in the environment repository.

Dependency upgrades are a separate requested operation: `uv lock --upgrade` updates all permitted versions; `uv lock --upgrade-package PACKAGE` targets one package. Apply with `uv sync --locked`, verify imports, and review `pyproject.toml`/`uv.lock` changes. Commit or push only on explicit instruction.

Update uv through its installation method: `brew upgrade uv` for Homebrew, or `uv self update` for the standalone installer. Recheck `uv --version` afterward.

If `.venv` is damaged, first confirm its exact project path and move it to a timestamped backup, then rebuild with `uv sync --locked`. Keep project files, lockfile, and shared uv caches intact. Restore the backup if rebuilding fails. For dependency rollback, use the reviewed prior environment definition and synchronize it; do not reset a dirty checkout.

Official behavior reference: [uv locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/). The repository README remains authoritative for project-specific changes.
