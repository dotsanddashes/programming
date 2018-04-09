import re

def open_file(fname): #открывает файл
    with open(fname, encoding = 'utf-8') as f:
       text = f.read()
    return text

def find_header(text): #ищет нужные нам строки
    header_start = text.split('<teiHeader>') #делит текст на строки по тегу <teiHeader>
    header_fin = header_start[1].split('</teiHeader>') #рассматривает первый элемент списка (т.к. в нем содержится вложенные в шапку теги, все, что было до <teiHeader>, лежит в нулевом элементе) и делит его по закрывающему тегу
    header = header_fin[0].split('\n') #в нулевом элементе предыдущего списка лежит интересующий нас заголовок файла XML
    return header

def count_lines(header): #считает строки
    i = len(header)+2
    return i #в header не лежат строки с тегами <teiHeader> и </teiHeader>, т.е. мы их не посчитали - поэтому +2

def first_task(i):
    with open('first_task_result.txt', 'w', encoding = 'utf-8') as f:
        return f.write(str(i))

def lemmas(text): #находит все возможные значения тега types
    all_lemmas = re.findall('<w lemma=.*?>', text)
    lemmas_str = '\n'.join(all_lemmas)
    all_types = re.findall('type=".*?"', lemmas_str)
    types = []
    for word in all_types:
        if word[6:-1] not in types:
            types.append(word[6:-1])
    return types

def make_dict(types, text): #создает словарь
    dictionary = {}
    for word in types:
        dictionary[word] = len(re.findall(word, text))
    return dictionary

def second_task(dictionary):
    a = '\n'.join(dictionary) #оно выводит только ключи, но не значения, увы :(
    with open('second_task_result.txt', 'w', encoding = 'utf-8') as f:
        return f.write(a)

def main():
    text = open_file('контрольная.xml')
    header = find_header(text)
    i = count_lines(header)
    first_task(i)
    types = lemmas(text)
    dictionary = make_dict(types, text)
    second_task(dictionary)

if __name__ == '__main__':
    main()