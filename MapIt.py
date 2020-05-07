#! python3
# MapIt.py - Launches map in browser using user input.

import webbrowser
import sys

if len(sys.argv) > 1:
    address = ' '.join()[1:]
    # stores address of list elements into variable and adds a space