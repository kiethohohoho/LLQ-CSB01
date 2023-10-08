arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Mảng cộng 2
arr_add_2 = [x + 2 for x in arr]

# Mảng nhân 2
arr_multiply_by_2 = [x * 2 for x in arr]

# Mảng dịch 2
arr_shift_2 = arr[2:] + arr[:2]

# In các mảng mới
print("Original list : ", arr)
print("Add 2         :", arr_add_2)
print("Multiply by 2 :", arr_multiply_by_2)
print("Shift 2       :", arr_shift_2)
