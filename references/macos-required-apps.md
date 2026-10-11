# Required macOS applications

This is the owner's evolving list of applications to install on a Mac. Keep entries concise and practical. For each addition, record its purpose, typical usage, official source, installation notes, and permissions or paid features that affect setup.

Do not install an application merely because it appears here. Check whether it is already installed, verify current compatibility from the official source, and obtain approval before downloading or installing software.

## Installation and verification workflow

1. Check `/Applications` and `~/Applications` for the requested app; confirm its version through **About** rather than reinstalling an existing copy.
2. Open its official download page and select a build compatible with the current macOS version and processor. Compatibility statements below are historical observations, so check them again at installation time.
3. For a DMG, mount it and drag the app to `/Applications`; for a ZIP, extract it and move the app there. Resolve an existing app conflict before replacing it. iTerm2 installation is performed by the owner.
4. Launch the app, let the user complete sign-in or license activation, and grant only required permissions. Use the official installer and macOS verification flow; do not bypass security checks.
5. Perform each entry's first-run setup and verify the behavior listed below. Record unavailable features or steps awaiting user action.

| App | Successful setup check |
|---|---|
| BetterDisplay | Select the actual monitor and verify one supported brightness or resolution adjustment; restore the original value after the test. |
| Scroll Reverser | Test mouse wheel and trackpad independently; trackpad stays natural while the mouse uses the chosen reverse direction. |
| iTerm2 | Open a new tab; verify Zsh, plugin loading, and reference appearance/shortcuts if settings were imported. |
| VS Code | `code --version` works and `code .` opens a chosen test folder. |
| Cursor (optional) | Open a chosen test folder and verify editing; check sign-in/indexing only if AI features were requested. |
| ChatGPT | Launch, confirm the intended account, and send a harmless test prompt; test the launcher shortcut if configured. |

## BetterDisplay

- **Official site:** [betterdisplay.pro](https://betterdisplay.pro/en/)
- **Purpose:** Improves control over built-in and external displays beyond the standard macOS display controls.
- **Typical usage:** Choose scaled or custom HiDPI resolutions; control external-display brightness and volume when the display supports DDC; synchronize brightness across displays; manage refresh rate, rotation, color modes, display connection state, and virtual displays.
- **Why it is useful:** Especially helpful with third-party monitors, TVs, headless Macs, remote access, or display setups where macOS does not expose the desired resolution and hardware controls.
- **After installation:** Open it from the menu bar, select each display, then configure only the features the display supports. Start with resolution and brightness controls before using advanced EDID, HDR/XDR, color, or virtual-screen overrides.
- **Important notes:** Free and Pro capabilities differ, and hardware-dependent features vary by Mac, macOS version, display, and connection. Download only from the official site or its linked GitHub repository because the developer warns about lookalike download sites.

## Scroll Reverser

- **Official site:** [pilotmoon.com/scrollreverser](https://pilotmoon.com/scrollreverser/)
- **Purpose:** Controls scroll direction independently for a trackpad, mouse, and Magic Mouse.
- **Typical usage:** Keep macOS Natural Scrolling for the trackpad while using traditional wheel direction for an external mouse. It can also adjust wheel step size instead of relying on macOS scroll acceleration.
- **Recommended configuration:** Enable Natural Scrolling in macOS, leave **Reverse Trackpad** off, and turn **Reverse Mouse** on. Enable **Start at Login** if the behavior should be persistent.
- **After installation:** Move the app to `/Applications`, launch it, and grant Accessibility/Input Monitoring access when macOS requests it. If enabling the app has no effect, remove and re-add it under macOS Privacy & Security permissions.
- **Important notes:** The current release listed by the official site requires macOS 13.5 or later and supports Intel and Apple silicon. It reverses scroll events, not swipe gestures, and does not affect custom gesture-based scrolling in every app.

## iTerm2

- **Official site:** [iterm2.com](https://iterm2.com/)
- **Purpose:** Replaces the built-in Terminal app with a more configurable terminal for local shells, SSH sessions, and command-line development.
- **Typical usage:** Run Zsh and tmux, split a tab into multiple panes, search terminal output, maintain separate profiles, and use Shell Integration for prompt marks, command status, directory history, and profile switching.
- **Recommended configuration:** Use the sanitized settings snapshot at [`../assets/iterm2/com.googlecode.iterm2.plist`](../assets/iterm2/com.googlecode.iterm2.plist) as a reference. Review [iterm2-profile.md](iterm2-profile.md) and [iterm2-default-diff.md](iterm2-default-diff.md) before importing it.
- **After installation:** Set the default profile to use the login shell. Enable automatic Shell Integration only if its dotfile behavior is wanted. Confirm that the configured font is available and that Option–Left/Right moves by word as expected.
- **Important notes:** The owner installs iTerm2 manually. Importing the stored settings can change global preferences, profiles, keyboard mappings, appearance, and terminal behavior, so do not import them without explicit approval.

## Visual Studio Code

- **Official site:** [code.visualstudio.com](https://code.visualstudio.com/)
- **Purpose:** Primary general-purpose editor for source code, configuration files, Git work, debugging, and remote development.
- **Typical usage:** Open a project folder, edit and search across the workspace, use integrated Git and terminal features, and install language-specific extensions only as needed.
- **Recommended configuration:** Keep the extension set project-driven instead of installing a large universal bundle. Turn on Settings Sync only when the user wants editor settings and extensions associated with the selected account.
- **After installation:** Move the app to `/Applications`. Open the Command Palette with `⇧⌘P` and run **Shell Command: Install 'code' command in PATH**, then verify that `code .` opens the current directory.
- **Important notes:** Core editor functionality does not require sign-in. Remote SSH, dev containers, language tooling, and AI features may require separate extensions, accounts, runtimes, or permissions.

## Cursor (optional)

- **Official site:** [cursor.com](https://cursor.com/)
- **Purpose:** Optional AI-focused code editor for codebase-aware questions, assisted editing, and agent-based coding workflows.
- **Typical usage:** Open an existing repository, let indexing finish, ask questions about the codebase, and review proposed edits and command execution before accepting them.
- **Recommended configuration:** Import VS Code settings only when matching editor behavior is desired. Keep VS Code as the baseline editor and install Cursor when its AI workflow provides a clear benefit.
- **After installation:** Download the correct macOS build, drag Cursor to `/Applications`, complete onboarding, and optionally install its shell command. Review codebase-indexing and privacy choices before opening sensitive repositories.
- **Important notes:** Cursor is optional and overlaps substantially with VS Code. AI functionality may require an account and may have plan-dependent limits. Avoid duplicating every extension and setting unless both editors are actively used.

## ChatGPT

- **Official site:** [chatgpt.com/download](https://chatgpt.com/download/)
- **Purpose:** Desktop access to ChatGPT for general assistance, research, writing, files, screenshots, coding work, and Codex tasks.
- **Typical usage:** Use the desktop app for conversations and files, invoke the Chat Bar for quick questions, and use Work or Codex when the task needs access to connected work context or a local coding workspace.
- **Recommended configuration:** Sign in to the intended account, review notification and data controls, and grant only the permissions required for features the user plans to use.
- **After installation:** Move the app to `/Applications`, sign in, and test its launcher shortcut. Enable access to screenshots, microphone, or supported apps only when those workflows are wanted.
- **Important notes:** The current ChatGPT desktop app requires macOS 14 or later and supports Apple silicon and Intel Macs. Account features and available tools can vary by plan and workspace policy.

## Maintenance format

Add future applications using the same fields:

```markdown
## Application name

- **Official site:** URL
- **Purpose:** What problem it solves.
- **Typical usage:** How the owner uses it.
- **Recommended configuration:** The important non-default choices.
- **After installation:** Permissions or first-run actions.
- **Important notes:** Compatibility, license, limitations, or risks.
```
