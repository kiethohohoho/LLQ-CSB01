# Lấy từ part 5
districts = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
populations = [247100, 333300, 266800, 420900, 318000]
# Lấy từ bài 1 part 6
areas = [9.224, 43.35, 12.04, 9.96, 10.09]
densities = [populations[i]/areas[i] for i in range(len(populations))]

avg_density = sum(densities) / len(densities)
print('Average population density:') 
print(avg_density)
