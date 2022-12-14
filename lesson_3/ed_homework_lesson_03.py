print('###' * 47)
print('###' * 20, 'УРОК №3  ЗАДАНИЕ №1', '###' * 20 )
print('###' * 47)

print(' ')
print('***' * 22, 'Функции', '***' * 22)
print(' ')

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def calculator(a, b):
    print('Результат деления (a/b):  ')
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Ошибка! Делить на ноль нельзя')

print(calculator(int(input('Введите первое число (a): ')), int(input('Введите второе число (b): '))))

print('###' * 47)
print('###' * 20, 'УРОК №3  ЗАДАНИЕ №2', '###' * 20 )
print('###' * 47)

print(' ')
print('***' * 22, 'Функции', '***' * 22)
print(' ')

# # 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# # Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.


def user_data(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')


user_data(
    name=input(' Имя:  '),
    lastname=input(' Фамилия:  '),
    year_of_birth=input(' Год Рождения:  '),
    city=input(' Город проживания:  '),
    email=input(' email:  '),
    phone=input(' phone:  '),
)

print('###' * 47)
print('###' * 20, 'УРОК №3  ЗАДАНИЕ №3', '###' * 20 )
print('###' * 47)

print(' ')
print('***' * 22, 'Функции', '***' * 22)
print(' ')

def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)


print('###' * 47)
print('###' * 20, 'УРОК №3  ЗАДАНИЕ №4', '###' * 20 )
print('###' * 47)

print(' ')
print('***' * 22, 'Функции', '***' * 22)
print(' ')

# # 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# # Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# # При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# # Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# # Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    return x ** y

print(f'Возведения степени вариантом 1: '
      f'{my_func(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')

#                           #  второй вариант не ролучается пока


print('###' * 47)
print('###' * 20, 'УРОК №3  ЗАДАНИЕ №5', '###' * 20 )
print('###' * 47)

print(' ')
print('***' * 22, 'Функции', '***' * 22)
print(' ')

# # Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# # При нажатии Enter должна выводиться сумма чисел.
# # Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# # Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# # Но если вместо числа вводится специальный символ, выполнение программы завершается.
# # Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def calculate_sum(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            flag = True
    return sum, flag

general_sum = 0

while True:
    numbers_string = input('Введите числа через пробел: ').split(' ')
    sum, stop_flag = calculate_sum(*numbers_string)
    general_sum += sum
    print(f'сумма {general_sum}')

    if stop_flag:
        break

print('###' * 47)
print('###' * 20, 'УРОК №3  ЗАДАНИЕ №6', '###' * 20)
print('###' * 47)

print(' ')
print('***' * 22, 'Функции', '***' * 22)
print(' ')

# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func(text):
    return text.title()

def my_title(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)

output_1 = []
output_2 = []
for word in input('Введите строку, слова в которой разделены пробелами: ').split(' '):
    output_1.append(int_func(word))
    output_2.append(my_title(word))

print(f'Вариант1 Результат : {" ".join(output_1)}')
print(f'Вариант2 Результат : {" ".join(output_2)}')