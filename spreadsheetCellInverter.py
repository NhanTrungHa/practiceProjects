#! python3
# spreadsheetCellInverter.py - Inverts row and column of spreadsheet and makes new one.

import os, sys, openpyxl

os.chdir("D:/Python/practiceProjects")
wbIn = openpyxl.load_workbook("cellInvert.xlsx")
sheetIn = wbIn.active
outputwb = openpyxl.Workbook()
sheetOut = outputwb.create_sheet("primary", 0)

#TODO: Loop through input sheet and save to output
for rows in range(1, sheetIn.max_row + 1):
    for columns in range(1, sheetIn.max_column + 1):
        sheetOut.cell(row=columns, column=rows).value = sheetIn.cell(row=rows, column=columns).value

filename, fileExtension = os.path.splitext("cellInvert.xlsx")
outputwb.save('{0}modified{1}'.format(filename, fileExtension))