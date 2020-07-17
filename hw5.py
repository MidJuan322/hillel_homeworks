import os
# 1. Напишите функцию, которая возвращает список файлов из директории.
def os_walk():
    for root, dirs, files in os.walk("."):
        for filename in files:
            print(filename)
            return filename

# 2. Напишите декоратор для этой функции, который распечатает все файлы с раcширением .log из найденных
def log_check():
    for file in os.listdir("."):
        if file.endswith(".log"):
            log_files = os.path.join("", file)
            print(log_files)
            return log_files