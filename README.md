# notShot

notShot is a screenshot utility made for Linux Mint Cinnamon.

## Prerequisites

- Python 3.12.3
- Be using an X Window system. Wayland isn't supported.
- xdotool + xwininfo (`# apt install xdotool`)

# Installing or Updating notShot

> [!CAUTION]
> Don't run scripts from the internet that you don't understand, even if you don't use sudo! Read these scripts first and see what they're going to do before you execute them.

> [!NOTE]
> If you're a first-time user, download both `setup.sh` and `update.sh` from the [Releases](https://github.com/shelevenspace/notshot/releases/latest) page.

**If you've already installed notShot before, skip to step 5.**
1. Open the folder containing `setup.sh` and `update.sh`. 
2. Make the files executable. You can do this by right-clicking the file, clicking Properties, Permissions, and checking `Allow executing file as a program`.
3. Open a terminal inside the folder. You can do this by right-clicking in your file browser's window and choosing `Open in Terminal`.
4. If you haven't already, install `xdotool`. See the command in the [prerequisites](#prerequisites) above.
5. Do one of the following.
    - If you are INSTALLING: Run the command `./setup.sh`. This will create the needed files for notShot, then hand off to the updater for you automatically.
    - If you are UPDATING: Run the command `./update.sh`. This will download the latest version, extract it (overwriting the copy installed), and clean up.

You're done! If you want to set up shortcuts, see [how to do so](#how-to-have-notshot-handle-screenshots-via-hotkey).

## Using notShot
Executing the script without arguments will cause it to wait for you to click a window. It will then capture an image of that window and save it.

By default, notShot will save captures to the folder `~/Pictures`, inside its own folder structure. It will organize the images within a folder for each month, then append the day onto the image filename itself.

Example: `~/Pictures/notShot/2025-10/09-image.png`

## How to have notShot handle screenshots via hotkey

> [!CAUTION]
> Don't run scripts from the internet that you don't understand, even if you don't use sudo! Read these scripts first and see what they're going to do before you execute them.

If you want to use notShot to take your screenshots instead of what you already have, you have to go through a couple steps, but it isn't complicated.

notShot includes two pre-made shortcut scripts to take screenshots based on your click (`launch-notshot.sh`), as well as immediately capturing the active window (`launch-notshot-instant.sh`). Here's how you use them:

1. By default, the updater places these files in `~/.notshot/notshot`. Navigate here and copy these files elsewhere, such as your home folder (`~`).
    - The reason you move them out of the default folder is because it prevents them from being changed if you update notShot and have customized them.
2. Make the files executable. You can do this by right-clicking them, clicking Properties, Permissions, and checking `Allow executing file as a program`.
3. Open the Cinnamon menu (click it, or press the Windows / `Super` key) and search `Keyboard`. Open it and click the `Shortcuts` tab.
4. Search `Take a screenshot`, click the `Print` keyboard binding, and press `Backspace` to clear it. 
5. On the bottom, click `Add custom shortcut`. Name it something memorable, like `notShot screenshot`.
6. Click the button on the `Command:` line that says `(None)` with a folder icon. Find the shortcut script you want, select it, and click the `Open` button in the dialog.
7. Click `Add` to create the shortcut.
8. In the `Keyboard Bindings` section, click any of the `unassigned` entries and press the `Print Screen`, `Prt Sc`, or `Print` key, whatever it may be called for you.
9. You're done! Test your new shortcut. If you wish, you can assign some other key combo to invoke notShot.

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

## Format support

> [!WARNING]
> This assumes the recommended installation of the Pillow framework on Linux Mint. No promises are made if you are running on another system or modify your framework, as format support relies on it.

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
> These frameworks and tools are *not in the source nor distributed* and you must [download them](#installing-notshot) to use this program.

- [ImageGrab](https://github.com/python-pillow/Pillow/) module from Pillow
- [xdotool](https://github.com/jordansissel/xdotool) from jordansissel

> [!NOTE]
> If you aren't on Linux Mint Cinnamon or something is acting up, you may need to install the specific versions of the prerequisites, listed below. <sup>*Remember to simulate with `$ apt -s` before changing your system!*</sup>
>- Python - 3.12.3 (apt)
>- xdotool + xwininfo - 3.20160805.1 (apt)
>- Pillow - 10.2.0 (pip3)

## The rest

- notShot will probably work on most X window system based desktop environments, but it is only tested under modern Linux Mint Cinnamon.
- If you aren't going to use xdotool much outside of this, it may be wise to block potential updates with `# apt hold xdotool`. While breaking feature changes aren't likely, it's better safe than sorry.

## License

notShot (c) 2025 by shelevenspace is licensed under CC BY-NC-SA 4.0 with Source Code Clarifications.

This project is licensed under a modified version of the CC BY-NC-SA 4.0. It includes important clarifications about how **source code is included** in its definitions.
Review the [License](LICENSE.txt) for details.
