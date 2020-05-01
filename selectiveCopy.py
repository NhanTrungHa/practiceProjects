#! python3
# selectiveCopy.py Program walks through a folder tree and searches for a file extension then copies to a new folder

import shutil
import os


def selectiveCopy(folder, location):
    folder = os.path.abspath(folder)
    location = os.path.abspath(location)
    for foldername, subfolders, filenames in os.walk(folder):
        # Check if file ends in .txt
        for filename in filenames:
            if filename.endswith('.txt'):
                print('Copying %s in %s to %s...' % filename, foldername, location)
                shutil.copy(os.path.join(folder,filename), location)


