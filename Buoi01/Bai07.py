import turtle

turtle.shape("turtle")
# Vẽ hình vuông, độ dài cạnh = 100
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

# Dừng vẽ, di chuyển con trỏ đến vị trí có toạ độ (50; 120) và tiếp tục vẽ
turtle.penup()
turtle.goto(50, 120)
turtle.pendown()

# Vẽ hình vuông thứ 2, độ dài cạnh = 100, nằm nghiêng 45 độ
turtle.left(45)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# Ngừng vẽ và chi chuyển con trỏ đến trung tâm hình vuông theo yêu cầu đề bài
turtle.penup()
turtle.goto(50, 50)
turtle.left(45)

turtle.mainloop()