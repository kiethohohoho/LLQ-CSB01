employee = ('Jane', 22, 'Engineer')
#employee[1] = 23 : Lỗi sẽ xảy ra vì tuple là immutable và không thể thay đổi giá trị của phần tử.
employee = employee[:1] + (23,) + employee[2:]
print(employee) ## ('Jane', 23, 'Engineer')