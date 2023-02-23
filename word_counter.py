with open('file.txt','r') as file:
    data = file.read()
words = data.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
sorted_word_count = dict(sorted(word_count.items()))
for word, count in sorted_word_count.items():
    print(word, count)
    
