#! python3
# renameDates.py - Renames american to european dates.


import shutil, os, re

datePattern = re.compile(r"""^(.*?)
                        (([01])\d)-
                        (([0123])\d)-
                        ((19|20)\d\d)
                        (.*?)$
""", re.VERBOSE)

# Loop through files
for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName)

    if mo is None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(5)

# Form European filename.
euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

absWorkingDir = os.path.abspath('.')
amerFileName = os.path.join(absWorkingDir, amerFileName)
euroFilename = os.path.join(absWorkingDir, euroFilename)

print(f'Renaming "{amerFileName}" to "{euroFilename}"...')
shutil.move(amerFileName, euroFilename)