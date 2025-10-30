# Лаб1
class Car: #создаем класс "Car"
    def __init__(self, make, model): #Определяем атрибуты марку и модель
        self.make = make #Присваиваем марку
        self.model = model #Присваиваем модель

my_car = Car("Toyota", "Corolla") #Создаем объект my_car класса Car с атрибутами

# Лаб2
class Car: #создаем класс "Car"
    def __init__(self, make, model): #Определяем атрибуты марку и модель
        self.make = make #Присваиваем марку
        self.model = model #Присваиваем модель

    def drive(self): #Определяем метод drive
        print(f"Driving the {self.make} {self.model}") #метод выводит сообщение с атрибутами

my_car = Car("Toyota", "Corolla") #Создаем объект my_car класса Car с атрибутами
my_car.drive() #вызываем метод drive для my_car

# Лаб3
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

# Лаб4
class Car: #создаем класс "Car"
    def __init__(self, make, model): #Определяем атрибуты марку и модель
        self._make = make #Присваиваем марку (защищенный артибут)
        self.__model = model #Присваиваем модель (приватный атрибут)

    def drive(self): #Определяем метод drive
        print(f"Driving the {self._make} {self.__model}") #метод выводит сообщение с атрибутами

my_car = Car("Toyota", "Corolla") #Создаем объект my_car класса Car с атрибутами
print(my_car._make) #доступ к защищенному атрибуту
my_car.drive() #вызываем метод drive для my_car

# Лаб5
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

# Сам1
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"Это {self.name}")

the_animal = Animal("Кошка")
the_animal.sound()

# Сам2
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

# Сам3
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

# Сам4
class Animal:
    def __init__(self, name):
        self._name = name

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

# Сам5
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