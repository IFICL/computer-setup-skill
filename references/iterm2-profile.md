# iTerm2 settings reference

The user installs iTerm2 manually. The skill does not install or update the application.

## Repository snapshot

[`../assets/iterm2/com.googlecode.iterm2.plist`](../assets/iterm2/com.googlecode.iterm2.plist) is a sanitized export of the complete `com.googlecode.iterm2` preferences domain from iTerm2 3.6.11. It includes global preferences and every regular profile, but not runtime caches, saved session databases, Keychain items, or the separate “All Settings and Data” recovery archive. The source machine's fixed working directory has been removed so that another Mac uses its normal default directory behavior.

See [iterm2-default-diff.md](iterm2-default-diff.md) for the audited differences between its Default profile and the factory profile bundled with that iTerm2 version.

## Refresh the preferences snapshot

Quit iTerm2 or avoid editing settings while exporting, then run:

```bash
defaults export com.googlecode.iterm2 assets/iterm2/com.googlecode.iterm2.plist
plutil -lint assets/iterm2/com.googlecode.iterm2.plist
```

## Export one reference profile

In iTerm2:

1. Open **Settings → Profiles**.
2. Select the profile to preserve.
3. Open **Other Actions** beneath the profile list.
4. Choose **Save Profile as JSON**.
5. Save the exported file under `assets/iterm2/` in this skill repository.

Export only the selected profile, not all iTerm2 settings and data. A single profile is easier to inspect, maintain, and reuse.

## Review before committing

Inspect the JSON for values that may not work on another Mac, including:

- absolute paths and custom startup commands;
- usernames, hostnames, SSH destinations, badges, and working directories;
- fonts or color presets that are not installed;
- profile GUIDs and keyboard shortcuts;
- triggers, coprocesses, and captured-output actions.

Do not commit credentials or other secrets. Keep a setting when it represents an intentional preference; document or remove it when it is tied only to the source machine.

Do not restore a fixed profile working directory unless the user explicitly requests one. The checked-in reference intentionally omits `Working Directory`.

## Use on another Mac

Treat the exported settings as a reference. Before import, explain any unavailable fonts, paths, commands, or shortcut conflicts. Do not import it or replace the user's settings without explicit approval.

For a Dynamic Profile, generate a new GUID rather than reusing the GUID of an existing regular profile. Dynamic Profiles can be placed in `~/Library/Application Support/iTerm2/DynamicProfiles/`, but copying a file there changes live application configuration and therefore requires explicit approval.
