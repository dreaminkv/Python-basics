import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from game import game

save_info('Начало')
try:
    command = sys.argv[1]
except:
    print('введите help')
else:
    if command == 'list_file':
        get_list()
    elif command == 'change_dir':
        name = sys.argv[2]
        change_dir(name)
    elif command == 'game':
        game()
    elif command == 'list_folder_only':
        get_list(True)
    elif command == 'create_file':
        try:
            name = sys.argv[2]
            text = sys.argv[3]
            path = sys.argv[4]
            create_file(name, text, path)
        except IndexError:
            print('Не заданно название файла')
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
            dir = sys.argv[3]
            create_folder(name, dir)
        except IndexError:
            print('Не заданно название папки')
    elif command == 'delete':
        try:
            name = sys.argv[2]
            delete_file(name)
        except IndexError:
            print('Не заданно имя файла для удаления')
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
            copy_file(name, new_name)
        except:
            print('Введите имя копируемого файла и создайте новое имя')
    elif command == 'help':
        print('list_file - показать файлы и папки')
        print('nlist_folder_only - показать только папки')
        print('create_file - создать файл, нужно указать название файла, текст, полный путь к файлу, вида (C:\\...)')
        print('create_folder - создать папку, нужно указать название новой папки и точный путь, вида (C:\\...)')
        print('delete - удалить файл или папку, нужно прописать путь до файл, вид: C:\\Users\\ ....primer.txt')
        print('copy - скопировать файл или папку, нужно указать полный путь C:\\Users\\ ....primer.txt к файлу и имя копии, копия окажется в корневой директории')
    save_info('Конец')