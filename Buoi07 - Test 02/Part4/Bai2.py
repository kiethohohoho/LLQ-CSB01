numbers = []
num = int(input('Input the list of numbers.\nEnter 0 to finish.\n'))
while True:
    if num == 0:
        break
    else:
        numbers.append(num)
        num = int(input())

evens = [num for num in numbers if num % 2 == 0]
print('Even numbers in list:', *evens)
