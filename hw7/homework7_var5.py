def file_name(): #проверяет существование файла
    fname = input('Введите имя файла: ')
    try:
        open(fname)
        return(fname)
    except FileNotFoundError:
        return print('Файл не найден. Попробуйте еще раз.') + exit(0)
def open_file(): #открывает файл и возвращает список слов
    fname = file_name()
    with open(fname, encoding = 'utf-8') as f:
            text = f.read()
            splited_text = text.split()
    return splited_text
def words_search(): #ищет прилагательные на -ous и создает список
    words = open_file()
    adj_list = []
    for word in words:
        if word.endswith('ous'):
            adj_list.append(word)
    return adj_list
def how_many(l): #cчитает количество прилагательных
    return print('Всего прилагательных, кончающихся на -ous: ', len(l))
def mid_length(a): #создает словарь и считает среднюю длину прилагательного
    words = a
    dictionary = {}
    for word in words:
        dictionary[word] = len(word)
    i = 0
    a = 0
    for num in dictionary.values():
        a += 1
        i += int(num)
    return print('Средняя длина прилагательного: ', i/a)
def main():
    my_var = words_search()
    how_many(my_var)
    mid_length(my_var)
if __name__ == '__main__':
    main()