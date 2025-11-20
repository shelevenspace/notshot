#!/bin/bash
if [ "$EUID" -eq 0 ]; then
    echo "Fatal error: DO NOT run this as root! Try again without elevation."
    exit 1
fi
echo "Checking for notShot..."
cd ~/.notshot/ || (echo "Can't find or access notShot folder. Have you ran setup.sh?" && exit 1)
if [ -f ~/.notshot/notshot/notshot.py ]; then # find out if notShot is already present
    echo "Updating notShot..." && cd ~/.notshot/notshot
else
    echo "notShot wasn't detected, it will be downloaded."
    mkdir ~/.notshot/notshot && cd ~/.notshot/notshot
fi
wget -q -nv -O - https://api.github.com/repos/shelevenspace/notshot/releases/latest | awk -F': ' '/browser_download_url/ && /notshot-1\.[0-9]+\.[0-9]+\.tar\.gz/ {gsub(/"/, "", $(NF)); system("wget -qi -L " $(NF))}' || (echo "Error downloading latest release." && exit 1) # download the latest version of notShot 1
filename="$(find -name notshot-1*.tar.gz)"
tar -xvz --overwrite -f $filename || (echo "Error untarring. Did the file download correctly?" && exit 1)
rm $filename || (echo "Couldn't delete tar, manual cleanup necessary.")
echo "Done updating notShot installation!"
xdg-open ~/.notshot/notshot
