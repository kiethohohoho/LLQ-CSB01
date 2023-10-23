def sort_list(lst):
  for i in range(len(lst)):
    min_idx = i
    for j in range(i+1, len(lst)):
      if lst[min_idx] > lst[j]:
        min_idx = j
        
    lst[i], lst[min_idx] = lst[min_idx], lst[i]

  return lst

lst = [5, 1, 8, 92, -1, 30]
print("Original list:")
print(lst)

print("Sorted list:")
print(sort_list(lst))
