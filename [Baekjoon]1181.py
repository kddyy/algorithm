import sys
N = int(input())

word = []
for i in range(N):
    word.append(input())

set_word = list(set(word()))

sort_word = []
for i in set_word:
    set_word.append((len(i), i))

result = sorted(sort_word)

for len_word, word in result:
    print(word)
