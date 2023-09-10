# Yêu cầu người dùng nhập một số thực là bán kính của một hình tròn. In ra chu vi và diện tích của hình tròn đó.
# Biết:
# S = 3.1416P = 2πrS = πr^2

pi = 3.1416
r = float(input("Radius: "))
print("Perimeter:", 2*pi*r)
print("Area:", pi*r**2)