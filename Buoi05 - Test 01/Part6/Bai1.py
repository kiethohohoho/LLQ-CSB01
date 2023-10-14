
def check_odd_digit(n):
    n = str(n)

    for digit in n:
        if int(digit) % 2 == 0:
            return True


    return False

n = int(input("Input a number: "))

if check_odd_digit(n):
    print("CÓ")
else:
    print("KHÔNG CÓ")