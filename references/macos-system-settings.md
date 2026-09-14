# macOS system settings reference

Snapshot source: macOS 26.6.2 on Apple silicon. This file records selected behavior preferences observed on the owner's Mac. It intentionally excludes Apple ID and account data, Wi-Fi and network configuration, Keychain data, privacy permissions, recent items, input history, application lists, file paths, window positions, analytics timestamps, and opaque system state.

Use these values as a comparison checklist on a new Mac. Do not apply them automatically: preference keys and effects can change between macOS releases, and some settings require an application or session restart.

## Verified automatic behaviors

The following were checked separately so that a current state is not confused with an automatic preference:

- **Appearance: Auto.** Confirmed by `AppleInterfaceStyleSwitchesAutomatically = 1`. `AppleInterfaceStyle = Dark` only records that Dark appearance was active at inspection time.
- **Spelling language: Automatic.** Confirmed by `KB_SpellingLanguageIsAutomatic = 1`.
- **Software update checks: Automatic.** `softwareupdate --schedule` reports that automatic checking is on. This does not prove that automatic download or installation is enabled, so those are not recorded as enabled.
- **Dock hiding: Automatic.** `com.apple.dock autohide = 1`.
- **Screen saver: Automatic after 20 minutes.** The current-host idle time is `1200` seconds.
- **Text assistance:** automatic capitalization, spelling correction, smart period, smart dash, smart quote, and text completion behaviors are enabled individually.

The following are explicitly **not** automatic:

- The menu bar is not set to hide automatically (`_HIHideMenuBar = 0`).
- Switching to an application does not automatically move to a Space containing one of its windows (`AppleSpacesSwitchOnActivate = 0`).
- Recent applications are not shown automatically in the Dock (`show-recents = 0`).

## Appearance and desktop behavior

- Appearance is set to **Auto**; see the verified automatic behaviors above.
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
- Spelling-language selection is automatic.
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
- Do not show recently used applications in the Dock.

The pinned Dock application order is deliberately excluded because it is machine- and workflow-specific.

## Finder and screenshots

No clear portable overrides were found for hidden files, path bar, status bar, default view style, new-window target, screenshot location, or screenshot format. Leave those at the new Mac's defaults unless the owner later adds explicit preferences.

The screen saver is configured to start after 20 minutes of inactivity.

## Control Center

### Menu bar

- The menu bar does not hide automatically (`_HIHideMenuBar = 0`).
- The clock is digital, uses 24-hour time, shows the day of the week, and does not show the date.
- The Control Center menu-bar item is visible.
- AirDrop, Displays, Screen Mirroring, Stage Manager, and Fast User Switching are not separately visible in the menu bar.
- No explicit `BatteryShowPercentage` preference was found, so battery-percentage display is not claimed as on or off.

### Control Center

- Battery, Clock, Focus, Sound, and Wi-Fi modules are enabled in the stored Control Center visibility state.
- Item positions are not preserved because they are layout state rather than portable behavior.

Item positions and migration state are excluded because they are implementation details rather than meaningful setup preferences.

## Maintenance

When refreshing this document:

1. Read relevant preference domains without changing them.
2. Compare behavioral keys, not the entire raw plist.
3. Exclude paths, identifiers, accounts, histories, cached state, window geometry, timestamps, and binary/opaque values.
4. Explain the corresponding System Settings behavior whenever known.
5. Record the macOS version used for the snapshot.
