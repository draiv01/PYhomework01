# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines 
# (на всякий случай проверим, что задано положительное целое число). 
# Протестируем функцию на файле «article.txt» со следующим содержимым:


# with open("art.txt", "r", encoding="utf-8") as file:
#     with open("res.txt", "w", encoding="utf-8") as file:
#         text = file.read().splitlines()
#         for i in range(len(text)):
#             if text[i].split():
#                 print(text)


def read_last(lines, file):
    if lines > 0:
        with open(file, encoding="utf-8") as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
        else:
            print("Количество строк может быть только целым положительным")
 
 
# Тесты
read_last(3, "art.txt")
read_last(-5, "art.txt")