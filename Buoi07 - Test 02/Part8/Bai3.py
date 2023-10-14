# Lấy từ bài 1
scores = [78, 56, 67]

new_score = int(input('Input new score: '))  
scores.append(new_score)
print('High scores:')
for i, score in enumerate(scores):
  print(f'{i+1}. {score}')