#! python3
# blankRowInserter.py Takes 3 user arguements and inserts blank rows at that point.
# python blankRowInserter.py 3 2 myProduce.xlsx
# 1st: Chooses initial row to insert 2nd: How many rows to insert 3rd: Name of spreadsheet

import requests, os, sys, openpyxl

# TODO: Take user arguments and store into variables.
if len(sys.argv) < 4:
    print("Usage: python blankRowInserter.py 3 2 myProduce.xlsx")
try:
    initialRow = int(sys.argv[1])
    skippedRows = int(sys.argv[2])
    input = sys.argv[3]
except ValueError as e:
    print("Values should be integers")
    sys.exit()
if not os.path.exists(input):
    print("File does not exist.")
# TODO: Take the spreadsheet provided and create a new file.
inputSheet = openpyxl.load_workbook(input)
sheet = inputSheet.active
outputSheet = openpyxl.Workbook()
# TODO: Store all rows until given point, skip number of lines given
for rows in range(1, sheet.max_row + 1):
    for columns in range(1, sheet.max_column + 1):
        if rows < initialRow:
            outputSheet.cell(rows, columns).value = inputSheet.cell(rows, columns).value
        else:
            # TODO: Insert the rest of the data in spreadsheet and close file.
            outputSheet.cell(rows+skippedRows, columns).value = inputSheet.cell(rows, columns).value
filename, fileExtension = os.path.splitext(inputSheet)
outputSheet.save('{0}modified{1}'.format(filename, fileExtension))