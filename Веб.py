# N = input('Введите целое число: ')
# print(('3' in N) or ('7' in N))

print("")

# is - проверяет являиются ли объекты одним и тем же.
a = [1,2,3]
print(id(a))

b = a
print(id(b))

print(a is b)

print("")

# Эквивалентные объекты всегда равны, но равные объекты не всегда эквивалентны.

a = [1,2,3]
b = [1,2,3]

print(a == b)# Проверяет равны ли объекты.
print(a is b)# Проверяет являются ли объекты одним и тем же.

# None - переменная которая без ничего.

print("")

# Задача

# N = input('Введите целое число: ')
# z = str(N)
# k = int(z[0])
# print(k % 2 == 0)

print("")

# Условные операторы.

is_rainy = True
if is_rainy:
    print("Брать зонт")
else:
    print("Не брать зонт")

print("")

password = "dgh36gh7"
answer = input("Введите пароль: ")
if answer == password:
    print("Пароль верен! Добро пожаловать!")
else:
    print("Вы ввели неверный пароль")

print("")

s = 5
a = 10
if a>0:
    s = s + a
else:
    s = s -a
print(s)

print("")

# Вложенные условные операторы.
# Допишем задачу с дождем.
is_rainy = True
heavy_rain = False

if is_rainy:
    if heavy_rain:
        print("Брать зонт")
    else:
        print("Надеть дождевик")
else:
    print("Не брать зонт")

print("")

# Задание 3.3.5

name = input("Введите назвоние на этикетке: ")
if "Арорат" in name:
    print("Нашлась подделка")
else:
    print(f"Вино {name} не подделка")

#ХУЕТА

# v = "Арарат"
#
# if name == v:
#     print("Вино Арарат не подделка" )
# else:
#     print("Нашлась подделка")

print("")

# Задача 3.3.6

cost = int(input("Введите цену кросовок: "))
if cost > 2500:
    print("Увы кросовки слишкомм дорогие(")
else:
    print("Вы можете купить эти кросоки!")

print("")

# Неявное приведение у булеву типу
# Провееряем к какому виду приводит тот или иной тип.

print(bool(0))
print(bool(1))
print("")
print(bool(""))
print(bool("1"))
print("")
print(bool([]))
print(bool([1]))

print("")

#Если ваша задача проверить, можно ли делить одно значение на другое и является ли делитель нулем,
# то проверку в явном виде zero != 0 делать излишне.
# # Плохо
# if zero != 0:
#     print(10 / zero)
# else:
#     print("Делить на ноль нельзя")

# # Хорошо
# if zero:
#     print(10 / zero)
# else:
#     print("Делить на ноль нельзя")

#Если вам нужно проверить, пустая строка или нет,
# то сравнивать её таким способом password == "", а уж тем более таким len(password) == 0 ни к чему.

# # Плохо
# if password == "":
#    print("Вы забыли ввести пароль")
# else:
#    ...
#
# # Очень плохо
# if len(password) == 0:
#    print("Вы забыли ввести пароль")
# else:
#    ...
#
# # Хорошо
# if not password:
#    print("Вы забыли ввести пароль")
# else:
#    ...

x = input("Введите число: ")

if x:
    x = int(x)
else:
    x = None
print(bool(x))

print("")

# Тернарный оператор.
# Синтаксис оператора.

# [on_true] if [условие] else [on_false]

# Сравниваем
# Делаем так:
a, b = 1, 2

min = a if a < b else b
print(min)

# Вместо

a, b = 1, 2

min = None

if a < b:
    min = a
else:
    min = b
print(min)

# ИЛИ

a, b = 1, 2
print(a,"больше") if a > b else print(b, "больше")

# Вместо

a ,b = 1, 2
if a > b:
    print(a, "больше")
else:
    print(b, "больше")

print("")

t = int(input("Какая сейчас температура на улице?"))

if t > 15:
    if t >= 35:
        print("Лучше остаться дома")
    else:
        print("Можете надеть летнюю одежду")
else:
    if t < -15:
        print("Необходимо надеть зимнюю одежду")
    else:
        print("Необходимо одеться потеплее")

print("")



