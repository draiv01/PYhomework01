# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines 
# (на всякий случай проверим, что задано положительное целое число). 
# Протестируем функцию на файле «article.txt» со следующим содержимым:


# def read_last(lines, file):
#     if lines > 0:
#         with open(file, encoding="utf-8") as text:
#             file_lines = text.readlines()[-lines:]
#         for line in file_lines:
#             print(line.strip())
#         else:
#             print("end")
 
 

# read_last(3, "article.txt")
# read_last(-5, "article.txt")




# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file),
# которая записывает в файл result.txt слово, имеющее максимальную длину
# (или список слов, если таковых несколько).


import os
 
 
def longest_words(file):
    with open(file, "r") as text:
        words = text.read().split()
 
    max_length = len(max(words, key=len))
    sought_words = [word for word in words if len(word) == max_length]
 
    f = "result.txt"
    i = 1
    while os.path.exists(f):
        f = f"result{i}.txt"
        i += 1
    with open(f, "w") as file:
        file.write(" ".join(sought_words) + "\n")
 
 
longest_words("article.txt")