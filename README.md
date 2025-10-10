# notShot

notShot is a screenshot utility made for Linux Mint Cinnamon.

## Prerequisites

- Python 3.12.3
- xwininfo (`# apt install xdotool`)
- Be using an X Window system. Wayland isn't supported.

## Using notShot

Currently, executing the script will then wait for you to click a window. It will then capture an image of that window and save it.

By default, notShot will save captures to the folder `~/Pictures`, inside its own folder structure. It will organize the images within a folder for each month, then append the day onto the image filename itself.

Example: `~/Pictures/notShot/2025-10/09-image.png`

## Arguments

| Arg | Arg-long   | Req | default |
| --- | ---------- | --- | ------- |
| -h  | --help     | no  |         |
| -v  | --verbose  | no  | false   |
| -o  | --output   | no  |         |
| -s  | --seeimage | no  | false   |
| -n  | --nostruct | no  | false   |
| -q  | --quiet    | no  | false   |
|     | --dry      | no  | false   |

- `--help` - Shows all available arguments and what they do, then quits
- `--verbose` - The program will display quite a lot of information about what it's up to and what it understands.
- `--output` - If you specify an output directory, notShot will create its folder structure there instead and then save the file.
- `--seeimage` - The captured image will open in your default image viewer.
- `--nostruct` - Instead of creating the folder structure (`(path)/notshot/yyyy-mm/`), just saves the image directly to the specified directory.
- `--quiet` - Don't show a notification on finished save.
- `--dry` - Only use `/tmp` and don't actually save the image

## Example usage

- `notshot.py`
  - Saves image to `~/Pictures/notShot/yyyy-mm/dd-filename.png`.
- `notshot.py -s`
  - Saves image to `~/Pictures/notShot/yyyy-mm/dd-filename.png` and opens it in your default viewer (`--seeimage`).
- `notshot.py -vsnq -o ~/Desktop/ --dry`
  - Shows all actions the program is doing, opens the image after writing, skips making any folders, outputs to `~/Desktop/dd-filename.png`, and then doesn't do anything but `--verbose` and `--seeimage` because of `--dry` making it a test run. This means it will open the image out of `/tmp` , which is usually lost on reboot. It will also not notify you of anything.

## Other things used in this program

- ImageGrab module by Pillow

## How to have notShot handle screenshots via hotkey
If you want to use notShot to take your screenshots instead of what you already have, you have to go through a couple steps, but it isn't complicated.

1. Make a new file in a location you have access to. I suggest your home folder (`~`). Name it something memorable, like `Launch-notShot.sh`.
2. Add the following, replacing the placeholders, into the file:
```sh
#!/bin/bash
cd /the/path/to/notshot.py
python3 notshot.py
```
3. Save the file and make it executable. You can do this by right-clicking the file, clicking Properties, Permissions, and checking `Allow executing file as a program`.
4. Open the Cinnamon menu (click it, or press the Windows / `Super` key) and search `Keyboard`. Open it and click the `Shortcuts` tab.
5. Search `Take a screenshot`, click the `Print` keyboard binding, and press `Backspace` to clear it. 
6. On the bottom, click `Add custom shortcut`. Name it something memorable, like `notShot screenshot`.
7. Click the button on the `Command:` line that says `(None)` with a folder icon. Find the file you just created, select it, and click the `Open` button in the dialog.
8. Click `Add` to create the shortcut.
9. In the `Keyboard Bindings` section, click any of the `unassigned` entries and press the `Print Screen`, `Prt Sc`, or `Print` key, whatever it may be called for you.
10. You're done! Test your new shortcut. If you wish, you can assign some other key combo to invoke notShot.
