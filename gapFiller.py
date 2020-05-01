#! python3
# gapFiller.py Find gaps in series of files and creates a file to fill it.

import shutil
import os
import re

def gapFiller(folder, prefix):
    folder = os.path.abspath(folder)
    fileReg = re.compile(r'(%s)(\d\d\d)\.txt' % prefix)

    # store all file with prefex
    prefixFiles = list()
    # loop through the list and see if there is gap
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if re.search(fileReg, filename):
                prefixFiles.append(filename)

    prefixFiles.sort()
    # create file with gap name
    for i in range(len(prefixFiles)):
        mo = re.search(fileReg, prefixFiles[i])
        if int(mo.group(2)) == i + 1:
            continue
        if i + 1 < 10:
            shutil.copy(prefixFiles[i], prefix + '00' + str(i + 1) + '.txt')
            os.unlink(prefixFiles[i])
        elif i + 1 < 100:
            shutil.copy(prefixFiles[i], prefix + '0' + str(i + 1) + '.txt')
            os.unlink(prefixFiles[i])
        else:
            shutil.copy(prefixFiles[i], prefix + str(i + 1) + '.txt')
            os.unlink(prefixFiles[i])

            