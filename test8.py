import xlrd

wb = xlrd.open_workbook("虚假用户信息.xls")
sheets = wb.sheets()
sheet = sheets[0]

rows = sheet.nrows
cols = sheet.ncols

for row in range(rows):
    for col in range(cols):
        print(sheet.cell(row, col).value, end=' , ')
    print('\n')
