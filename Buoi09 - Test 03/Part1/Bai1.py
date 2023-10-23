def is_even(num):
  return num % 2 == 0

num = int(input("Input a number: "))
if is_even(num):
  print("This number is even")
else:
  print("This number is not even")
