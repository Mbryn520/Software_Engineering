# Лаб1
one = int(input('Введите значение первой переменной: '))
two = int(input('Введите значение второй переменной: '))

if one == two:
    print('Выполняется')
else:
    print('Не выполняется')

# Лаб2
one = int(input('Введите значение переменной: '))
if one < 0:
    print('Переменная меньше 0')
elif 0 < one < 10:
    print('Переменная больше 0 и меньше 10')
else:
    print('Переменная больше 10')

# Лаб3
numbers = [1, 3, 4, 6, 8, 9]
value = int(input('Введите значение переменной: '))
if value in numbers:
    print('Переменная есть в данном массиве')
else:
    print('Переменной нет в этом массиве')

# Лаб4
numbers = [1, 3, 4, 6, 8, 9, 15, 16, 73, 321, 322]
value = int(input('Введите значение переменной: '))
if value in numbers:
    if value % 2 == 0:
        print('Переменная четная и есть в массиве numbers')
    else:
        print('Переменная нечетная и есть в массиве numbers')
else:
    print(f"Переменной нет в массиве numbers и она равна {value}")

# Лаб5
for i in range(10):
    print('i = ', i)
    if i == 0:
        i += 2
    if i == 1:
        continue
    if i == 2 or i == 3:
        print('Переменная равна 2 или 3')
    elif i in [4, 5, 6]:
        print('Переменная равна 4,5 или 6')
    else:
        break

# Лаб6
string = 'Привет всем изучающим Python!'
value = input()
for i in string:
    if i == value:
        index = string.find(value)
        print(f"Буква '{value}' есть в строке под {index} индексом")
        break
else:
    print(f"Буквы '{value}' нет в указанной строке")

# Лаб7
value = 100
for i in range(10, -1, -1):
    value -= i
    print(i, value)

# Лаб8
value = 0
while value < 100:
    if value == 0:
        value += 10
    elif value // 5 > 1:
        value *= 5
    else:
        value -= 5
    print(value)

# Лаб9
value = 0
for i in range(10):
    for j in range(10):
        if i != j:
            value += j
        else:
            pass
print(value)

# Лаб10
even_array = [2, 4, 6, 8, 9]
flag = False
for value in even_array:
    if value % 2 == 1:
        flag = True

if flag is True:
    print('В массиве есть нечетное число')
else:
    print('В массиве все числа четные')

# Сам1
x=1
for _ in range(2):
    x *= 5
    x += 1
print(x)

# Сам2
a = "Hello World"
for i in range(len(a)-1, -1, -1):
    print(a[i])

# Сам3
n = int(input())
if n <= 3:
    print("от 0 до 3 включительно")
elif n>= 4 and n < 6:
    print("от 3 до 6")
elif n >=6 and n <=10 :
    print("от 6 до 10 включительно")
else:
    print("Число не в диапазоне от 0 до 10")

# Сам4
s = input("Введите предложение: ")

print("Длина:", len(s))
print("В нижнем регистре:", s.lower())

count = 0
for letter in s.lower():
    if letter in 'aeiou':
        count += 1
print("Гласных:", count)
new = s.replace('ugly', 'beauty')
print("После замены:", new)
print("Начинается с The:", s.startswith('The'))
print("Заканчивается на end:", s.endswith('end'))

# Сам5
string = 'hello'
values = [0, 2, 4, 6, 8, 10]
counter = 0
while 'world' not in string:
    memory = string
    if counter in values:
        string = string + 'world'
    print(string)
    if counter < 10:
        string = memory
        counter += 1