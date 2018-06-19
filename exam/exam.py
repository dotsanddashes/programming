import re
import os
import csv

def open_file(fname): #открыть файл
    with open (fname) as f:
        text = f.read()
        text = text.lower()
    return text

def find_info(text): #генерирует словарь со всеми данными, кроме заголовка
    dict = {}
    title = re.findall(r'<title>.*?<', text)
    title = title[0]
    meta = re.findall(r'<meta content=".*?" name=".*?"', text)
    author = meta[1]
    created = meta[4]
    topic = meta[7]
    tegging = meta[0]
    dict['title'] = title[7:-1]
    dict['author'] = author[15:-15]
    dict['created'] = created[15:-16]
    dict['topic'] = topic[15:-13]
    dict['tegging'] = tegging[15:-16]
    return dict

def all_news(): #список файлов
    file_list = os.listdir('./news')
    return file_list

def main(): #записывает csv-файл
    file_list = all_news()
    with open ('table.csv', 'w') as f:
        for fname in file_list:
            adress = './news/' + fname
            text = open_file(adress)
            dict = find_info(text)
            f.write('doc_id' + ',' + fname + '\n')
            for key, value in dict.items():
                f.write(key + ',' + value + '\n')

    
if __name__ == '__main__':
    main()
