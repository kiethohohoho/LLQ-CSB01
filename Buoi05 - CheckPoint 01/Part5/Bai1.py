print("== FREAKING MATH CONSOLE ==")
print("Give correct answers to get scores.")
print()

def random_calculation(n):
    if n == 1:
        return '+'
    elif n == 2:
        return '-'
    elif n == 3:
        return '*'
    else:
        return '/'

def get_correct_result(left, calculation, right):
    if calculation == '+':
        return left + right
    elif calculation == '-':
        return left - right
    elif calculation == '*':
        return left * right
    else:
        return left / right

from random import *
turns = 5
i = 1
scores = 0
while i <= turns:
    left = randint(0, 100)
    calculation = random_calculation(randint(1, 4))
    right = randint(1, 50)
    result = randint(-100, 100)
    print(f"{left} {calculation} {right} = {result}")
    user_answer = int(input("1 for True, 0 for False: "))
    while user_answer != 0 and user_answer != 1:
        user_answer = int(input("1 for True, 0 for False: "))
    if (get_correct_result(left, calculation, right) == result and user_answer == 1) or (get_correct_result(left, calculation, right) != result and user_answer == 0):
        scores += 1
        print(f"Scores: {scores}")
    else:
        print("Incorrect.")
    print()
    i += 1
print()
print("== GAME OVER ==")
print(f"Your total score is {scores}")