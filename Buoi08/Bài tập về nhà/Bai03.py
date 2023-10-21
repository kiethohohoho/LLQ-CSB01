from Bai02 import is_prime

n = int(input("Input number: "))

print("First", n, "prime(s):", end=" ")
count = 0
num = 2
while count < n:
  if is_prime(num):
    print(num, end=" ")
    count += 1
  num += 1