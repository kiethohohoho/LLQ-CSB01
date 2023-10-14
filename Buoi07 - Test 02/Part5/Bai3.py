# Lấy từ bài 1
districts = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
populations = [247100, 333300, 266800, 420900, 318000]

# Lấy từ bài 2
max_index = populations.index(max(populations))
min_index = populations.index(min(populations))

print('Names of:')
print('- Most populated dist.:', districts[max_index])
print('- Least populated dist.:', districts[min_index])