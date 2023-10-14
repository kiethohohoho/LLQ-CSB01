# Lấy từ part 5
districts = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
populations = [247100, 333300, 266800, 420900, 318000]

areas = [9.224, 43.35, 12.04, 9.96, 10.09]
densities = [populations[i]/areas[i] for i in range(len(populations))]
print('Population density of:')
for i in range(len(populations)):
    print('-', districts[i] + ':', densities[i])
