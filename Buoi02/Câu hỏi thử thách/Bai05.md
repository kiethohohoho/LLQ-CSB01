Câu 5. Cho đoạn code sau:
      num = 20
      num += input()
Đâu là kết quả của lệnh print(num) nếu người dùng nhập vào số 2?
A. 20
B. 22
C. 202
D. Chương trình báo lỗi

=> D. Chương trình báo lỗi
Lý do: Giá trị mặc định của input() là chuỗi rỗng. Do đó, lệnh num += input() tương đương với lệnh num += ''. Lệnh này không hợp lệ vì không thể cộng chuỗi với số.
