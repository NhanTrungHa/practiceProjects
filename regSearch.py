#! python3
# regSearch.py
# Usage: Read through all text files and return lines that matches a given regex

import re, os

# Save all files in a directory then sort all text files into a list
allFiles = os.listdir(os.curdir)
textFiles = []
for files in allFiles:
    if files.endswith('.txt'):
        textFiles.append(files)

# Get the user regex
userReg = input("Enter a regex to search for: ")
regex = re.compile(userReg)

# Open files in the list then search for regex
for files in textFiles:
    currentFile = open(files)
    content = currentFile.readlines()
    currentFile.close()

    for lines in content:
        matchingLines = regex.findall(lines)
        if matchingLines is not None:
            for items in matchingLines:
                print(items)

