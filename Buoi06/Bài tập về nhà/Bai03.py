def fibonacci(n):
    fib_series = []
    a, b = 1, 1  # Khởi tạo hai phần tử đầu tiên của dãy Fibonacci

    if n <= 0:
        print("Vui lòng nhập một số nguyên dương.")
    elif n == 1:
        fib_series = [1]
    elif n == 2:
        fib_series = [1, 1]
    else:
        fib_series = [1, 1]
        for _ in range(2, n):
            temp = a
            a = b
            b = temp + b
            fib_series.append(b)

    return fib_series

n = int(input("Input a positive number: "))
result = fibonacci(n)
print(f"First {n} Fibonacci number(s: {result}")
