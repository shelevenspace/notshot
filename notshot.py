# notShot (c) 2025 by shelevenspace
# This source code is licensed under the CC BY-NC-SA 4.0 with Source Code Clarifications. Review the LICENSE.txt for details.

from PIL import ImageGrab
import os
import sys
from datetime import datetime
import argparse
import subprocess
import pathlib

version = "1.3.3"

parser = argparse.ArgumentParser(
    prog="notShot",
    description="notShot screenshot utility version " + version
)
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help="(DEPRECATED) see unnecessary amounts of detail")
parser.add_argument('-n', '--nostruct', dest="nostructure", action="store_true", help="don't use notshot's folder structure and just save the file at the output location")
parser.add_argument('-s', '--seeimage', dest="seeimage", action="store_true", help="open the image in the default viewer after saving")
parser.add_argument('-q', '--quiet', dest="quiet", action="store_true", help="do not send notifications (this will suppress error notifications too)")
parser.add_argument('-a', '--active', dest="useactive", action="store_true", help="just capture the active window instead of waiting for you to click on something")
parser.add_argument('--dry', dest="dry", action="store_true", help="dry run (don't save anything but go through the motions)")
parser.add_argument('--oldnamescheme', dest="oldnamescheme", action="store_true", help="use the filename formatting from v1.2 (filename, then date)")
parser.add_argument('-f', '--format', default="png", type=str, dest="format", help="the format to save the image as (see readme). default: png")
parser.add_argument('-o', '--output', default="~/Pictures/", type=pathlib.Path, dest='directory', help="the directory to output to, including trailing forward slash. default: ~/Pictures/")
arg = parser.parse_args()

# figure out where the user wanted the image saved
if arg.verbose: print(f'verbose mode: {arg.verbose} / --output recieved: {arg.directory}')
arg.directory = os.path.expanduser(arg.directory) # this is needed if there is no `--output` provided whatsoever, else it fails to verify.
if arg.verbose: print(f'expanded: {arg.directory}')
arg.directory = str(arg.directory) + "/" # pathlib strips the trailing forward slash which is necessary to have for the final file output.
if arg.verbose: print(f'trailing added: {arg.directory}')

if os.path.exists(arg.directory) and not os.path.isfile(arg.directory) and os.access(arg.directory, os.W_OK) and arg.directory.endswith("/"):
    if arg.verbose: print(f'directory check passed (exists and writable)')
else:
    if not arg.quiet: subprocess.run(["/usr/bin/notify-send", "-u", "critical", "Invalid directory!", "Fatal (error 1) - Couldn't access specified directory\n\nYou didn't include a trailing forward slash, the specified directory doesn't exist, isn't writable, or you specified a file."])
    sys.exit("fatal (error 1) - You didn't include a trailing forward slash, the specified directory doesn't exist, isn't writable, or a file was specified.")

# capture the image and figure out where the window is on screen
try:
    if not arg.useactive: # ask for what to take image of with mouse click
        capturedid = subprocess.check_output(["/bin/bash", "-c", "xwininfo | awk '/Window id/ {print $4}'"]).decode("utf-8").strip()
        if arg.verbose: print(f'click caught, capturing information')
    else: # just capture the active window
        capturedid = subprocess.check_output(["/bin/bash", "-c", "xwininfo -id `xdotool getwindowfocus` | awk '/Window id/ {print $4}'"]).decode("utf-8").strip()
        if arg.verbose: print(f'active window caught, capturing information')
except Exception:
    sys.exit("fatal (error 2) - can't detect x window system or xwininfo isn't available")

geometryupleftx = int(subprocess.check_output(["/bin/bash", "-c", "xwininfo -id " + capturedid + " | awk '/Absolute upper-left X/ {print $4}'"]).decode("utf-8").strip())
geometryuplefty = int(subprocess.check_output(["/bin/bash", "-c", "xwininfo -id " + capturedid + " | awk '/Absolute upper-left Y/ {print $4}'"]).decode("utf-8").strip())
geometrywidth = int(subprocess.check_output(["/bin/bash", "-c", "xwininfo -id " + capturedid + " | awk '/Width/ {print $2}'"]).decode("utf-8").strip())
geometryheight = int(subprocess.check_output(["/bin/bash", "-c", "xwininfo -id " + capturedid + " | awk '/Height/ {print $2}'"]).decode("utf-8").strip())

# prepare the coordinates for imagegrab
if arg.verbose: print(f'id {capturedid}, geom ulx {geometryupleftx}, geom uly {geometryuplefty}, geom w {geometrywidth}, geom h {geometryheight}\nnow processing geometry')
postgeomleft = geometryupleftx # distance of top left corner from leftmost of screen(s)
postgeomupper = geometryuplefty # distance of top left corner from topmost of screen(s)
postgeomright = geometryupleftx + geometrywidth # distance of bottom right corner from leftmost of screen(s)
postgeomlower = geometryuplefty + geometryheight # distance of bottom right corner from topmost of screen(s)
if arg.verbose: print(f"window distance from left of screen {postgeomleft}\nwindow distance from top of screen {postgeomupper}\nwindow bottom distance from top of screen {postgeomright}\nwindow bottom right distance from left of screen {postgeomlower}\nnow capturing image")

# take picture
capture = ImageGrab.grab(bbox=(postgeomleft, postgeomupper, postgeomright, postgeomlower))
if arg.verbose: print(f"image captured")

# post-capture actions - try to do as little BEFORE capturing as possible to reduce delay between click and capture
processname = subprocess.check_output(["/bin/bash", "-c", "xprop -id " + capturedid + " | awk '/WM_CLASS/'"]).decode("utf-8").split(",")[1].split()[0].strip().strip(r'"*<>:/\|?`').lower() # remove invalid characters for linux and windows systems
timestamp = datetime.now().strftime("%d_%H-%M-%S_%f") # e.g. "09_16-02-32_753956"
if arg.verbose: print(f"process name: {processname}\ntime: {timestamp}")
if not arg.nostructure:
    struct = "notShot/" + datetime.now().strftime("%Y-%m") + "/" # e.g. "2025-10".
    if not arg.dry: os.makedirs(arg.directory + struct, exist_ok=True)
    if not arg.oldnamescheme:
        filepath = arg.directory + struct + timestamp + "-" + processname + "." + arg.format  # while linux doesn't care if there's an extension, programs usually do.
    else: 
        filepath = arg.directory + struct + processname + "-" + timestamp + "." + arg.format
else:
    if not arg.oldnamescheme:
        filepath = arg.directory + timestamp + "-" + processname + "." + arg.format
    else:
        filepath = arg.directory + processname + "-" + timestamp + "." + arg.format

if arg.dry: print(f"Dry run, not writing to disk (--dry)")
if arg.nostructure: print(f"Skipping making any folders and saving directly (--nostruct)")
if arg.seeimage: print(f"Will open image after saving (--seeimage)")

# save to disk or if failed, try to open in your image viewer of choice out of /tmp
if arg.verbose: print(f"saving image")
try:
    if not arg.dry: 
        capture.save(fp=filepath, format=arg.format)
        if not arg.quiet: subprocess.run(["/usr/bin/notify-send", "-u", "low", "Capture complete", "Image saved to " + filepath + "."])
except Exception:
    if not arg.quiet: subprocess.run(["/usr/bin/notify-send", "-u", "critical", "Capture failed!", "Fatal (error 3): couldn't save image after all? (3)\n\nA temporary copy has possibly been opened, save this manually or you will lose the image!"])
    capture.show()
    sys.exit("fatal (error 3) - couldn\'t save image after all?\ntrying to open temporary file, save this manually or lose the image!") # better than nothing

# post-save actions for result of save
if not arg.dry: print(f"Saved as {filepath}")
else: 
    if not arg.quiet: subprocess.run(["/usr/bin/notify-send", "-u", "low", "Dry run complete", "Would have saved as " + filepath + "."])
    print(f"Dry run complete. Would have saved as {filepath}")

if arg.seeimage:
    if arg.dry: capture.show()
    else:
        if arg.verbose: print(f"final: {filepath}")
        subprocess.call(('xdg-open', filepath)) # open the saved file, not the one in /tmp, in the system default viewer