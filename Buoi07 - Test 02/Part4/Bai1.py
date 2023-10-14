numbers = [5, 1, 8, 92, 7, 30]
evens = [num for num in numbers if num % 2 == 0]
print('Even numbers:', *evens)