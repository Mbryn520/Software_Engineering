#Лаб1
set_1 = {'White', 'Black', 'Red', 'Pink'}
set_2 = {'Red', 'Green', 'Blue', 'Red'}
print('1', set_1 - set_2)

set_1 = {'White', 'Black', 'Red', 'Pink', 'Black', 'White'}
set_2 = {'Red', 'Green', 'Blue', 'Red'}
print('2', set_1 - set_2)

set_1 = {'White', 'Black', 'Red', 'Pink', 'Red', 'Red'}
set_2 = {'Red', 'Green', 'Red', 'Red', 'Red'}
print('3', set_1 - set_2)

# Лаб2
a = set('abcdefg')
print(a)
for i in range(1, 5):
    a.add(i)
print(a)

a = frozenset('abcdefg')
print(a)
for i in range(1, 5):
    a.add(i)
print(a)

# Лаб3
def replace(input_list):
    memory = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = memory

    return input_list

print(replace([1, 2, 3, 4, 5]))

# Лаб4
a = [12, 54, 32, 57, 843, 2346, 765, 75, 25, 234, 756, 23]
print(a[2:6])

# Лаб5
def useless(lst):
    return max(lst) / len(lst)

print(useless([3, 5, 7, 3, 33]))
print(useless([-12.5, 54, 77.3, 0, -36, 98.2, -63, 21.7, 47, -89.6]))
print(useless([-25.8, 86, 12.5, -56, 73.2, 0, 43, -91.5, 65.9, -7]))

# Лаб6
superheroes = ['superman', 'spiderman', 'batman']

nikolay, vasiliy, ivan = superheroes

print('Николай - ', nikolay)
print('Василий - ', vasiliy)
print('Иван - ', ivan)

# Лаб7
a = [-25.8, 86, 12.5, -56, 73.2, 0, 43, -91.5, 65.9, -7]
a.sort()
print('Отсортированный список:\n', a)
a.pop(0)
print('Отсортированный список без наименьшего элемента:\n', a)

# Лаб8
from random import randint

def list_maker():
    a = [randint(1, 100)] * randint(3, 10)
    return a

if __name__ == '__main__':
    result = []
    for i in range(randint(1, 5)):
        result.append(list_maker())

    print(result)

# Лаб9
def superset(set_1, set_2):
    if set_1 > set_2:
        print(f'Объект {set_1} является чистым супермножеством')
    elif set_1 == set_2:
        print('Множества равны')
    elif set_1 < set_2:
        print(f'Объект {set_2} является чистым супермножеством')
    else:
        print('Супермножество не обнаружено')

if __name__ == '__main__':
    superset({1, 8, 3, 5}, {3, 5})
    superset({1, 8, 3, 5}, {5, 3, 8, 1})
    superset({3, 5}, {5, 3, 8, 1})
    superset({90, 100}, {3, 5})

# Лаб10
my_list = [2, 5, 8, 3]
print(my_list[::-1])


# Сам1
visits = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,
          1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666,
          5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,
          5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987,
          3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]

total = len(visits)
univisitors = len(set(visits))
uniworkers = list(set(visits))
counts = []

for worker in uniworkers:
    count = 0
    for visit in visits:
        if visit == worker:
            count += 1
    counts.append(count)

maxcount = max(counts)
maxindex = counts.index(maxcount)
mostworker = uniworkers[maxindex]

print(total)
print(univisitors)
print(mostworker)

# Сам2
results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
           27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

sortres = sorted(results)
top3 = sortres[:3]
bad3 = sortres[-3:]
results10 = sortres[9:]

print(top3)
print(bad3)
print(results10)

# Сам3
from math import *
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]


a_min = min(one)
b_min = min(two)
c_min = min(three)


a_max = max(one)
b_max = max(two)
c_max = max(three)

p_min = (a_min + b_min + c_min) / 2
p_max = (a_max + b_max + c_max) / 2

plmin = sqrt(p_min * (p_min - a_min) * (p_min - b_min) * (p_min - c_min))
plmax = sqrt(p_max * (p_max - a_max) * (p_max - b_max) * (p_max - c_max))

print(plmin)
print(plmax)

# Сам4
gr1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
gr2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
gr3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

i = 0
while i < len(gr1):
    if gr1[i] == 2:
        gr1.pop(i)
    elif gr1[i] == 3:
        gr1[i] = 4
        i += 1
    else:
        i += 1

i = 0
while i < len(gr2):
    if gr2[i] == 2:
        gr2.pop(i)
    elif gr2[i] == 3:
        gr2[i] = 4
        i += 1
    else:
        i += 1

i = 0
while i < len(gr3):
    if gr3[i] == 2:
        gr3.pop(i)
    elif gr3[i] == 3:
        gr3[i] = 4
        i += 1
    else:
        i += 1

print(gr1)
print(gr2)
print(gr3)

# Сам5
list1 = [1, 1, 3, 3, 1]
list2 = [5, 5, 5, 5, 5, 5, 5, 5]
list3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def newlist(lst):
    resset = set()
    for num in set(lst):
        count = lst.count(num)
        resset.add(num)
        for i in range(2, count + 1):
            resset.add(str(num) * i)
    return resset

set1 = newlist(list1)
set2 = newlist(list2)
set3 = newlist(list3)

print(set1)
print(set2)
print(set3)