# macOS system settings reference

Snapshot source: macOS 26.6.2 on Apple silicon. This file records selected behavior preferences observed on the owner's Mac. It intentionally excludes Apple ID and account data, Wi-Fi and network configuration, Keychain data, privacy permissions, recent items, input history, application lists, file paths, window positions, analytics timestamps, and opaque system state.

Use these values as a comparison checklist on a new Mac. Do not apply them automatically: preference keys and effects can change between macOS releases, and some settings require an application or session restart.

## Appearance and desktop behavior

- Appearance is set to **Auto**. The snapshot was captured while Dark appearance was active; `AppleInterfaceStyle = Dark` is the current state, while `AppleInterfaceStyleSwitchesAutomatically = 1` is the persistent preference.
- Double-clicking a window title bar maximizes the window rather than minimizing it.
- Scroll bars appear while scrolling.
- Activating an application does not automatically switch to a Space containing one of its open windows.
- The menu bar is not configured to remain hidden.

## Language, region, and time

- Preferred languages: English (United States), followed by Simplified Chinese.
- Locale: `en_US`.
- Time uses the 24-hour clock.
- Temperature is displayed in Celsius.
- General measurement units are configured as US/inches rather than metric.

These regional choices may be personal or location-dependent. Ask before reproducing them on another Mac.

## Keyboard and text input

- Key repeat delay: `InitialKeyRepeat = 25`.
- Key repeat rate: `KeyRepeat = 6`.
- Press-and-hold for accented characters is disabled, allowing keys to repeat.
- Automatic capitalization, spelling correction, period substitution, smart dashes, smart quotes, and text completion are enabled.
- Enabled typing methods include the U.S. keyboard and Simplified Chinese Pinyin; Pinyin was active when inspected.
- The Fn/Globe key behavior is stored as `AppleFnUsageType = 2`.

Do not preserve learned dictionaries, text replacements, spelling history, or recent input-source history in the skill.

## Pointer and trackpad

- Natural scrolling is enabled at the macOS level.
- Mouse tracking speed: approximately `0.875`.
- Trackpad tracking speed: `1`.
- Tap to click is enabled.
- Two-finger secondary click is enabled.
- Force Click is enabled at the global level, while the device preference reports Force Click suppression; verify the actual UI behavior before reproducing it.
- Pinch, rotate, horizontal scrolling, momentum scrolling, Mission Control/App Exposé swipes, and the two-finger Notification Center gesture are enabled.
- Three-finger drag and three-finger tap are disabled.
- Connecting a USB mouse does not disable the trackpad.

Scroll Reverser supplies the device-specific exception: keep natural scrolling for the trackpad and reverse only the external mouse.

## Dock

- Automatically hide and show the Dock.
- Dock magnification is enabled, with a stored magnified size of `93`.
- Minimize windows into the application icon.
- Group App Exposé windows by application.
- Use the Genie minimize effect.

The pinned Dock application order is deliberately excluded because it is machine- and workflow-specific.

## Finder and screenshots

No clear portable overrides were found for hidden files, path bar, status bar, default view style, new-window target, screenshot location, or screenshot format. Leave those at the new Mac's defaults unless the owner later adds explicit preferences.

## Control Center

- Battery, Clock, Focus, Sound, and Wi-Fi are visible in Control Center.
- Most individual controls are not separately pinned to the menu bar.

Item positions and migration state are excluded because they are implementation details rather than meaningful setup preferences.

## Maintenance

When refreshing this document:

1. Read relevant preference domains without changing them.
2. Compare behavioral keys, not the entire raw plist.
3. Exclude paths, identifiers, accounts, histories, cached state, window geometry, timestamps, and binary/opaque values.
4. Explain the corresponding System Settings behavior whenever known.
5. Record the macOS version used for the snapshot.
