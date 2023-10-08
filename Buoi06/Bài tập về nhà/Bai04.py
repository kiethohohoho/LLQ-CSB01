number_of_items = int(input("Number of items: "))
print("\n")
items = []
for i in range(1, number_of_items + 1):
    name = input(f"Item {i}: ")
    price = float(input(f"Price of {name}: "))
    items.append((name, price))
    print("\n")

average_price = sum([item[1] for item in items]) / number_of_items
print("Average price:", average_price)
print(f"Item(s) above average price: ", end="")
for item in items:
    if item[1] > average_price:
        print(item, end=" ")

