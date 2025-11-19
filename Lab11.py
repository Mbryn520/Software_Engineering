# Лаб1
numbers = [0,1,2,3,4,5]
for item in numbers:
    print(item)

# Лаб2
class CountDown:
    def __init__(self, start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -=1
        if self.count < 0:
            raise StopIteration
        return self.count

if __name__== "__main__":
    counter = CountDown(5)
    for i in counter:
        print(i)

# Лаб3
a = [i**2 for i in range(1,5)]

print('a -', a)
for i in a:
    print(i)

print('iter(a) -', iter(a))
for i in a:
    print(i)

# Лаб4
b = (i**2 for i in range(1,5))
print(b)
print('first')
for i in b:
    print(i)
print('second')

for i in b:
    print(i)

# Лаб5
def countdown(count):
    while count>=0:
        yield count
        count -=1

if __name__== '__main__':
    counter = countdown(5)
    for i in counter:
        print(i)

# Сам1
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fib(200):
    result = num
print(result)

# Сам2
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

with open('fib.txt', 'w') as f:
    for num in fib(200):
        f.write(f'{num}\n')