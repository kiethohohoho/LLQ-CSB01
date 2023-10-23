pi = 3.14

def cal_area(r):
  return pi * r * r

r = float(input("Input radius: "))
print("Circle's area:", round(cal_area(r), 2))
