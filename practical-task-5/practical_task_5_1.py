#1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). В нем создайте функцию создающую
# директории от dir_1 до dir_9 в папке из которой
# запущен данный код. Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os, sys

dir = 'dir_'

def create_dir():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), f'{dir}{i}')
        os.mkdir(new_path)

def del_dir():
    for i in range(1, 10):
        del_path = os.path.join(os.getcwd(), f'{dir}{i}')
        os.rmdir(del_path)

command = sys.argv[1]

if command == 'create_dir':
    create_dir()
elif command == 'del_dir':
    del_dir()