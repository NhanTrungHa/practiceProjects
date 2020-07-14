#! python3
# sheetToText.py
# Usage: Reads a spreadsheet and write cells of column A into a text file, B into another text file, etc.

import os, sys, openpyxl

# TODO: Read a spreadsheet
os.chdir("D:/Python/practiceProjects")
wb = openpyxl.load_workbook("sheetToText.xlsx")
sheet = wb.active
# TODO: Loop through rows and columns
for columns in range(1, sheet.max_column + 1):
    for rows in range(1, sheet.max_row + 1):
        # TODO: Every column loop, open a new textfile in location and write into the text file.
        currentText = open('sheetToText{0}.txt'.format(columns), 'a')
        if str(sheet.cell(row=rows, column=columns).value) == "None":
            continue
        else:
            currentText.write(str(sheet.cell(row=rows,column=columns).value) + " ")
    # TODO: Close text file every loop
    currentText.close()
