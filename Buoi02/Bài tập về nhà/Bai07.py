# Hãy dùng thư viện turtle để vẽ logo sau (không cần vẽ chữ).
# Gợi ý: Sử dụng lệnh pencolor('#cf8f03') và pencolor('#0b2c3c') để đổi màu phù hợp.

import turtle

turtle.pensize(10)
turtle.pencolor('#cf8f03')

# Vẽ hình thoi thứ nhất
turtle.left(30)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(150)

# Vẽ hình thoi thứ hai
turtle.pencolor('#0b2c3c')
turtle.penup()
turtle.goto(50, 0)
turtle.pendown()
turtle.left(30)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)

turtle.mainloop()