#! python3
# deleteLargeFiles.py Program walks through a folder tree and deletes files above 100MB

import shutil
import os
import send2trash

def deleteLargeFiles(folder):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if os.path.getsize(filename) >= 100000000:
                send2trash.send2trash('filename')
