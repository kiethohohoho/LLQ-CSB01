# Lấy từ bài 1
districts = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
populations = [247100, 333300, 266800, 420900, 318000]

max_index = populations.index(max(populations))
min_index = populations.index(min(populations))

print('Indices of:')
print('- Most populated dist.:', max_index)  
print('- Least populated dist.:', min_index)