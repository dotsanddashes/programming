import re

def open_file(fname): #открывает файл
    with open(fname, encoding = 'utf-8') as f:
        text = f.read()
    return text

def search_words(text): #ищет формы
    all_results = re.findall('[\s"][сC]ъе[млшсдв]\w*', text) #я не знаю почему, но у меня никак не получается заставить программу выводить слова с большой буквы и/или с кавычек :(
    if all_results:
        return all_results
    else:
        return print('Nothing found') + exit(0)

def delete_repeat(word_list): #убирает повторяющиеся формы
    final_results = []
    for word in word_list:
        if word not in final_results:
            final_results.append(word)
    return final_results

def main():
    text_for_search = open_file('omnomnom.txt')
    forms = search_words(text_for_search)
    final = delete_repeat(forms)
    print(final)

if __name__ == '__main__':
    main()
