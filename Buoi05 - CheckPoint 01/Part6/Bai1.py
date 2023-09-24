
def check_odd_digit(n):
    n = str(n)

    even_count = 0

    for digit in n:
        if int(digit) % 2 == 0:
            even_count += 1


    return even_count > 0

n = int(input("Input a number: "))

if check_odd_digit(n):
    print("CÓ")
else:
    print("KHÔNG CÓ")