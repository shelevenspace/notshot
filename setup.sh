#!/bin/bash
if [ "$EUID" -eq 0 ]; then
    echo "Fatal error: DO NOT run this as root! Try again without elevation."
    exit 1
fi
which python3.12 > /dev/null || (echo "Python 3.12 not found. Is it installed?" && exit 1)
echo "Setting up Python 3.12 virtual environment..."
python3.12 -m venv ~/.notshot || (echo "Failed to set up virtual environment. Is Python 3.12 accessible?" && exit 1)
echo "Entering virtual environment..."
source ~/.notshot/bin/activate || (echo "Failed to enter virtual environment." && exit 1)
echo "Installing Pillow framework..."
yes | pip3 install pillow==10.2.0 --quiet || (echo "Failed to install Pillow framework." && exit 1)
echo "notShot prerequisites set up. From now on, use ./update.sh!"
echo "Installing notShot from latest release..."
./update.sh
