# Лаб2
f = open('input.txt', 'r')
print(f.readline())
f.close()

# Лаб3
f = open('input.txt', 'r')
print(f.readlines())
f.close()

# Лаб4
with open('input.txt') as f:
    print(f.readlines())

# Лаб5
with open('input.txt') as f:
    for line in f:
        print(line)

# Лаб6
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)

# Лаб7
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')

# Лаб8
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'[Папка {catalog[0]} содержит:')
    print(f'[Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs('C:/Users/Gigabyte/Desktop/Pictures/Cats')

# Лаб9
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

# Лаб10
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)

# Сам1
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

# Сам2
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

# Сам3
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

# Сам4
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

# Сам5
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