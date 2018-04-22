import os
import re

def file_list():
    direct_list = os.listdir()
    return direct_list

def twoandmore(direct_list):
    direct_str = '\n'.join(direct_list)
    longnames = re.findall('.*[ _].*', direct_str)
    return longnames

def main():
    direct_list = file_list()
    longnames = twoandmore(direct_list)
    print('Файлов, в названии которых больше одного слова: ', len(longnames))
    print('Найденные файлы:')
    for word in direct_list:
        print(word)

if __name__ == '__main__':
    main()