# ШАГ 1 Функция для создания файла
import os, shutil, datetime


def create_file(name, text, path):  # Функция с 2 параметрами, по умолчанию в text стоит None, так как мы можем
    # записать текст в файл, а можем и не записывать
    os.chdir(path)
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# ШАГ 2 Функция создающая папку


def create_folder(name, path):
    try:
        os.chdir(path)
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже создана')


# ШАГ 3 просмотр файлов и папок

def get_list(only_folder=False):
    result = os.listdir()
    if only_folder:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# ШАГ 4 Удаление папок и файлов

def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# ШАГ 5 Копирование файлов

def copy_file(name, new_name):
    try:
        if os.path.isdir(name):
            shutil.copytree(name, new_name)
        else:
            shutil.copy(name, new_name)
    except FileExistsError:
        print('Такая папка уже есть')


# ШАГ 6 Сохранение информации о работе

def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')

# ШАГ 7 Добавить возможность изменения текущей рабочей директории.

def change_dir(name):
    os.chdir(name)
    print(os.getcwd())

if __name__ == '__main__':
    create_file('Text.dat')
    create_file('Text.dat', 'lalalalalaa')
    create_folder('тша')
    get_list(True)
    delete_file('тша')
    copy_file('first.txt', 'first1.txt')
    save_info('Privetiki')
    change_dir('new_g')
