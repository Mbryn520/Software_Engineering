# Лаб1
class Ivan:
    __slots__ = ['name']
    def __init__(self, name):
        if name == 'Марина':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Марина"

person1 = Ivan('Алексей')
person2 = Ivan('Марина')
print(person1.name)
print(person2.name)

person2.surname = 'Петрова'

# Лаб2
class Icecream:
    def __init__(self, ingredient=None):
        self.base_price = 99
        if isinstance(ingredient, str):
            self.ingredient = ingredient
            self.price = self.base_price + 49
        else:
            self.ingredient = None
            self.price = self.base_price

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient} будет стоить {self.price} руб.")
        else:
            print(f"Обычное мороженое будет стоить {self.price} руб.")

icecream = Icecream()
icecream.composition()
icecream = Icecream("шоколадом")
icecream.composition()
icecream = Icecream(5)
icecream.composition()

# Лаб3
class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value): # устанавливаем значение атрибута
        self._value = value

    def get_value(self): # получаем значение
        return self._value

    def del_value(self): # удаляем атрибут
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value() # здесь мы удаляем атрибут, из-за чего у нас возникает ошибка
print(obj.get_value()) # нет доступа к удаленному атрибуту = ошибка

# Лаб4
class Mammal:
    className = 'млекопитающее'

class Dog(Mammal):
    species = 'собака'
    sounds = 'гав'
    special = 'хороший нюх'

class Cat(Mammal):
    species = 'кошка'
    sounds = 'мяу'
    special = 'хорошее зрение в темноте'

dog = Dog()
print(f"Собака это {dog.className}, но говорит {dog.sounds} и имеет {dog.special}")
cat = Cat()
print(f"Кошка это {cat.className}, но говорит {cat.sounds} и имеет {cat.special}")

# Лаб5
class Russian:
    @staticmethod
    def greeting():
        print("Привет")

class English:
    @staticmethod
    def greeting():
        print("Hello")

def greet(language):
    language.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)

# Сам1
class Tomato:
    # Статическое свойство, содержит в себе все стадии созревания
    states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}
    def __init__(self, index):
        # Динамические свойства:
        self._index = index # индекс томата (передается параметром)
        self._state = self.states['Отсутствует'] # стадия созревания (первое значение из словаря)

    def grow(self): # Томат переходит на следующую стадию созревания
        if self._state < 3:
            self._state += 1

    def is_ripe(self): # Проверка созрел ли томат
        return True if self._state == 3 else False


class TomatoBush:

    def __init__(self, num): # Создает список класса Tomato заданного количества
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    def grow_all(self): # Переход всех томатов на следующую стадию созревания
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self): # Проверка все ли томаты созрели
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self): # Очистка списка томатов после сбора
        self.tomatoes = []


class Gardener:
    # Динамические свойства:
    def __init__(self, name, plant):
        self.name = name # Имя садовника (параметр)
        self._plant = plant # Растение (Объект TomatoBush)

    def work(self):
        self._plant.grow_all() # Садовник работает и растения растут

    def harvest(self):
        print("* Смотрим, созрели ли плоды *")
        if self._plant.all_are_ripe(): # Если все томаты созрели то собираем
            print("Помидоры созрели, урожай собран.")
            self._plant.give_away_all()
        else:
            print("Подождите, еще не все помидоры созрели!")

    @staticmethod
    def knowledge_base():
        print("Справка")
        print("Садоводство — это отрасль растениеводства, которая занимается выращиванием многолетних плодовых, ягодных и декоративных культур.")
        print("Садовод должен ухаживать за растениями, обеспечивать им оптимальные условия для роста и созревания.")
        print("Помидор имеет 4 стадии: 0 - отсутствует, 1 - цветение, 2 - зеленый, 3 - красный.")
        print("Ухаживайте за помидорами и получайте результат.")
        print("************")

# Тесты
# Вызов справки по садоводству
Gardener.knowledge_base()
# Создание объектов классов TomatoBush и Gardener
bush = TomatoBush(5)
gardener = Gardener('Марина', bush)
# Уход за кустом
gardener.work()
# Сбор не спелого урожая и продолжение ухода
gardener.harvest()
gardener.work()
gardener.work()
# Сбор спелого урожая
gardener.harvest()