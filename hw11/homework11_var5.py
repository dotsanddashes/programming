import re

def open_file(fname): #открывает файл
    with open(fname, encoding = 'utf-8') as f:
        text = f.read()
    return text

def change(text):
    changed_text = re.sub('Диноза.?вр([аоуеы]?[мвх]?и?)', r'Кот\1', text)
    changed_text = re.sub('динозавр([аоуеы]?[мвх]?и?)', r'кот\1', changed_text)
    return changed_text

def writing_file(result): #запись файла в html
    with open('коты.html', 'w', encoding='utf-8') as f:
        return f.write(result)


def main():
    text = open_file('Динозавры.html')
    result = change(text)
    writing_file(result)

if __name__ == '__main__':
    main()