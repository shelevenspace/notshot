#!/bin/bash
if [ "$EUID" -eq 0 ]; then
    echo "Fatal error: DO NOT run this as root! Try again without elevation."
    exit 1
fi
~/.notshot/bin/python3.12 ~/.notshot/notshot/notshot.py
