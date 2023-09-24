num = int(input("Input number: "))

# Cách 1
# i = 1
# while i <= num:
#     j = 1
#     while j <= i:
#         print("#", end="")
#         j += 1
#     print()
#     i += 1

# Cách 2
for i in range(num):
    print("#" * (i+1))