# Cho người dùng nhập vào một ngày với định dạng Tháng/Ngày/Năm (MM/DD/YYYY). Ví dụ: 12/31/2020.
# In ra màn hình ngày đã nhập, định dạng theo Ngày/Tháng/Năm.

date = input("Date in MM/DD/YYYY format: ")
print("Date in DD/MM/YYYY format:", date[3:5] + "/" + date[0:2] + "/" + date[6:10])