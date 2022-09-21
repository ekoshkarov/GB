print('###' * 47)
print('###' * 20, 'УРОК №6  ЗАДАНИЕ №1', '###' * 20 )
print('###' * 47)

print(' ')
print('***' * 22, '  ООП  ', '***' * 22)
print(' ')

# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

import time

class TrafficLight():

    # Определяем время ожидания сигнала светофора
    red_color_wait = 7
    yellow_color_wait = 2
    green_color_wait = 5

    # Определяем названия цветов сигналов светофора
    red_color_name = 'красный'
    yellow_color_name = 'желтый'
    green_color_name = 'зеленый'

    def __init__(self, color):
        self.__color = color
        print(f'\nСоздан новый объект TrafficLight со стартовым цветом {self.__color}')

    def switch_light(self, color, wait_period):
        self.wait_period = wait_period
        print(f'Включен {color} свет, время ожидания {self.wait_period} сек')
        time.sleep(self.wait_period)

    def running(self, color = ''):


        if not color:
            loc_color = self.__color
        else:
            loc_color = color

        if loc_color == self.red_color_name:
            self.switch_light('красный', self.red_color_wait)
            self.switch_light('желтый', self.yellow_color_wait)
            self.switch_light('зеленый', self.green_color_wait)
        elif loc_color == self.yellow_color_name:
            self.switch_light('желтый', self.yellow_color_wait)
            self.switch_light('зеленый', self.green_color_wait)
        else:
            self.switch_light('зеленый', self.green_color_wait)

        print('Цикл переключения цветов завершен')

tl1 = TrafficLight('красный')
tl1.running()

tl2 = TrafficLight('желтый')
tl2.running()

tl3 = TrafficLight('зеленый')
tl3.running()

# Инициализируем класс красным цветом, а метод запускаем с желтого
tl1 = TrafficLight('красный')
tl1.running('желтый')



print('###' * 47)
print('###' * 20, 'УРОК №6  ЗАДАНИЕ №2', '###' * 20 )
print('###' * 47)

print(' ')
print('***' * 22, '  ООП  ', '***' * 22)
print(' ')


# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.



class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self._length
        wid = self._width
        w = self.weight
        dep = self.depth
        total = leng * wid * w * dep / 1000
        return print(f"Масса асфальта\n {leng} м * {wid} м * {w} кг * {dep} см = ", total, "т")


r = Road(20, 5000, 25, 5)
r.mass()


print('###' * 47)
print('###' * 20, 'УРОК №6  ЗАДАНИЕ №3', '###' * 20 )
print('###' * 47)

print(' ')
print('***' * 22, '  ООП  ', '***' * 22)
print(' ')

#
# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position('Иван', 'Иванов', 'QA', '100000', '20000')
print(p.get_full_name(), p.get_total_income())



print('###' * 47)
print('###' * 20, 'УРОК №6  ЗАДАНИЕ №4', '###' * 20 )
print('###' * 47)

print(' ')
print('***' * 22, '  ООП  ', '***' * 22)
print(' ')

# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Разгоняемся до {speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Останавливаемся')

    def turn(self, direction: str):
        if self.speed > 0:
            print(f'Поворачиваем {direction}')
        else:
            print('Не можем повернуть - мы стоим на месте')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def test_drive(vehicle):
    print(f"Тест-драйв {'полицейского' if vehicle.is_police else 'гражданского'} автомобиля {vehicle.name}, цвет {vehicle.color}")
    vehicle.go(40)
    vehicle.show_speed()
    vehicle.turn('направо')
    vehicle.stop()
    vehicle.show_speed()
    vehicle.turn('налево')
    vehicle.go(60)
    vehicle.show_speed()
    vehicle.go(120)
    vehicle.show_speed()
    vehicle.stop()
    print("Тест-драйв окончен", end="\n\n")


car = Car('белый', 'Mercedes', False)
test_drive(car)

towncar = TownCar('синий', 'Lincoln Towncar')
test_drive(towncar)

ferrari = SportCar('красный', 'Ferrari F430')
test_drive(ferrari)

rio = WorkCar('чёрный', 'KIA RIO')
test_drive(rio)

mondeo = PoliceCar('оранжевый', 'Ford Mondeo')
test_drive(mondeo)

print('###' * 47)
print('###' * 20, 'УРОК №6  ЗАДАНИЕ №5', '###' * 20 )
print('###' * 47)

print(' ')
print('***' * 22, '  ООП  ', '***' * 22)
print(' ')


# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title= 'Somewhat'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):

    def draw(self):
        self.title = 'pen'
        print(f'We are drawing by {self.title}')


class Pencil(Stationary):

    def draw(self):
        self.title = 'pencil'
        print(f'We are drawing by {self.title}')


class Handle(Stationary):

    def draw(self):
        self.title = 'handle'
        print(f'We are drawing by {self.title}')


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()