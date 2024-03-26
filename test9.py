import xlrd
from xlutils.copy import copy

wb = xlrd.open_workbook('虚假用户信息.xls', formatting_info= True)
xwb = copy(wb)

sheet = xwb.get_sheet('第一个sheet')
rows = sheet.get_rows()
len(rows)

import faker
faker = faker.Faker()
for i in range(len(rows), 150):
    sheet.write(i, 0, faker.first_name() + ' ' + faker.last_name())
    sheet.write(i, 1, faker.address())
    sheet.write(i, 2, faker.phone_number())
    sheet.write(i, 3, faker.city())

xwb.save('虚假用户信息1.xls')