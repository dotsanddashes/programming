latin_words = []
word = input('Введите латинское слово: ')
if word == '':
    print('Вы не ввели слово.')
else:
    while word != '':
        if word.endswith('tur') or word.endswith('ntur'):
            latin_words.append(word + '\n')
        word = input()
with open('spisok.txt', 'w', encoding='utf-8') as f:
    f.writelines(latin_words)