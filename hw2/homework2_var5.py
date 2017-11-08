word = input("Введите слово: ")
word_length = int(len(word))
print('Длина слова: ', word_length)
i = 0
while i < word_length // 2:
    print(word[i])
    i += 1
i = word_length - 1
while i >= word_length // 2:
    print(word[i])
    i -= 1
print("End.")