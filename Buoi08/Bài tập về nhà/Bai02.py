def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1): # n mũ 0.5 chính là căn bậc 2 của n
    if n % i == 0:
      return False
  return True
  
# n = int(input("Input number: "))
# if is_prime(n):
#   print(f"{n} is a prime")
# else:
#   print(f"{n} is not a prime")