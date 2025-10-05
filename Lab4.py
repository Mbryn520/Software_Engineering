# Лаб1
def main():
    print(2+2)
if __name__ == "__main__":
    main()

# Лаб2
def main():
    return 2+2
if __name__ == "__main__":
    print(main())

# Лаб3
def main(one, two):
    result = one + two
    return result


for i in range(5):
    x = 1
    y = 10
    answer = main(x, y)
    print(answer)

# Лаб4
def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))

    print(f"one={one}\ntwo={two}\nthree={three}")

    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(10, 0, 1, 2, -1, 0, -1, 1, 2)
    print(f"\nresult={result}")

# Лаб5
def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])

    print()

    for key in kwargs:
        print(f"{key} = {kwargs[key]}")


if __name__ == '__main__':

    main(x=[1, 2, 3], y=[3, 3, 0], z=[2, 3, 0], q=[3, 3, 0], w=[3, 3, 0])
    print()

    main(**{'x': [1, 2, 3], 'y': [3, 3, 0]})

# Лаб6
def main(**kwargs):

    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):

    return sum(data) / float(len(data))

if __name__ == '__main__':
    main(x=[1, 2, 3], y=[3, 3, 0])

# Лаб7
from for_import_lab4 import say_hello
if __name__ == "__main__":
    say_hello()

# Лаб8
import math

def main():
    value = int(input('Введите значение: '))
    print(math.sqrt(value))
    print(math.sin(value))
    print(math.cos(value))

if __name__ == '__main__':
    main()

# Лаб9
from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Сегодня {dt.today().date()}. "
        f"День недели - {dt.today().isoweekday()}"
    )
    n = int(input('Введите количество дней: '))
    today = dt.today()
    result = today + td(days=n)
    print(
    f"Через {n} дней будет {result.date()}. "
    f"День недели - {result.isoweekday()}"
    )

if __name__ == '__main__':
    main()

# Лаб10
global result

def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a * b

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5 * a * h

figure = input("1-прямоугольник, 2-треугольник: ")

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f"Площадь: {result}")


#Сам1

from datetime import datetime # Импорт класса datetime из модуля datetime для работы с датой и временем
from math import sqrt # Импорт функции sqrt (квадратный корень) из модуля математических операций math

def main(**kwargs):
    """
    Функция для вычисления длины векторов по их координатам.

    Принимает произвольное количество именованных аргументов, где каждый аргумент -
    список из двух чисел [x, y], представляющих координаты вектора.

    Args:
        **kwargs: Произвольное количество именованных аргументов вида
        имя_вектора=[координата_x, координата_y]

    Returns:
        None: Функция выводит результаты в консоль, но не возвращает значений
        """
    for key in kwargs.items():
    # Цикл по всем элементам словаря kwargs
    # Метод items() возвращает пары (ключ, значение) для каждого элемента
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
    # Вычисление длины вектора по теореме Пифагора:
    # result = √(x² + y²), где x = key[1][0], y = key[1][1]
    # **2 - возведение в квадрат
    # sqrt() - вычисление квадратного корн
        print(result)  # Вывод вычисленной длины вектора в консоль

# __name__ - специальная переменная, которая равна '__main__' когда скрипт запущен напрямую
# и имени модуля когда скрипт импортирован
if __name__ == '__main__':
    start_time = datetime.now() # datetime.now() возвращает текущие дату и время
    main(
        one=[10, 3], # Вектор "one" с координатами x=10, y=3
        two=[5, 4], # Вектор "two" с координатами x=5, y=4
        three=[15, 13], # Вектор "three" с координатами x=15, y=13
        four=[93, 53], # Вектор "four" с координатами x=93, y=53
        five=[133, 15] # Вектор "five" с координатами x=133, y=15
    )
    time_costs = datetime.now() - start_time # Вычисление времени выполнения программы = текущее - время начала
    print(f"Время выполнения программы - {time_costs}") # Вывод времени выполнения программы

#Сам2
import random
def game():

    roll = random.randint(1, 6)
    print(f"Выпало: {roll}")

    if roll == 5 or roll == 6:
        print("Вы победили")
    elif roll == 3 or roll == 4:
        print("Повторный бросок")
        game()
    elif roll == 1 or roll == 2:
        print("Вы проиграли")

if __name__ == '__main__':
    game()

# Сам3
import datetime
import time

for i in range(5):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    print(f"Текущее время: {formatted_time}")
    time.sleep(1)

# Сам4
def calculate(*args):
    return sum(args) / len(args)

if __name__ == '__main__':
    result = calculate(1, 2, 3, 4, 5)
    print(f"Среднее чисел 1, 2, 3, 4, 5: {result}")

# Сам5
from heron import heron_triangle_area

def main():

        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        c = float(input("Сторона c: "))

        area = heron_triangle_area(a, b, c)
        print(f"Площадь треугольника: {area:.2f}")

if __name__ == '__main__':
    main()