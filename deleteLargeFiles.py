#! python3
# deleteLargeFiles.py Program walks through a folder tree and deletes files above 100MB

import shutil
import os


def deleteLargeFiles(folder):
    folder = os.path.abspath(folder)