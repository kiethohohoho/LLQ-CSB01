# Một email gồm có hai phần là tên tài khoản và tên miền.
# Ví dụ: somename@gmail.com có tên tài khoản là somename và tên miền là gmail.com
# Hãy viết chương trình yêu cầu người dùng nhập riêng tên tài khoản và tên miền, sau đó in ra email hoàn chỉnh.

name = input("Account name: ")
domain = input("Domain name: ")
print("Full email:", name + "@" + domain)