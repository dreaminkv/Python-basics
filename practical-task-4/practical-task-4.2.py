#2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def big_three(one_num, two_num, three_num):
    result = sorted((one_num, two_num, three_num), reverse=True)
    return result[0]

print(big_three(1, 2, 5))