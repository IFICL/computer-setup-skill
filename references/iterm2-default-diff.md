# iTerm2 settings analysis

Baseline: `DefaultBookmark.plist` bundled with iTerm2 3.6.11. Current source: the profile named `Default` in `assets/iterm2/com.googlecode.iterm2.plist`.

This is a semantic summary rather than a raw plist diff. Fields absent from the saved profile commonly inherit behavior from iTerm2 and are not automatically user changes.

## Significant Default profile changes

| Area | Factory default | Current setting |
|---|---|---|
| Window grid | 80 columns × 25 rows | 100 columns × 35 rows |
| Font | Monaco 12 | Monaco 13.5 |
| Terminal type | `xterm` | `xterm-256color` |
| Background | light/dark adaptive defaults | black, P3 color space |
| Foreground | adaptive dark text/light text | approximately 73% gray |
| Transparency | 0 | approximately 49.9% |
| Blur | off | on, radius approximately 20.31 |
| Cursor blink | off | on |
| Scrollback | 1,000 lines, limited | unlimited |
| Option key | normal behavior | sends escape/meta |
| Initial directory | unspecified | omitted from the sanitized skill asset |
| Close confirmation | factory behavior | “Prompt Before Closing” disabled |

The profile also replaces the full ANSI 16-color palette with the classic evenly spaced terminal palette, changes selection/cursor colors, and does not store separate light- and dark-mode palettes.

## Custom key mappings

Two profile mappings are present:

- Option–Left sends Escape followed by `b`, which moves backward one word in common shells.
- Option–Right sends Escape followed by `f`, which moves forward one word in common shells.

These mappings align with `Option Key Sends = Esc+` and are intentional, portable shell-navigation preferences.

## Global preferences worth preserving

- Automatic updates are enabled.
- Tabs are hidden when the layout does not need them.
- Clipboard access is enabled.
- macOS window tabbing is set to manual.
- No dedicated global hotkey window is enabled, although migrated hotkey metadata remains stored.
- iTerm2 AI options target the OpenAI Responses endpoint and select `gpt-5.5`; no API key or token was found in this plist export.

## Machine-specific and noisy values

The exported plist contains window frame coordinates, update UI state, onboarding/migration flags, and recent navigation state. These are not good reusable defaults. The source profile originally fixed its working directory to `/Users/czyang`; that field has been removed from the skill asset.

For cross-machine use, consider producing a second curated profile containing only visual, terminal, scrollback, and keyboard preferences. Keep the full preferences plist as a personal recovery reference rather than applying it automatically.
