import faker
import xlwt
wb = xlwt.Workbook()
sheet = wb.add_sheet('第一个sheet')
head_data = ['姓名', '地址', '手机号', '城市']
for head in head_data:
    sheet.write(0, head_data.index(head), head)

faker = faker.Faker()
for i in range(1, 100):
    sheet.write(i, 0, faker.first_name() + ' ' + faker.last_name())
    sheet.write(i, 1, faker.address())
    sheet.write(i, 2, faker.phone_number())
    sheet.write(i, 3, faker.city())

wb.save("虚假用户信息.xls")