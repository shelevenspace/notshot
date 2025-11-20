## v1.4 (clicky)
- Depreciated verbosity (`--verbose`). It will still function for now but some features may lack verbosity and the feature may be removed altogether in a future version.
- Fixed an impending error with notification icons making no notification appear whatsoever.

## v1.3.2
- Adjusted wording of some code, removed some extraneous spaces

## v1.3.1
- Fixes issue with escaping a forbidden character in the code.
- Refactors function to be directly in code.

## v1.3 (bookkeeper)
- Flipped image name from `process + time` to `time + process`. This will not affect functionality, only how file browsers sort A-Z.
    - Added an option to use the v1.2 `process + time` if you wish.
- Changed how the window title is processed to solve issues relating to spaces in window titles. If a window has spaces, the program will now record only the first word.
- Now removes forbidden characters from image name (`< > : " \ / | ? *`).
- Made errors more readable to normal people.
- Created a changelog file.
- Adds `--oldnamescheme` argument to revert image filenames back to the format used in v1.2 and earlier.

## v1.2 (eager multilingual)
- This update was something I should have added earlier, but here it is. Adds support for Pillow's image formats, see the readme for the chart. Also adds the option to capture the active window instead of asking you to pick a window.
- Adds `--format` (`-f`) argument to specify a format. If you choose one that isn't supported, it will not save and will give you a PNG in /tmp instead.
- Adds  `--active` (`-a`) argument to quickly capture the currently focused window, or the desktop if there is none.

## v1.1 (noisy)
- Adds native notification pushing on capture or error. This is very useful when you capture via shortcut key as no terminal opens and you have no way of knowing if it actually worked. Now you do!
- Adds `--quiet` (`-q`) argument to silence notifications.

## v1.0-mvp
- First release, with the basic features I wanted out of a screenshot tool. I have plans to add more, but this is fully functional and usable as it is now. Run with your equivalent of `python3 /path/to/notshot.py`.