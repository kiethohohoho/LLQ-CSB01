num = int(input("Input number: "))

# Cach 1
# tong = sum([int(i) for i in str(num)])

# Cach 2
temp = num
tong = 0
while temp != 0:
    tong += temp % 10
    temp = temp // 10

print(f"Sum of digits of {num} = {tong}")
