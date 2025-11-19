# notShot

notShot is a screenshot utility made for Linux Mint Cinnamon.

## Prerequisites

- Python 3.12.3
- xdotool + xwininfo (`# apt install xdotool`)
- Be using an X Window system. Wayland isn't supported.

> [!NOTE]
> If you aren't on Linux Mint Cinnamon or something is acting up, you may need to install the specific versions of the prerequisites, listed below. <sup>*Remember to simulate with `$ apt -s` before changing your system!*</sup>
>- Python - 3.12.3
>- xdotool + xwininfo - 3.20160805.1
>- Pillow - 10.2.0

## Using notShot

Executing the script without arguments will cause it to wait for you to click a window. It will then capture an image of that window and save it.

By default, notShot will save captures to the folder `~/Pictures`, inside its own folder structure. It will organize the images within a folder for each month, then append the day onto the image filename itself.

Example: `~/Pictures/notShot/2025-10/09-image.png`

## Arguments

| Arg | Arg-long        | Req | Default     |
| --- | --------------- | --- | ----------- |
| -h  | --help          | no  |             |
| -v  | --verbose       | no  | false       |
| -s  | --seeimage      | no  | false       |
| -n  | --nostruct      | no  | false       |
| -q  | --quiet         | no  | false       |
| -a  | --active        | no  | false       |
|     | --dry           | no  | false       |
|     | --oldnamescheme | no  | false       |
| -f  | --format        | no  | png         |
| -o  | --output        | no  | ~/Pictures/ |

- `--help` - Shows all available arguments and what they do, then quits
- `--verbose` - The program will display quite a lot of information about what it's up to and what it understands.
- `--seeimage` - The captured image will open in your default image viewer.
- `--nostruct` - Instead of creating the folder structure (`(path)/notshot/yyyy-mm/`), just save the image directly to the specified directory.
- `--quiet` - Don't show a notification on finished save.
- `--active` - Instead of clicking on a window to capture, just capture the currently active window and save that.
- `--dry` - Only use `/tmp` and don't actually save the image.
  - *This will disregard `--format` and produce a png when using `--seeimage` as well.*
- `--oldnamescheme` - Write filenames as `process + time` instead of `time + process`, like in v1.2 and earlier.
- `--format` - Use a specified format instead of `png`. See the [format support](#format-support) section for choices.
- `--output` - If you specify an output directory, notShot will create its folder structure there instead and then save the file.

## Example usage

- `notshot.py`
  - After clicking a window, saves an image of it to `~/Pictures/notShot/yyyy-mm/dd-filename.png`.
- `notshot.py -s`
  - After clicking a window, saves an image of it to `~/Pictures/notShot/yyyy-mm/dd-filename.png` and opens it in your default viewer.
- `notshot.py -asn -o ~/Desktop/`
  - Immediately saves image of the active window to `~/Desktop/dd-filename.png` and opens it in your default viewer.

## How to have notShot handle screenshots via hotkey
If you want to use notShot to take your screenshots instead of what you already have, you have to go through a couple steps, but it isn't complicated.

1. Make a new file in a location you have access to. I suggest your home folder (`~`). Name it something memorable, like `Launch-notShot.sh`.
2. Add the following, replacing the placeholders, into the file:
```sh
#!/bin/bash
cd /the/path/to/notshot.py
python3 notshot.py
```

> [!TIP]
> You can add `-a` to the end of the third line, like `python3 notshot.py -a` if you'd like to have it quickly capture the active screen instead of waiting for you to click.


3. Save the file and make it executable. You can do this by right-clicking the file, clicking Properties, Permissions, and checking `Allow executing file as a program`.
4. Open the Cinnamon menu (click it, or press the Windows / `Super` key) and search `Keyboard`. Open it and click the `Shortcuts` tab.
5. Search `Take a screenshot`, click the `Print` keyboard binding, and press `Backspace` to clear it. 
6. On the bottom, click `Add custom shortcut`. Name it something memorable, like `notShot screenshot`.
7. Click the button on the `Command:` line that says `(None)` with a folder icon. Find the file you just created, select it, and click the `Open` button in the dialog.
8. Click `Add` to create the shortcut.
9. In the `Keyboard Bindings` section, click any of the `unassigned` entries and press the `Print Screen`, `Prt Sc`, or `Print` key, whatever it may be called for you.
10. You're done! Test your new shortcut. If you wish, you can assign some other key combo to invoke notShot.

## Format support

> [!WARNING]
> This assumes the default system-included installation of the Pillow framework on Linux Mint. No promises are made if you are running on another system or modify your installation's framework, as format support relies on that.

| Format   | Supported    | Format | Supported |
| -------- | ------------ | ------ | --------- |
| png      | yes, default | icns   | partial   |
| dds      | yes          | apng   | no        |
| eps      | yes          | blp    | no        |
| gif      | yes          | dib    | no        |
| jpeg     | yes          | im     | no        |
| jpeg2000 | yes          | msp    | no        |
| pdf      | yes          | palm   | no        |
| ppm      | yes          | pcx    | no        |
| sgi      | yes          | spi    | no        |
| tga      | yes          | xv     | no        |
| tiff     | yes          |        |           |
| webp     | yes          |        |           |

## Frameworks and tools used by this program

> [!IMPORTANT]
> These frameworks and tools are *not in the source nor distributed* and you must [download them yourself](#Prerequisites) to use this program. If you are using the standard Linux Mint Cinnamon distribution, ImageGrab is already installed.

- [ImageGrab](https://github.com/python-pillow/Pillow/) module from Pillow
- [xdotool](https://github.com/jordansissel/xdotool) from jordanissel

## The rest

- notShot will probably work on most X window system based desktop environments, but it is only tested under modern Linux Mint Cinnamon.

## License

notShot (c) 2025 by shelevenspace is licensed under CC BY-NC-SA 4.0 with Source Code Clarifications.

This project is licensed under a modified version of the CC BY-NC-SA 4.0. It includes important clarifications about how **source code is included** in its definitions.
Review the [License](LICENSE.txt) for details.