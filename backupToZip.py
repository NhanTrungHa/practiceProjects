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
        number += 1

    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}')
        backupToZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupToZip.write(os.path.join(foldername, filename))
        backupZip.close()

        print('Done.')