# from tkinter import *
from PIL import ImageGrab
import os
import sys
from datetime import datetime
# import keyboard
import argparse
import subprocess
import pathlib

version = "1.0-mvp"

def verify_writable(directory):
    if os.path.exists(directory) and not os.path.isfile(directory) and os.access(directory, os.W_OK) and directory.endswith("/"):
        if arg.verbose: print(f'directory check passed (exists and writable)')
        return
    else:
        if not arg.quiet: subprocess.run(["/usr/bin/notify-send", "--icon=error", "Invalid directory!", "Fatal error: Couldn't access specified directory (1)\n\nYou didn't include a trailing forward slash, the specified directory doesn't exist, isn't writable, or you specified a file."])
        sys.exit("fatal - You didn't include a trailing forward slash, the specified directory doesn't exist, isn't writable, or a file was specified. (1)") # need to expand these errors out into being able to tell you what one happened eventually

parser = argparse.ArgumentParser(
    prog="notShot",
    description="notShot screenshot utility version " + version
)
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help="see unnecessary amounts of detail")
parser.add_argument('-n', '--nostruct', dest="nostructure", action="store_true", help="don't use notshot's folder structure and just save the file at the output location")
parser.add_argument('-s', '--seeimage', dest="seeimage", action="store_true", help="open the image in the default viewer after saving")
parser.add_argument('-q', '--quiet', dest="quiet", action="store_true", help="do not send notifications (this will suppress error notifications too)")
parser.add_argument('--dry', dest="dry", action="store_true", help="dry run (don't save anything but go through the motions)")
parser.add_argument('-o', '--output', default="~/Pictures/", type=pathlib.Path, dest='directory', help="the directory to output to, including trailing forward slash. default: ~/Pictures/")
arg = parser.parse_args()

# figure out where the user wanted the image saved
if arg.verbose: print(f'verbose mode: {arg.verbose} / --output recieved: {arg.directory}')
arg.directory = os.path.expanduser(arg.directory) # this is needed if there is no `--output` provided whatsoever.
if arg.verbose: print(f'expanded: {arg.directory}')
arg.directory = str(arg.directory) + "/" # pathlib strips the trailing forward slash which is necessary here for the final file output.
if arg.verbose: print(f'trailing added: {arg.directory}')
verify_writable(arg.directory)

# ask for what to take image of and figure out where it is
idatcursor = subprocess.check_output(["/bin/bash", "-c", "xwininfo | awk '/Window id/ {print $4}'"]).decode("utf-8").strip()
if arg.verbose: print(f'click caught, capturing information')
geometryupleftx = int(subprocess.check_output(["/bin/bash", "-c", "xwininfo -id " + idatcursor + " | awk '/Absolute upper-left X/ {print $4}'"]).decode("utf-8").strip())
geometryuplefty = int(subprocess.check_output(["/bin/bash", "-c", "xwininfo -id " + idatcursor + " | awk '/Absolute upper-left Y/ {print $4}'"]).decode("utf-8").strip())
geometrywidth = int(subprocess.check_output(["/bin/bash", "-c", "xwininfo -id " + idatcursor + " | awk '/Width/ {print $2}'"]).decode("utf-8").strip())
geometryheight = int(subprocess.check_output(["/bin/bash", "-c", "xwininfo -id " + idatcursor + " | awk '/Height/ {print $2}'"]).decode("utf-8").strip())
processname = subprocess.check_output(["/bin/bash", "-c", "xprop -id " + idatcursor + " | awk '/WM_CLASS/ {print $4}'"]).decode("utf-8").strip().strip('\"').lower() # i am sure there's a better way to do this but for now, it functions.

# prepare the coordinates for imagegrab
if arg.verbose: print(f'id {idatcursor}, geom ulx {geometryupleftx}, geom uly {geometryuplefty}, geom w {geometrywidth}, geom h {geometryheight}, name {processname}\nnow processing geometry')
postgeomleft = geometryupleftx # distance of top left corner from leftmost of screen(s)
postgeomupper = geometryuplefty # distance of top left corner from topmost of screen(s)
postgeomright = geometryupleftx + geometrywidth # distance of bottom right corner from leftmost of screen(s)
postgeomlower = geometryuplefty + geometryheight # distance of bottom right corner from topmost of screen(s)
if arg.verbose: print(f"window distance from left of screen {postgeomleft}\nwindow distance from top of screen {postgeomupper}\nwindow bottom distance from top of screen {postgeomright}\nwindow bottom right distance from left of screen {postgeomlower}\nnow capturing image")

# take picture
capture = ImageGrab.grab(bbox=(postgeomleft, postgeomupper, postgeomright, postgeomlower))
if arg.verbose: print(f"image captured")

# post-capture actions - try to do as little BEFORE capturing as possible to reduce delay between click and capture
timestamp = datetime.now().strftime("%d_%H%M%S_%f") # e.g. "09_160232_753956"
if arg.verbose: print(f"time: {timestamp}")
fileformat = "png"
if not arg.nostructure:
    struct = "notShot/" + datetime.now().strftime("%Y-%m") + "/" # e.g. "2025-10".
    if not arg.dry: os.makedirs(arg.directory + struct, exist_ok=True) # create the notShot folder and the yyyy-mm folder if either don't exist
    filepath = arg.directory + struct + processname + "-" + timestamp + "." + fileformat  # while linux doesn't care about if there's an extension, programs usually do.
else: 
    filepath = arg.directory + processname + "-" + timestamp + "." + fileformat

if arg.dry: print(f"Dry run, not writing to disk (--dry)")
if arg.nostructure: print(f"Skipping making any folders and saving directly (--nostruct)")
if arg.seeimage: print(f"Will open image after saving (--seeimage)")

# save to disk or explode and open in your image viewer of choice instead
if arg.verbose: print(f"saving image")
try:
    if not arg.dry: 
        capture.save(fp=filepath, format=fileformat)
        if not arg.quiet: subprocess.run(["/usr/bin/notify-send", "--icon=info", "Capture complete", "Image saved to " + filepath + "."])
except Exception:
    if not arg.quiet: subprocess.run(["/usr/bin/notify-send", "--icon=error", "Capture failed!", "Fatal error: couldn't save image after all? (3)\n\nA temporary copy has been opened, save this manually or you will lose the image!"])
    capture.show()
    sys.exit("fatal - couldn\'t save image after all? (3)\nopening temporary file, save this manually or lose the image!") # better than nothing

# post-save actions for result of save
if not arg.dry: print(f"Saved as {filepath}")
else: 
    if not arg.quiet: subprocess.run(["/usr/bin/notify-send", "--icon=info", "Dry run complete", "Would have saved as " + filepath + "."])
    print(f"Dry run complete. Would have saved as {filepath}")

if arg.seeimage:
    if arg.dry: capture.show()
    else:
        if arg.verbose: print(f"final: {filepath}")
        subprocess.call(('xdg-open', filepath)) # open the saved file, not the one in /tmp, in the system default viewer