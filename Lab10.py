# Лаб1
from functools import lru_cache

@lru_cache(None)
def fiboonacci(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    return fiboonacci(n-1) + fiboonacci(n-2)

if __name__ == '__main__':
    print(fiboonacci(100))

# Лаб2
def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 130:
            age = 'Недопустимый возраст'
        input_func(name, age)

    return output_func

@check
def personal_info(name,age):
    print(f"Name: {name}  Age: {age}")

if __name__ == '__main__':
    personal_info('Владимир', 38)
    personal_info('Александр', -5)
    personal_info('Петр', 138,15,48,2)

# Лаб3
def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i] *15)//10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print('Вся информация обработана')

if __name__ == '__main__':
    data([1,15, 'Hello', 'i', 'try', 'to', 'crash', 'your','site', 38, 45])

# Лаб4
class NegativeValueException(Exception):
    pass

def check_name(name):
    if len(name)>10:
        raise NegativeValueException('Длина более 10 символов')
    else:
        print('Успешная регистрация')

if __name__ == '__main__':
    name = '12345678910'
    check_name(name)

# Лаб5
class SiteChecker:
    def __init__(self, func):
        print('> Класс SiteChecker метод __init__ успешный запуск')
        self.func = func

    def __call__(self):
        print('> Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасного выключения')

@SiteChecker
def site():
    print('Усердная работа сайта')

if __name__ == '__main__':
    print('>> Сайт запущен')
    site()
    print('>> Сайт выключен')

# Сам1
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения {func.__name__}: {execution_time} секунд")
        return result
    return wrapper

@measure_time
def fibonacci():
    fib1 = fib2 = 1
    print(fib1, fib2, end=' ')

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')
    print()


if __name__ == '__main__':
    fibonacci()

# Сам2
def read_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                raise ValueError("Файл пустой")
            print(f"Содержимое файла: {content}")
    except FileNotFoundError:
        print("Файл не найден")
    except ValueError as e:
        print(e)

if __name__ == '__main__':

    print("Пустой файл:")
    read_file_content('empty.txt')

    print("\nНе пустой файл:")
    read_file_content('input.txt')

# Сам3
def add_two():
    try:
        user_input = input()
        number = float(user_input)
        result = 2 + number
        print(f"2 + {number} = {result}")
        return result
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    add_two()
    add_two()

# Сам4
# Создаем класс декоратора
class AddTen:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs) + 10
        return result

# Создаем две функции, которые будут использовать наш декоратор
@AddTen
def minus(a, b):
    return a - b

@AddTen
def divide(a, b):
    return a / b

# Тестируем функции
print("minus(10, 3):", minus(10, 3))
print("divide(20, 4):", divide(20, 4))

# Сам5
class MyError(Exception):
    pass

# Первая функция
def check_age(age):
    if age < 0:
        raise MyError("Возраст не может быть отрицательным")
    return f"Возраст: {age}"

# Вторая функция
def check_name(name):
    if len(name) < 2:
        raise MyError("Имя слишком короткое")
    return f"Имя: {name}"

# Тестируем
try:
    print(check_age(25))
    print(check_age(-5))
except MyError as e:
    print("Ошибка:", e)

try:
    print(check_name("Анна"))
    print(check_name("А"))
except MyError as e:
    print("Ошибка:", e)
