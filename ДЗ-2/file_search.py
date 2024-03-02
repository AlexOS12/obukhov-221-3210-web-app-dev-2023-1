import os
from sys import argv

def file_search(path : str, requred_file : str):
    dirs = os.walk(path)
    lines = []
    for i in dirs:
        if requred_file in i[2]:
            with open(f"{i[0]}\\{requred_file}") as file:
                for i in range(5):
                    lines.append(file.readline())
            for i in lines:
                print(i, end="")
            return
    print(f"Файл {requred_file} не найден")

if __name__ == "__main__":
    if len(argv) == 2:
        path, file = os.curdir, argv[1]
        file_search(path, file)
    elif len(argv) == 3:
        path, file = argv[1:]
        file_search(path, file)
    else:
        print("Неверное кол-во аргументов")