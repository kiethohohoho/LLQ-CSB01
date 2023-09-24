print("Numbers with sum of digits = 9:")

# Cach 1
# def sum_digit(n):
#   return sum([int(i) for i in str(n)])

# Cach 2
def sum_digit(n):
    temp = n
    tong = 0
    while temp != 0:
        tong += temp % 10
        temp = temp // 10
    return tong

count = 0
i = 1000
while count < 10:
    if sum_digit(i) == 9:
        print(i, end=" ")
        count += 1
    i += 1
