#! python3
# gapFiller.py Find gaps in series of files and creates a file to fill it.

import shutil
import os
import re

def gapFiller(folder, prefix):
    folder = os.path.abspath(folder)
    fileReg = re.compile(r'%s\d\d\d\.txt' % prefix)

    while True:
        basefiles = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1