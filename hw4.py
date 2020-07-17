# 1. Напишите функцию, которая читает и распечатывает текстовый файл.
def file_open_read():
    with open('markul-lebron.txt', 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            print(line, end=" ")
            line = file.readline()
    print(file_open_read)
    return file_open_read

# 2. Напишите декоратор к этой функции, который печатает название файла и количество слов в нем
def name_words():
    with open('markul-lebron.txt', 'r', encoding='utf-8') as file:
        name = file.name
        words = 0
        for lines in file:
            wordslist = lines.split()
            words = words + len(wordslist)
        print('Слов в тексте: ' + str(words))
        print('Название фалйа: ' + name)
    return name_words

