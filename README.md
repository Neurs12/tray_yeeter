# Tray yeeter
A Python tool to yeet your windows.

## Installation
1. Download the [latest release build](https://github.com/Neurs12/tray_yeeter/releases/).
2. Extract and run `tray_yeeter.exe`.
3. A notification should pop up, indicates that the process has started successfully.

## Edit hotkey
- All keys are based off of [virutal key codes](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes).
- To edit a hotkey, open `config.json` in the same folder with `tray_yeeter.exe`. It will look something like this:
```json
{
    "hotkeys": {
        "yeet": "f1",
        "yeet_all": "f11",
        "unyeet": "f2",
        "unyeet_all": "f12"
    }
}
```
- Now, let's change yeet hotkey to `window + x`:
    1. Lookup `window` key code, we get `VK_LWIN` and `VK_RWIN`.
    2. Remove `VK_` prefix and remove any indicator that the key is left `L` or right `K`.
    3. Now we got `win`.
    4. Follow up by that is an `x`, so we will add an extra `+` to seperate between those keys.
    5. And the final result is `win+x`.
- Apply it to our config:
```json
{
    "hotkeys": {
        "yeet": "win+x",
        "yeet_all": "f11",
        "unyeet": "f2",
        "unyeet_all": "f12"
    }
}
```
- Open system tray and find `Tray Yeeter`.
- Right click on it and press `Reload`.
- It will reload the whole program and show the notification again.

You can also combine multiple keys: `ctrl+shift+alt+3`, `shift+f5`, `shift+win+7`,... or even `h+i+d+e`.

Yes, normal keys also works.

## Start with Windows
1. Create a shortcut to `tray_yeeter.exe` we've extracted earlier.
2. Press `win + R`, then enter `shell:startup`, this should opens `Startup` folder.
3. Put the shortcut to `Startup` folder.

## Debug
Clone the repository and run the script.
