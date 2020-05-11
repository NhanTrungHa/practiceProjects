import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
type(wb)
wb.sheetnames

sheet = wb['Sheet3']
sheet.title

anotherSheet = wb.active
anotherSheet