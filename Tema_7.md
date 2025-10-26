# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
- Малых Марина Игоревна
- ИВТ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |


знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- Ротенштрайх Т.В.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Lab1.png)
## Вывод

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().
```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Lab2.png)
## Вывод

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().
```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Lab3.png)
## Вывод

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().
```python
with open('input.txt') as f:
    print(f.readlines())
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Lab4.png)
## Вывод

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().
```python
with open('input.txt') as f:
    for line in f:
        print(line)
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Lab5.png)
## Вывод

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.
```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Lab6.png)
## Вывод

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что изменения вампинирования сохранилась в файле.
```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Lab71.png)
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Lab72.png)
## Вывод

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'[Папка {catalog[0]} содержит:')
    print(f'[Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs('C:/Users/Gigabyte/Desktop/Pictures/Cats')
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Lab8.png)
## Вывод

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст:
Приветствие
Спасибо
Извините
Пожалуйста
До свидания
Ты готов?
Как дела?
С днем рождения!
Удача!
Я тебя люблю.
Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных
```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Lab9.png)
## Вывод

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
- № - номер по порядку (от 1 до 300);
- Секунда – текущая секунда на вашем ПК;
- Микросекунда – текущая миллисекунда на часах.
Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Lab10.png)
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Lab101.png)
## Вывод

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
```python
from collections import Counter

def word_count(file):
    result = 0
    with open(file, 'r', encoding='utf-8') as file:
        data = file.read()
        lines = data.split()
        result += len(lines)
    return result

def most_said(file):
    with open(file, 'r', encoding='utf-8') as file:
        data = file.read()
        split_it = data.split()
        most_occur = Counter(split_it).most_common(4)
    return most_occur

print(word_count('input.txt'), most_said('input.txt'))
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Sam1.png)
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Sam12.png)
## Вывод

## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
```python
def record_expense(filename):
    while True:
        expense_item = input("Введите название расхода или 'отмена' для выхода: ")
        if expense_item.lower() == 'отмена':
            break
        expense_amount = input("Введите данные расходов:")

        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"{expense_item}: {expense_amount}\n")

    print()
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())

filename = 'input.txt'
record_expense(filename)
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Sam2.png)
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Sam22.png)
## Вывод

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
```python
def analyze_text(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            letter_count = sum(c.isalpha() for c in text)
            word_count = len(text.split())
            line_count = text.count('\n') + 1
            print(f"Input file contains:\n{letter_count} letters\n{word_count} words\n{line_count} lines")
    except FileNotFoundError:
        print("Файл не найден.")
analyze_text('input.txt')
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Sam3.png)
## Вывод

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam,
Exam, ExaM, EXAM и exAm должны быть заменены на ****.
-  Запрещенные слова:
hello email python the exam wor is
```python
def censor_sentence(text):
    with open('input.txt', 'r', encoding='utf-8') as file:
        bad_words = file.read().split()
    words = text.split()
    censored_words = []
    for word in words:
        lowercase_word = word.lower()
        for bword in bad_words:
            if (lowercase_word.find(bword) >= 0):
                censored_word = lowercase_word.replace(bword, '*' * len(bword))
                censored_words.append(censored_word)
                break
        else:
            censored_words.append(word)
    censored_sentence = ' '.join(censored_words)
    print(censored_sentence)

text = "Hello, world! Python IS the programming language of thE future. My EMAIL is .... PYTHON is awesome!!!!"
censor_sentence(text)
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Sam4.png)
## Вывод

## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
```python
def count_vowels(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    vowels = 'аеёиоуыэюя'
    vowel_count = {}
    for char in text.lower():
        if char in vowels:
            if char not in vowel_count:
                vowel_count[char] = 0
            vowel_count[char] += 1

    return vowel_count

vowel_counts = count_vowels('input.txt')
total_vowels = 0

for vowel, count in vowel_counts.items():
    print(f"'{vowel}': {count}")
    total_vowels += count

print(f"\nОбщее количество гласных: {total_vowels}")
```
### Результат
![](https://github.com/Mbryn520/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pics7/Sam5.png)
## Вывод
