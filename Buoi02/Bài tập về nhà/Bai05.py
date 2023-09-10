# Lãi suất tiết kiệm của một ngân hàng là 5% một năm. Giả sử một khách hàng gửi A đồng vào ngân hàng:
#     - Sau một năm, khách hàng đó sẽ có tổng cộng A×105% đồng.
#     - Sau hai năm, khách hàng đó sẽ có tổng cộng A×(105%)^2 đồng.
#     - Tương tự với các năm tiếp theo.
# Yêu cầu người dùng nhập số tiền gửi vào ngân hàng trên. In ra số tiền người dùng có được sau một năm, hai năm và mười năm.

money = float(input("Deposit: "))
print("Account after 1 year:", money*1.05)
print("Account after 2 years:", money*(1.05**2))
print("Account after 10 years:", money*(1.05**10))
