#Логические операторы
weight = 56
age = 23
res = age > 24 and weight == 56 # age не больше 24? = 0. weight = 56? = 1. 0 * 1 = 0
print(res)

weight = 56
age = 23
res = age > 21 or not weight == 56 # age больше 21? = 1. weight  не = 56! = 0. 1 + 0 = 1
print(res)

print("")

a = '23'
b = int(a)
print(type(a), type(b))

print("")

# name = input('введите имя: ')
# age = int(input('введите ваш возраст: '))
# print(name, age)

print("")

# staring - строки
# '' ""
a = '23'
b = '34'
c = a + b # Происходид конкантинация(объединение)  строк.
print(c)

print("")

# f - строки - это динамические передачи параметров или переменных.
name = 'Ivan'
age = 23
print (f'привет, меня зовут, {name}, мне {age} лет')

print("")

# индексы и методы == функции строк
# срез строк [start:stop:step] или [начальное:конечное:шаг]
a = 'hello'# Хочу сделать заглавную букву 'H'
a_mod = a[0].upper() # Нам нужно вытащить первый ээлемент. upper преобразовует в верхний регистр.
b = a[1::]
c = a_mod + b
print(c)

# Допустим задача
# a = input('Введите имя ')
# a_mod = a[0].upper()
# b = a[1::].lower()
# c = a_mod + b
# print(f'мы поменяли  в верхний регистр первую букву {c}')

print("")

a = 'hello'
print(a[::-1])# Выдает в обратном порядке.
print(a[-1::])# Выдает последнюю букву.

print("")

# len - показывает размер строки.
a = 'hello'
print(len(a))

print("")

# Список list
#  массив != список
data_1 = ['hello', True, [1,2,3]]
a = data_1[0]

print("")

# список list
data = [2, 34, 45, 56, 6]
for item in data:
    if item % 2 == 0:
        print(item)

print("")

# Задача
# num = int(input('input number '))
# data = []
# while num != 0:
#     data. append(num)
#     num = int(input('input number '))
# data.sort()
# print(data)

print("")

data = [3,4,5]
print(len(data))

print("")

# списки + строки
# генерируем пароль

import random
a = 'QWERTYUIOPASDFGHJKLZXCVBNM'
b = 'qwertyuiopasdfghjklzxcvbnm'
c = '0123456789'
d = '{}[],!/-()'
all = a + b + c + d # Делаем конкантинацию(складываем) всех строк.
length = 13 # Установили длинну пароля 13.
password = ''.join(random.sample(all, length)) # sample - делает выборку из элементов.
# join - отвечает за объединение списка строк, при помощи указателя.
print(password)

data = ['hello', 'bye', 'hello1']
print(*data[2::]) # Функация '*' уберает скобки.

print("")

# словарь {ключ:значение}
users_list = [
    ['+1234', 'Tom'],
    ['+234', 'Bob']
]
users_dict = dict(users_list)
print(users_dict)

print("")

users_dict = {
    '+123456': 'Tom',
    '1254678': 'Kate',
    '46546822': 'Bob'
}
users_dict_mod = users_dict['+12334'] = 'Bill'
print(users_dict['+123456'])
print(users_dict)

print("")

users_dict = {
    '+123456': 'Tom',
    '1254678': 'Kate',
    '46546822': 'Bob'
}
# Способ 1
for key in users_dict:
    print(f'phone:{key} Users: {users_dict[key]}')
# Способ 2
for key, value in users_dict.items():
    print(f'phone: {key} Users: {value}')
# Еще один. Выводит ключи.
for key in users_dict.keys():
    print(key)

print("")

a = 'random' # Получить на выходе mod.
a_mad = a[3::]
b = a_mad[::-1]
print(b)

#ИЛИ

a = 'random' # Получить на выходе mod.
a_mod = a[:2:-1]
print(a_mod)
