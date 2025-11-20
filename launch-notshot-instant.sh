#!/bin/bash
if [ "$EUID" -eq 0 ]; then
    echo "Fatal error: DO NOT run this as root! Try again without elevation."
    exit 1
fi
cd ~/.notshot/notshot
python3 notshot.py -a

