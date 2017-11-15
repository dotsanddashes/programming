word = input("Введите слово: ")
word_length = int(len(word))
i = 0
while i <= word_length:
    print(word[-i:])
    i += 1
print("End.")