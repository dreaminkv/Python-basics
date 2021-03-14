import random
print('загадайте число от 1-100. Компьютер попробует его угадать')
from_num = 1
to_num = 100
while True:
    number = random.randint((from_num), (to_num))
    print(f'Компьютер предположил, что это число: {number}')
    answer = input('Ваедите:если компьютер угадал !, если число меньше загаданного <, если больше загаданного >: ')
    if answer == '!':
        print('Победа')
        break
    elif answer == '<':
        print('Число меньше загаданного')
        from_num = number + 1
    elif answer == '>':
        print('Число больше загаданого')
        to_num = number - 1