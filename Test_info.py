import xlrd


workbook = xlrd.open_workbook('tests_info.xls')  # worker in the lab writing this excel
print("dear manager enter the city you want to see the info about ")
city = input()
worksheet = workbook.sheet_by_name(city)    # the sheets are by cities
print(worksheet)


