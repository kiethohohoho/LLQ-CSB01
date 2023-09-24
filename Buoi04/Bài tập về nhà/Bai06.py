n = int(input("Nhập vào một số > 2: "))

d = 0
if n <= 2:
    n = int(input("Nhập vào một số > 2: "))
else:
    d = (1 - (n-2)/n)*180

from turtle import *
shape('turtle')
i = n
while i > 0:
    forward(100)
    left(d)
    i -= 1
mainloop()