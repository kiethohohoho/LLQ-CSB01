scores = [78, 70, 67, 56, 45] 

new_score = int(input('Input new score: '))  
scores.append(new_score)
scores.sort(reverse=True)
print('High scores:')
for i in range(5):
  print(f'{i+1}. {scores[i]}')