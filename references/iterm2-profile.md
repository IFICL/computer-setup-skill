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

Run from the skill repository root. Export to a temporary candidate first when replacing the existing reference. Remove `Working Directory` from **every** item in `New Bookmarks`, inspect other machine-specific fields, then validate and replace the stored asset. Exporting again otherwise reintroduces the excluded source directory.

## Export one reference profile

In iTerm2:

1. Open **Settings → Profiles**.
2. Select the profile to preserve.
3. Open **Other Actions** beneath the profile list.
4. Choose **Save Profile as JSON**.
5. Save the exported file under `assets/iterm2/` in this skill repository.

Export only the selected profile, not all iTerm2 settings and data. A single profile is easier to inspect, maintain, and reuse.

## Review before committing

Inspect the exported plist or JSON for values that may not work on another Mac, including:

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

### Restore the full preferences domain

Use this when the user explicitly wants the whole stored preference set. The plist is not a profile JSON and cannot be imported through the single-profile menu. It also contains window geometry, migration state, and AI settings; discuss those differences before replacing the preference domain.

1. Record the installed iTerm2 version, compare it with the snapshot version, and confirm iTerm2 is installed. Check **General → Settings/Preferences** for a custom preferences folder: if enabled, determine the authoritative source before importing.
2. Export current preferences to a timestamped backup outside the skill asset directory:

   ```bash
   defaults export com.googlecode.iterm2 "/absolute/backup/path/iterm2-before.plist"
   plutil -lint "/absolute/backup/path/iterm2-before.plist"
   ```

3. Quit iTerm2 normally after saving active work. Use another terminal or the agent's shell for the remaining commands.
4. Validate the reference, then import it using an absolute path:

   ```bash
   plutil -lint "/absolute/skill/path/assets/iterm2/com.googlecode.iterm2.plist"
   defaults import com.googlecode.iterm2 "/absolute/skill/path/assets/iterm2/com.googlecode.iterm2.plist"
   ```

5. Reopen iTerm2. Verify font size, transparency, blur, 100×35 initial grid, word-navigation shortcuts, and normal starting directory in a new window. Check the resulting preferences as well as the visible behavior; version migrations may change stored values.
6. If needed, quit iTerm2 again, import `iterm2-before.plist`, and reopen it to roll back.

For a complete recovery archive including support files, use **Settings → General → Export/Import All Settings and Data** when that feature exists in the installed version. That archive is separate from this repository's plist. See [iTerm2 General preferences](https://iterm2.com/documentation-preferences-general.html).
