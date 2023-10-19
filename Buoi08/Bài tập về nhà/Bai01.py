def is_int(num):
  return num == int(num)

num = float(input("Input number: "))
if is_int(num):
  print(f"{int(num)} is an integer")
else:
  print(f"{num} is not an integer")