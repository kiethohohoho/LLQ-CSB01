num = int(input("Input number: "))

# # Cach 1:
# def giai_thua(n):
#     if n == 0:
#         return 1
#     else:
#         return n * giai_thua(n - 1)

# # Cach 2:
def giai_thua(n):
    if n == 0:
        return 1
    else:
        ketQua = 1
        i = 1
        while i <= n:
            ketQua = ketQua * i
            i = i + 1
        return ketQua

if num < 0:
    print("Invalid")
else:
    print(f"{num}! = {giai_thua(num)}")
