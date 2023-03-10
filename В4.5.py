# В4.5. Замыкания и декоратторы

# Функция высшего порядка — в программировании это функция, принимающая в качестве
# аргументов другие функции или возвращающая другую функцию в качестве результата.

# Мы можем передавать функции как параметры:
# def my_func(inside_func):
#     ...
#     inside_func() # Вызов функции принятой в качестве аргумента.
#     ...

# Можем возвращать как результат:
# def a():
#     def b():
#         pass
#     return b

# Сделаем функцию, которая будет выполнять принимаемую функцию дважды:

def twice_func(inside_func):
    """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
    inside_func()
    inside_func()

def hello():
    print("Hello")

test = twice_func(hello)

print("---")

# Замыкание функций.

# Замыкание в программировании — это функция, в теле которой присутствуют ссылки на переменные,
# объявленные вне тела этой функции в окружающем коде и не являющиеся её аргументами.

# Сделаем функцию, которая будет возвращать функцию, всегда прибавляющую одно и тоже число x:

def make_adder(x):
    def adder(n):
        return x + n # Захват переменной "x" из nonlocal области.
    return adder # Возвращение функции в качестве результата.
# Функция, которая будет к любому числу прибавлять пятёрку.
add_5 = make_adder(5)
print(add_5(10))
print(add_5(100))

print('---')

# Декораторы

# Декораторы предназначены для подключения любого дополнительного поведения к основной функции,
# называемой декорируемой функцией, которое может выполняться до, после или даже вместо основной
# функции. При этом исходный код декорируемой функции никак не затрагивается.

# def my_decorator(a_function_to_decorator):
#     def wrapper():
#         recult = a_function_to_decorator()
#         return recult
#     return wrapper

# Давайте посмотрим на примере, как добавить дополнительное поведение к основной функции.

def my_decorator(a_function_to_decorate):
# Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
# каждый раз при вызове оригинальной функции, а не только один раз.
    def wrapper():
    # Здесь поместим код, которые будет выполняться до вызова, потом вызов
    # оригинальной функции, потом код после вызова
        print("Я буду выполне до основного вызова!")

        result = a_function_to_decorate() # Не забываем вернуть значение исходной функции

        print("Я буду выполнен после основного вызова!")
        return result
    return wrapper()

# def my_function():
#     print("Я - оборачиваемая функция!")
#     return 0
#
# print(my_function())
#
# decorated_funtcion = my_decorator(my_function) # Декорирование функции.
# print(decorated_funtcion())

print('---')

# Задание 4.5.1
import time

N = 100


def decorator_time(fn):
   def wrapper():
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       return dt
   return wrapper


def pow_2():
   return 10000000 ** 2


def in_build_pow():
   return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

mean_pow_2 = 0
mean_in_build_pow = 0
for _ in range(N):
   mean_pow_2 += pow_2()
   mean_in_build_pow += in_build_pow()

print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / N:.10f}")

print('---')

# «Синтаксический сахар»

# Пользоваться им можно так:

@my_decorator
def my_function():
    pass

# При этом будет происходить все то же самое, аналогичное.

# my_function = my_decorator(my_function)

print('---')

# Имейте в виду, что при использовании синтаксического сахара, на месте декорируемой функции появляется задекорированная функция.

def my_decorator(fn):
    def wrapper():
        fn()
    return wrapper # Здесь возвращается задекорированая функция, которая заменяет исходную.

# Выводим незадекорированую функцию.

@my_decorator
def my_function():
    pass
print(my_function)

print("---")

# Передача аргументов в декорируемую функцию

# def do_it_twice(func):
#     def wrapper():
#         func(arg)
#         func(arg)
#     return wrapper
#
# @do_it_twice
# def say_word(word):
#     print(word)
#
# say_word("Oo!!!")

# При выполнении кода выше, буддет выдаваться ошибка:
# TypeError: wrapper() takes 0 positional arguments but 1 was given

# Декоратор в котром встроенная функция умеет принимать аргументы.
def do_it_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@do_it_twice
def say_word(word):
    print(word)

say_word("Oo!!!")

print('---')

# Универсальный шаблон для декоратора:

def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return result
    return wrapper

# Задание 4.5.2

def my_decorator(fn):
    count = 0 # Данная переменная является nonlocal
    def wrapper(*args, **kwargs):
        nonlocal count
        fn(*args, **kwargs)
        count += 1
        print(f"Функция {fn} была вызвана {count} раз.")
    return wrapper

@my_decorator
def say_word(word):
    print(word)

say_word("Oo!!!")
say_word("Oo!!!")

print("---")

def no_my_decorator(fn):
    dicter = {}
    def wrapper(num):
        nonlocal dicter
        if num not in dicter:
            dicter[num] = fn(num)
            print(f"Добавление результата в кэш: {dicter[num]}")
        else:
            print(f"Возвращение результата из кэша: {dicter[num]}")
        print(f"Кэш {dicter}")
        return dicter[num]
    return wrapper

print('---')





# Вебинар. «Генераторы и итераторы».

a = [12, 33, 55]

for x in a:
    print(x)

print('---')

a = [12, 33, 55]

b = [i**2 for i in range(1, 10)] # это генератор списка.
print(b)

# Это можно представить таким образом.

b = []
for i in range(1, 10):
    b.append(i**2)

# Все вышеперечисленое это генератор.
print('---')

a = [12, 33, 55]

b = (i**2 for i in range(1, 10))# Это функция, которая может нам возвращать элементы по штучно.
print(b)

print('---')

a = [12, 33, 55]

b = (i**2 for i in range(1, 10))# Это функция, которая может нам возвращать элементы по штучно.
print(dir(b))

print('---')

# Попробуем пробежаться циклом по этому генератору

a = [12, 33, 55]

b = (i**2 for i in range(1, 10))
for x in b:
    print(x)

# Генератор это итерируемый объект.

print('---')

# Возьмем этот список и превратим его в генератор.

a = [12, 22, 33]

d = [i**2 for i in range(1, 10)] # В этом списке, где находится генератор, здесь она сразу получаем весь список и он сразу заносится в ОП.
b = (i**2 for i in range(1, 10)) # В случае с итератором он не созает все заранее, он заносит в ОП этлементы по запросу.

c = iter(a) # iter - это итератор
print(c)
# print(next(c))
# print(next(c))
# print(next(c))

print('---')

# Напишем функцию генератора. Генератор обратной последовательности.

def my_gen(n): # Функция будет принимать число и будет создавать генератор, от числа до 0.
    while n != 0: # Пока n не равно нулю.
        print('hello')
        yield n - 1 # yield тодает управлению коду, выполнять что-то дальше. Он возвращает значени, которое в нем записано и говорит работай дальше без меня до след. вызова.
        n -= 1

gen = my_gen(123)
print(next(gen))
print(next(gen))

# Премущество в том, что здесь мы не занимаем память. Скорость больше.

print('---')

# Запишем перд. прогу. другим способом. Генератор списков.

def my_gen_list(n):
    res = [] # Создаем список.
    while n != 0:
        res.append(n - 1) # Заполняем список.
        n -= 1
    return res # Возвращаем список.
print(my_gen_list(3))

print('---')





# Вебинар «Циклы и условия. Функциональное программирование»

# Условные конструкции if, elif, else.

a = 1000

if a > 10:
    print('a > 10')
elif a == 10:
    print('a = 10')


if a > 100:
    print('a > 100')
else:
    print('a < 10')

print('---')

# Циклы

# while - это бесконечный цикл.
# for - итерируемым циклом.

# while True:
    # print('hello')

# Останавливается 3-мя способами.
# 1)
a = True
while a:
    print(a)
    a = False
# 2)
a = True
while a:
    print(a)
    break

a = 0
while a < 10:
    a += 1
    print(a)

print('---')

# for

numberlist = [1, 2, 3, 4, 5]
a = 0
for x in numberlist: # х - это временная переменная, которая каждый раз меняет свое значение.
    a += x
print(a)

# Можем сделать и  со строкой.

numberlist = 'string'
a = 'jxbkvsdv'
for x in numberlist:
    a += x
print(a)

print('---')

# Как он выглядит внутри.

# for i in gen:
#     print(i)
#
#
# try:
#     while True:
#         print(gen.next())
# except StopIteration:
#     pass

print('---')

for i in range(0, 10, 2): # 1 число от какого числа. 2 до какого не включая. 3 с каким шагом.
    print(i)

print('---')

a = 'string'
b = ''
for i in a:
    b += i + '..'
    print(b)

print('---')

a = [1,2,3,4,5,6,7,8,9,10]
b = []
c = []

for i in a:
    if i <= 5:
        b.append(i)
        for x in b:
            print(b)
    else:
        c.append(i)
        for x in c:
            print(c)
print(b)
print(c)

print('---')

# Функции - это отдельные куски кода, в которую мы заносим повторяющиеся вещи.

def name():
    print('hello')

name()

print('---')

def name(atr): # atr - это атрибут.
    print(atr)

name('world')
name(10)

print('---')

def name(atr):
# Если брать пример с контрольной по математике, то, точто мы считаем в уме это тело функции( от def до return).
    return atr # return - это то что мы записываем в тетрадь и сдаем.

print(name('world'))

print('---')

# Будем высчитывать квадрат.

def name(atr):
    square = atr * atr
    print(square)

def sq(atr):
    square = atr * atr
    return square

print(name(5))
print(sq(5))

print('---')

def name(atr):
    square = atr * atr
    print(square)

def sq(atr):
    square = atr * atr
    return square

a = name(6)
b = sq(5)
print(b + 1)

print('---')

