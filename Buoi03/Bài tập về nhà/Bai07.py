import turtle

a = float(input("Input length 1: "))
b = float(input("Input length 2: "))
c = float(input("Input length 3: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Đây là tam giác đều.")
        # Vẽ tam giác đều
        turtle.shape('turtle')
        turtle.forward(a)
        turtle.left(120)
        turtle.forward(b)
        turtle.left(120)
        turtle.forward(c)
        turtle.mainloop()
    elif a == b or b == c or a == c:
        print("The 3 line segments can form a equilateral triangle.")
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("The 3 line segments can form a right triangle.")
    else:
        print("The 3 line segments can form a triangle.")
else:
    print("The 3 line segments cannot form a triangle.")

