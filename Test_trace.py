import xlrd


workbook = xlrd.open_workbook('tests_info.xls')  # for lab workers
print("dear worker ,to trace and find mistakes we need you enter the following right after finishing a test ")
print("enter the city you tested in ")
city = input()
worksheet = workbook.sheet_by_name(city)    # the sheets are by cities


def find_row(i):
    while i is not None:
        i += 1
    return i


i = find_row(0)
print("enter the number of the test :")
num_of_test = input()
worksheet.cell(row=i, column=0).value = num_of_test

print("enter your id:")
work_id = input()
worksheet.cell(row=i, column=1).value = work_id

print("enter patient's id:")
patient_id = input()
worksheet.cell(row=i, column=2).value = patient_id

print("enter the test time:")
time = input()
worksheet.cell(row=i, column=3).value = time

print("enter test date:")
date = input()
worksheet.cell(row=i, column=4).value = date

print("enter the test result:")
test_res = input()
worksheet.cell(row=i, column=5).value = test_res

workbook.save()


print("thank you!")



