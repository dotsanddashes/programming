import random

def open_file(fname): #открывает файл
    with open(fname, encoding = 'utf-8') as f:
        text = f.read()
    lines = text.splitlines()
    return lines

def create_dictionary(words): #создает словарь с подсказками и словами для отгадывания
    dictionary = {}
    for word in words:
        clue, guess = word.split(',')
        dictionary[guess] = clue
    return dictionary

def main():
    words = open_file('words.csv')
    dict = create_dictionary(words)
    words_to_guess = list(dict.keys())
    rand_word = random.choice(words_to_guess)
    clue = dict[rand_word]
    i = 0
    print('Подберите подходящее слово: ', clue, '...')
    answer = input('Ваш вариант: ')
    while answer != rand_word:
        print('Неверный ответ')
        i += 1
        print('Число попыток: ', i)
        answer = input('Попробуйте еще раз: ')
    print('Ура! Вы угадали!')

if __name__ == '__main__':
    main()