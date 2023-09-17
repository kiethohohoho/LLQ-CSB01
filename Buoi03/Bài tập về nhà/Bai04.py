n = int(input("Input number: "))
if n % 3 == 0 and n % 5 == 0:
    print(f"{n} is divisible by 3 and 5.")
elif n % 3 == 0:
    print(f"{n} is divisible by 3.")
elif n % 5 == 0:
    print(f"{n} is divisible by 5.")
else:
    print(f"{n} is not divisible by 3 and 5.")
