# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
- Малых Марина Игоревна
- ИВТ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |


знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- Ротенштрайх Т.В.

## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.
```python
class Car: #создаем класс "Car"
    def __init__(self, make, model): #Определяем атрибуты марку и модель
        self.make = make #Присваиваем марку
        self.model = model #Присваиваем модель

my_car = Car("Toyota", "Corolla") #Создаем объект my_car класса Car с атрибутами
```
## Вывод

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Car: #создаем класс "Car"
    def __init__(self, make, model): #Определяем атрибуты марку и модель
        self.make = make #Присваиваем марку
        self.model = model #Присваиваем модель

    def drive(self): #Определяем метод drive
        print(f"Driving the {self.make} {self.model}") #метод выводит сообщение с атрибутами

my_car = Car("Toyota", "Corolla") #Создаем объект my_car класса Car с атрибутами
my_car.drive() #вызываем метод drive для my_car
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pics8/Lab2.png)
## Вывод

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться.
```python
class Car: #создаем класс "Car"
    def __init__(self, make, model): #Определяем атрибуты марку и модель
        self.make = make #Присваиваем марку
        self.model = model #Присваиваем модель

    def drive(self): #Определяем метод drive
        print(f"Driving the {self.make} {self.model}") #метод выводит сообщение с атрибутами

my_car = Car("Toyota", "Corolla") #Создаем объект my_car класса Car с атрибутами
my_car.drive() #вызываем метод drive для my_car

class ElectricCar(Car): #определяем новый класс который наследуется от класса Car
    def __init__(self, make, model, battery_capacity): #вызов конструктора родительского класса с помощью super
        super().__init__(make, model)
        self.battery_capacity = battery_capacity #новый атрибут

    # usage
    def charge(self): #определяем метод charge
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh") #выводит сообщение с атрибутами

my_electric_car = ElectricCar("Tesla", "Model S", 75) #создаем новый объект класса electriccar
my_electric_car.drive() #вызываем унаследованный метод
my_electric_car.charge() #вызываем метод
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pics8/Lab3.png)
## Вывод

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Car: #создаем класс "Car"
    def __init__(self, make, model): #Определяем атрибуты марку и модель
        self._make = make #Присваиваем марку (защищенный артибут)
        self.__model = model #Присваиваем модель (приватный атрибут)

    def drive(self): #Определяем метод drive
        print(f"Driving the {self._make} {self.__model}") #метод выводит сообщение с атрибутами

my_car = Car("Toyota", "Corolla") #Создаем объект my_car класса Car с атрибутами
print(my_car._make) #доступ к защищенному атрибуту
my_car.drive() #вызываем метод drive для my_car
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pics8/Lab4.png)
## Вывод

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
# Определение общего класса Shape
class Shape:
    def area(self):
        pass

# Определение класса Rectangle, унаследованного от Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
# Метод для подсчета площади прямоугольника
    def area(self):
        return self.width * self.height

#Определение класса Circle, унаследованного от Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
# Метод для подсчета площади круга
    def area(self):
        return 3.14 * self.radius * self.radius
# Создание экземпляров классов Rectangle и Circle
rectangle = Rectangle(2, 10)
circle = Circle(3)

# Помещение фигур в массив
shapes = [rectangle, circle]

# Вывод площади каждой фигуры в массиве
for shape in shapes:
    print(shape.area())
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pics8/Lab5.png)
## Вывод

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"Это {self.name}")

the_animal = Animal("Кошка")
the_animal.sound()
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pics8/Sam1.png)
## Вывод

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Гав!"

class Cat(Animal):
    def sound(self):
        return "Мяу!"

cat = Cat("Кошка")
dog = Dog("Собака")

print(f"{dog.name} говорит {dog.sound()}")
print(f"{cat.name} говорит {cat.sound()}")
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pics8/Sam2.png)
## Вывод

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Гав!"

class Cat(Animal):
    def sound(self):
        return "Мяу!"

class Pig(Animal):
    def sound(self):
        return "Хрю!"

dog = Dog("Собака")
cat = Cat("Кошка")
pig = Pig("Свинья")

print(f"{dog.name} говорит {dog.sound()}")
print(f"{cat.name} говорит {cat.sound()}")
print(f"{pig.name} говорит {pig.sound()}")
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pics8/Sam3.png)
## Вывод

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Animal:
    def __init__(self, name):
        self._name = name  #

    def sound(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

class Dog(Animal):
    def sound(self):
        return "Гав!"

class Cat(Animal):
    def sound(self):
        return "Мяу!"

dog = Dog("Собака")
cat = Cat("Кошка")

print(f"{dog.get_name()} говорит {dog.sound()}")
print(f"{cat.get_name()} говорит {cat.sound()}")

cat.set_name("Пушок")
print(f"{cat.get_name()} говорит {cat.sound()}")
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pics8/Sam4.png)
## Вывод

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Гав!"

class Cat(Animal):
    def sound(self):
        return "Мяу!"

def animal_sound(animal):
    print(f"{animal.name} говорит {animal.sound()}")

dog = Dog("Бобик")
cat = Cat("Мурка")

animals = [dog, cat, Dog("Шарик"), Cat("Пушок")]

for animal in animals:
    animal_sound(animal)
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pics8/Sam5.png)
## Вывод

## Общий вывод по теме
