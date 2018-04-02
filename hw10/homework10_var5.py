import re

def open_file(fname): #открывает файл
    with open(fname, encoding = 'utf-8') as f:
        text = f.read()
    return text

def search_family(file): #ищет нужную подстроку
    result = re.search('Семейство.*', file)
    if result:
        return result.group()
    else:
        return print('Nothing found') + exit(0)

def fin_search(family): #ищет само семейство
    new_family = family[9:]
    fin_result = re.search('[А-Я]\w*', new_family)
    if fin_result:
        return fin_result.group()
    else:
        return print('Nothing found') + exit(0)

def writing_file(result): #запись файла
    with open('result_family.txt', 'w', encoding='utf-8') as f:
        return f.write(result)

def main():
    fname = input('Введите имя файла: ')
    file = open_file(fname)
    family = search_family(file)
    result = fin_search(family)
    writing_file(result)

if __name__ == '__main__':
    main()