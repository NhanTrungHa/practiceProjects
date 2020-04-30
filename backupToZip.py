#! python3
#backupToZip.py - Copies an entire folder and contents into a Zip File.

import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break

