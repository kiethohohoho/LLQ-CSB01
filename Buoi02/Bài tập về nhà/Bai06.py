# Hãy dùng thư viện turtle để vẽ logo của Gmail như sau.
# Để đơn giản, ta có thể xem logo như một hình chữ nhật và một tam giác vuông cân.
# Gợi ý: Sử dụng lệnh pencolor('#de5246') để đổi màu phù hợp.

import turtle
import math

width = 150
height = 125
cross = width / math.sqrt(2) # Độ dài cạnh tam giác vuông cân

turtle.shape("turtle")
turtle.forward(width)
turtle.right(180)
turtle.penup()
turtle.goto(width, -height)
turtle.pendown()
turtle.forward(width)
turtle.right(90)
turtle.pensize(10)
turtle.pencolor('#de5246')
turtle.forward(height)
turtle.right(135)
turtle.forward(cross)
turtle.left(90)
turtle.forward(cross)
turtle.right(135)
turtle.forward(height)

turtle.penup()
turtle.goto(width/2, 30)
turtle.right(180)

turtle.mainloop()