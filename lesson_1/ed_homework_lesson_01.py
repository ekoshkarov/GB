print('###' * 40)
print('ЗАДАНИЕ: №1')
print('###' * 40)

name = input('What is your name?  Enter your name: ')
print('Glad to meet you', name,'!')
print('Have a nice day', name, '!  :)')

print('___' * 40)
a = 100
b = 200
c = 300
d = a + b + c
print('a =', a, 'b =', b, 'c = ', c)
print('d = a+b+c', d)

print('   ' * 40)

print('###' * 40)
print('ЗАДАНИЕ: №2')
print('###' * 40)
#######################################

import time

print('введем число (в секундах) и узнаем сколько в нем часов, минут и секунд')
print('   ' * 40)

n = int(input('enter the number of seconds from 1 to 86400:  '))
print('введенное число: ',n)
time_format = time.strftime("%H:%M:%S", time.gmtime(n))
print("Time in preferred format :-",time_format)

print('   ' * 40)
print('###' * 40)
print('ЗАДАНИЕ: №3')
print('###' * 40)
#######################################

print('   ' * 40)
print('введем число (n)  и проверим формулу:  ')
print( 'результат = n + nn + nnn')
print('   ' * 40)
n = int(input("enter any number from 0 to 9: "))

temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print("Результат равен:", comp)

print('   ' * 40)
print('###' * 40)
print('ЗАДАНИЕ: №4')
print('###' * 40)
#######################################
print('   ' * 40)



n = int(input("Введите целое положительное число "))
print('   ' * 40)
print('найдем самую большую цифру в этом числе')
print('   ' * 40)
max1 = n % 10

while n >= 1:
    n = n // 10
    if n % 10 > max1:
            max1 = n % 10
    elif n > 9:
        pass


print('Максимальное цифра в числе:  ', max1)


print('   ' * 40)
print('###' * 40)
print('ЗАДАНИЯ: №5 & №6')
print('###' * 40)
#######################################
print('   ' * 40)

print('Анализ финансовой деятельности компании:  ')

revenue = int(input('Введите значение выручки компании: '))
print('выручка, (млн.руб.) :  ', revenue)
cost = int(input('Введите значение затрат компании: '))
print('затраты, (млн.руб.) :  ', cost)
if revenue > cost:
    print('Компания работает с прибылью, молодцы! ')
    profit = revenue - cost                                         # Определение рентабельности выручки = отношение прибыли к выручке
    profitability = profit / revenue
    print('рентабельность компании :  ', profitability * 100, '%')
    worker = int(input('Введите количество сотрудников в компании (человек):  '))
    production = profit / worker
    print('Выработка на 1 сотрудника составляет:   ', production, ('млн.руб.'))

else:
    print('Компания убыточна, необходимо принять меры!  ')

print('   ' * 40)
print('###' * 40)
print('ЗАДАНИЕ: №7')
print('###' * 40)
#######################################
print('   ' * 40)

# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

# Ввод исходных данных

a = int(input("Введите расстояние первой пробежки в км: "))
b = int(input("Введите целевой результат в км: "))
print('-----' * 40)
# задаем начальное значение счетчика дней
counter = 1
while a < b:                                   # запуск цикла с условием
    a *= 1.1                                   # расчет расстояния пробежки (+10% ежедневно)
    a = float('{:.2f}'.format(a))              # уменьшаем количество знаков после запятой в пробежке
    print(counter+1, 'день', '    ', a, 'км')  # выводим ежедневный результат красиво :)
    counter += 1                               # увеличение счетчика дней
                                               # вывод финального результата
print(f"На {counter}-й день спортсмен достиг результата — не менее {b} км")
print('-----' * 40)

print('###' * 40)
print('ДОМАШНЯЯ РАБОТА ЗАВЕРШЕНА. СПАСИБО ЗА ВНИМАНИЕ !!!')                 #  уффф

