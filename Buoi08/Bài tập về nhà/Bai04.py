def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)

n = int(input("Input number: "))

result = 0
for i in range(1, n+1):
  result += factorial(i) / i
print("Result:", result)