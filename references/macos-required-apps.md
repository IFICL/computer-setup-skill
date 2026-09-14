# Required macOS applications

This is the owner's evolving list of applications to install on a Mac. Keep entries concise and practical. For each addition, record its purpose, typical usage, official source, installation notes, and permissions or paid features that affect setup.

Do not install an application merely because it appears here. Check whether it is already installed, verify current compatibility from the official source, and obtain approval before downloading or installing software.

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
