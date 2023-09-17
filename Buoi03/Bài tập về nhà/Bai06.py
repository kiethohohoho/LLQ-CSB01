a = float(input("Input length 1: "))
b = float(input("Input length 2: "))
c = float(input("Input length 3: "))

if a + b > c and a + c > b and b + c > a:
    print("The 3 line segments can form a triangle.")
else:
    print("The 3 line segments cannot form a triangle.")
