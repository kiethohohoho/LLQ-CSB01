sentence = input("Write a sentence: ")
strs = sentence.split(" ")
words = []
for i in strs:
    if i in words:
        continue
    else:
        words.append(i)
print("Number of unique words: ", len(words))