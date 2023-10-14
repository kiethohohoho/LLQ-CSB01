scores = [78, 56, 67]

new_score = int(input('Input new score: '))  
scores.append(new_score)
scores.sort(reverse=True)
print('High scores:')
for i in range(len(scores)):
  print(f'{i+1}. {scores[i]}')