def open_file(fname): #открывает файл и возвращает список слов
    with open(fname, encoding = 'utf-8') as f:
        text = f.read()
        splited_text = text.split()
    return splited_text
def words_search(): #ищет прилагательные на -ous и заносит их в словарь следующим образом: прилагательное - ключ, его длина - значение
    words = open_file('Pride_and_Prejudice.txt')
    dictionary = {}
    for word in words:
        if word.endswith('ous'):
            dictionary[word] = len(word)
    return dictionary
def how_many(): #считает количество прилагательных на -ous
    words = open_file('Pride_and_Prejudice.txt')
    i = 0
    for word in words:
        if word.endswith('ous'):
            i += 1
    return print('Всего прилагательных, заканчивающихся на -ous: ', i)
def mid_length(): #считает среднюю длину
    dictionary = words_search()
    i = 0
    a = 0
    for num in dictionary.values():
        a += 1
        i += int(num)
    return print('Средняя длина прилагательного: ', i/a)

how_many()
mid_length()