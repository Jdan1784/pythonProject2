# Итоговый проект 3.10

integer = int(input('Введите целое число: '))
remainder = []

while True:
    remainder.append(integer % 10)
    integer = integer // 10
    print(integer)
    print(remainder)
    if integer == 0:
        break
print(5 in remainder) or (7 in remainder) or (9 in remainder)

print("---")

# Как должно быть, но хуйня.

number = 111115222222222222225
digitToFind = 5

num = number
while num > 0:
   digit = num % 10
   if digit == digitToFind:
       print(f"{digitToFind} is in number {number}")
       break
   num = int(num / 10)

print("---")

# Вебинар. Условные конструкции и циклы.

a = int(input('Input your lucky number: '))
b = int(input('Input your second lucky number: '))

if a == 10:
    print("You're winner")
elif b == 5:
    print("You're winner")
else:
    print("You're looser")

# Циклы

# While

count = 10 # Здесь цикл будет идти столько раз сколько указано в count.
while count != 0: #  Пока count не = 0 будет выполняться.
    count -= 1 # Через каждое прохождение цикла уберается один count.
    print(count)
    print("Hello world")

# For

# Можно сделать так ...
a = [1, 'Hello', 5]
count = len(a) # Пременная принимает длинну этого списка.
while count != 0:
    count -= 1
    print(a[count])

print("---")

# Но так компактнее, но сложнее для понимания.
a = [1, 'Hello', 5]
for x in a: # For может применяться только итерируемому объекту(т.е. к объекту, который можно посчитать).
    print(x)

print("---")

a = [1, 'Hello', 3, 5, 6]
for x in range(1, 4, 2):
    print(a[x])

print("---")

a = ['hello', 'world', 5, 6, ['my list', 5]]
for x in a:
    print(x)

print("---")

a = ['hello', 'world', 5, 6, ['my list', 5]]
for x in a:
    if type(x) == list: # Пробежались по списку внутри списка.
        for l in x:
            print(l)
    else: # Вывели все элементы списка и список в списке.
        print(x)




















