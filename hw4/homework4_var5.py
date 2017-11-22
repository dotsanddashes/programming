with open("text.txt", encoding="utf-8") as f:
    text = f.read()
    splited_text = text.split()
all_words = len(splited_text)
a = 0
for word in splited_text:
    if len(word) >= 10:
        a += 1
print("Доля длинных слов: ", (a / all_words)*100, "%")
print("End.")