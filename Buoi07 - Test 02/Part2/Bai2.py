# Lấy từ bài 1
colors = ['blue', 'red', 'teal', 'green']

colors_to_string = ', '.join(colors)
print(f'Color list: {colors_to_string}')

item = input('Item to delete: ')
if item.isdigit():
    item = int(item)
    # kiểm tra xem item có nằm ngoài index của list hay không
    if item <= 0 or item > len(colors):
        print('Index out of range')
    else:
        colors.remove(colors[item-1])
        colors_to_string = ', '.join(colors)
else:
    # kiểm tra xem item có trong list hay không
    if item in colors:
        colors.remove(item)
        colors_to_string = ', '.join(colors)
    else:
        print('Item not found')

print(f'Color list: {colors_to_string}')
