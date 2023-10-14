# Lấy từ bài 1
colors = ['blue', 'red', 'teal', 'green']
# Lấy từ bài 2
colors_to_string = ', '.join(colors)
print(f'Color list:\n{colors_to_string}')

new_color = input('Input a new color: ')
colors.append(new_color)
colors_to_string = ', '.join(colors)
print(f'Color list:\n{colors_to_string}')