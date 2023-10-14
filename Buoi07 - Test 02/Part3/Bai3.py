numbers = []
num = int(input('Input the list of numbers.\nEnter 0 to finish.\n'))
while True:
    if num == 0:
        break
    else:
        numbers.append(num)
        num = int(input())

print(f'Sum of numbers in list: {sum(numbers)}')
