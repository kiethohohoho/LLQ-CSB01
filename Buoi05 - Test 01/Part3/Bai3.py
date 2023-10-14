# Viết chương trình cho người dùng nhập vào một tháng trong năm và in ra số ngày của tháng này
mouth = int(input("Input a mouth: "))

if mouth == 1 or mouth == 3 or mouth == 5 or mouth == 7 or mouth == 8 or mouth == 10 or mouth == 12:
    print("This mouth has 31 days")
elif mouth == 2:
    print("This mouth has 28 or 29 days")
elif mouth == 4 or mouth == 6 or mouth == 9 or mouth == 11:
    print("This mouth has 30 days")