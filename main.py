"""число Вудала

Описание программы:

Вычисление n-го обобщенного числа Вудала.
Проверка n-го обобщенного числа Вудала на кратность трем.

Примеры:
1)
входный данные:
K = hhhh
выведет программа:
Необходимо ввести целое число. Введено ghgh
ведите число K:
2)
входный данные:
K = 2
N = 10
выведет программа:
n-е обобщенное число Вудала: 10239
число 10239 кратно 3
3)
входный данные:
K = 10
N = 2
выведет программа:
Число не подходит к ограничению N + 2 > K, N: 2
ведите число N, N + 2 > K:
4)
входный данные:
K = 3
N = 5
выведет программа:
n-е обобщенное число Вудала: 1214
число 1214 не кратно 3
-------

    python -m woodall_number.py

:Authors:
    Колезнев Алексей Владимирович, КИ20-16/1б
"""


# Далее идет Ваш код (функции, класс, атрибуты и т.д.)

def woodalls_number(n, k):
    woodalls_number_ = (k ** n) * n - 1
    print('-' * 15)
    print('n-е обобщенное число Вудала: {}' .format(woodalls_number_))
    return woodalls_number_


def aliquot(number):
    if number % 3 == 0:
        print('число {} кратно 3' . format(number))
        print('-' * 15)
    else:
        print('число {} не кратно 3' .format(number))
        print('-' * 15)


def main():
    while True:
        stop = input('Продолжить y/n? ').lower()
        if stop in ('n', 'no'):
            break
        while True:
            k = input('ведите число K: ')
            if not k.isdigit() or int(k) == 0:
                print('Необходимо ввести целое число. Введено', k)
            else:
                break

        while True:
            n = input('ведите число N, N + 2 > K: ')
            if n.isdigit() or not int(n) == 0:
                if int(n) + 2 > int(k):
                    break
                print('Число не подходит к ограничению N + 2 > K, N:', n)
            else:
                print('Необходимо ввести целое число. Введено', n)

        k = int(k)
        n = int(n)

        woodalls_number_ = woodalls_number(n, k)
        aliquot(woodalls_number_)


if __name__ == '__main__':
    main()
