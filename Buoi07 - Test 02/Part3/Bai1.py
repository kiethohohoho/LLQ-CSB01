numbers = [5, 1, 8, 92, -1, 30]
num = int(input('Input a number: '))
if num in numbers:
  print(f'Number found at position {numbers.index(num) + 1}')
else:
  print('Number not found') 