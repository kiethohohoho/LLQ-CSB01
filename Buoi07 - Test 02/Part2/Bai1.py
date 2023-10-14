# Lấy từ bài 1
colors = ['blue', 'red', 'teal', 'green']

colors_to_string = ', '.join(colors)
print(f'Color list:\n{colors_to_string}')

position = int(input('Input position: '))
# bắt người dùng nhập lại nếu position <= 0 hoặc position > len(colors)
while position <= 0 or position > len(colors):
    position = int(input('Input position: '))
print(f'Color at position {position}: {colors[position-1]}')