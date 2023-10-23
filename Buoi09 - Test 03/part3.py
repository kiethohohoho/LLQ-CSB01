def check_array(arr):
  increasing = decreasing = True
  
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      increasing = False
    if arr[i] < arr[i+1]:
      decreasing = False
      
  if increasing:
    print('Increasing')
  elif decreasing:  
    print('Decreasing')
  else:
    print('None')

arr = [1, 2, 3] 
check_array(arr) # Increasing 

arr = [3, 2, 1]
check_array(arr) # Decreasing

arr = [1, 3, 2] 
check_array(arr) # None