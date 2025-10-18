# Лаб1
request = int(input('Введите номер кабинета: '))

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False},
}

response = dictionary.get(request)
if not response:
    response = dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)

# Лаб2
from pprint import pprint

my_dict = {'first': 'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name='Михаил', age=31, weight=70, eyes_color='blue')
pprint(my_dict)

# Лаб3
input_string= "HelloWorld"
result = tuple(input_string)
print(result)
print(list(result))

# Лаб4
def personal_info(name, age, company='unnamed'):
    print(f"Имя: {name}  Возраст: {age}  Компания: {company}")

tom = ("Григорий", 22)
personal_info(*tom)

bob = ("Георгий", 41, "Yandex")
personal_info(*bob)

# Лаб5
def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort((5, 5, 3, 1, 9)))
    print(tuple_sort((5, 5, 2.1, '1', 9)))

Сам1
numstr = input()
numlist = list(map(int, numstr.split()))
numtuple = tuple(numlist)

print(numlist)
print(numtuple)

# Сам2
def deleteelem(tpl, elem):

    tlist = list(tpl)

    if elem in tlist:
        tlist.remove(elem)

    return tuple(tlist)

testlist = [
    ((1, 2, 3), 1),
    ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
    ((2, 4, 6, 6, 4, 2), 9)
]
for tpl, elem in testlist:
    result = deleteelem(tpl, elem)
    print(result)

# Сам3
def countnumbs(digits_string):
    digits = [int(char) for char in digits_string]

    unidigits = sorted(set(digits))

    pairs = []
    for digit in unidigits:
        count = digits.count(digit)
        pairs.append((count, digit))

    pairs.sort(reverse=True)

    top_three = {}
    for count, digit in pairs[:3]:
        top_three[digit] = count

    return top_three

test_string = str(input())
result = countnumbs(test_string)
print(result)

# Сам4
def newlist(tpl, elem):

    if tpl.count(elem) == 0:
        return ()
    elif tpl.count(elem) == 1:
        return tpl[tpl.index(elem):]
    else:
        first_index = tpl.index(elem)
        second_index = tpl.index(elem, first_index + 1)
        return tpl[first_index:second_index + 1]

test_cases = [
    ((1, 2, 3), 8),
    ((1, 8, 3, 4, 8, 8, 9, 2), 8),
    ((1, 2, 8, 5, 1, 2, 9), 8)
]

for tpl, elem in test_cases:
    result = newlist(tpl, elem)
    print(result)

# Сам5
def srnum(numbers):
    return sum(numbers) / len(numbers)

print(srnum([10, 20, 30, 40, 50]))
print(srnum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(srnum([2.5, 3.7, 1.8, 4.2, 5.1]))

