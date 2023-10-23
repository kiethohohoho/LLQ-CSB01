def print_fibo(n):
  a, b = 0, 1
  print(a, end=' ')
  
  for i in range(1, n):
    print(b, end=' ')
    a, b = b, a + b
    
n = int(input("Input a number: "))  
print("\nFirst", n, "Fibonacci numbers:")
print_fibo(n)