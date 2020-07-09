#! python3
# textToSheet.py
# Usage: Reads several text files and insert each line into spreadsheet row

import os, sys, openpyxl, re

# Access a spreadsheet
os.chdir("D:/Python/practiceProjects")
wb = openpyxl.Workbook()
sheet = wb.create_sheet("sheet", 0)
textFiles = []

# Make regex for files.
fileRegex = re.compile(r'test\d*.txt')

# Create list of files using the regex
for filename in os.listdir("D:/Python/practiceProjects"):
    if fileRegex.match(filename):
        textFiles.append(filename)

# Loop through every row in spreadsheet
for rows in range(1, len(textFiles)+1):
    # Access textfile
    currentFile = open(textFiles[rows - 1])
    # In every textfile, loop through all lines and append to spreadsheet
    sheet.cell(row=rows, column=1).value = str(currentFile.readlines())
    # Close file and save spreadsheet
    currentFile.close()
wb.save('textToSheet.xlsx')
