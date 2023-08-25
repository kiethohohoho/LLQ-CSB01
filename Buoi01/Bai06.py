import turtle

turtle.shape("turtle")
# Vẽ hình vuông nhỏ bên trong, độ dài cạnh = 100
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

# Dừng vẽ, di chuyển con trỏ 10 đơn vị, tăng kích thước bút lên 5 và tiếp tục vẽ
turtle.penup()
turtle.forward(10)
turtle.pensize(5)
turtle.pendown()

# Vẽ hình vuông lớn bên ngoài, độ dài cạnh = 120
turtle.left(90)
turtle.forward(110)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(10)

# Ngừng vẽ và chi chuyển con trỏ đến trung tâm hình vuông theo yêu cầu đề bài
turtle.penup()
turtle.goto(50, 50)
turtle.left(90)
turtle.pendown()

turtle.mainloop()