# B4.4. Итераторы и генераторы, оператор yield
# Реализуем бесконечную последовательность чисел фибоначи.

def fib():
    a, b = 0, 1
    yield a # F0
    yield b # F1

    while True:
        a, b = b, a + b
        yield b

# Чтобы получить значения из функции-генератора, можно воспользоваться циклом for:

for num in fib():
    if num > 10000000000000000000000000000000000000000000000:
        break
    print(num)

print('---')

# Задание 4.4.1
# Создать бесконечную последовательность натуральных чисел.

def endless (a = 1, n = 1):
    start = a

    while True:
        yield start
        start += n

for num in endless(5, 18):
    if num > 1000:
        break
    print(num)

print('---')

# Задание 4.4.2
# Создаем бесконечный повтор одного и того же списка.

def repeat_list(list_):
    b = list_.copy()
    while True:
        value = b.pop(0)
        b.append(value)
        yield value

# for lis in repeat_list([1,2,3]):
#     print(lis)

print("---")

# Итераторы

# Если мы знаем являются ли объекты итерируемыми,
# значит мы можем использовать функцию iter(object). В качестве аргумента передавать оъект для проверки.
# Фукция next() позволяет получить следующий элемент от итератора.

# Пример
str_ = "my tst"
str_iter = iter(str_)

print(type(str_)) # Вызываем строку
print(type(str_iter)) # Вызываем итератор строки

# Дальше, используя next() будем получать элементы от итератора строки.

print(next(str_iter)) # m
print(next(str_iter)) # y
print(next(str_iter)) # (пробел)
print(next(str_iter)) # t
print(next(str_iter)) # s
print(next(str_iter)) # t

# Проверить, что будет происходить после окончания последовательности.

# print(next(str_iter)) # Ошибка.

# Пробуем реализовать бесконечный счетчик.

def count (start, step): # В качестве аргументов будет принимать "start", т.е. тот элемент с которого будет начинаться посл. и шаг, с которым будем получать элементы.
    counter = start # Локальная переменная, котрой присваеваем значение "start".
    while True: # Запускаем бесконеный цикл.
        yield counter # И этот цикл каждый раз юудет возвращать новый элемент.
        counter += step # Дальше будет добавлять шаг и переписывааться переменная.
my_gen_func = count(100, 10)
for i in range(10): # При помощи range  получим 10 чисел из нашей последовательности.
    print(next(my_gen_func)) # Получаем 10 элементов, начиная со 100 с шагом 10.

print('---')

# Как и все генераторы, функция-генератор останавливается с вызовом StopIteration.
# Это происходит при следующих условиях:
# 1. Интерпретатор достиг конца выполнения функции и не встретил никаких инструкций.
# 2. В функции был выполнен return.
# 3. "Вручную" вызвано неперехваченное исключение StopIteration.

# Примеры всех 3-х.

# № 1
def first_gen(input_): # Объявляем функцию генератор.
    yield input_ # Которая всего 1 раз возврат. введенное знач.
    input_ += 1 # Также счетчик увеличиваем на еденицу.
    print(input_) # И попытаемся после этого ещё раз распечатать наше знач.

my_first_gen = first_gen(5) # Инициализируем наш генератор.

print(next(my_first_gen))

print('---')

# next(my_first_gen) # Будет выдавать ошибку.

print('---')

# № 2

def second_gen(input_):
    yield input_
    input_ += 1

    yield input_
    input_ += 1

    return input_

my_second_gen = second_gen(10) # Мы 2 раза сможем обратится к фукции next(), а при обращении 3-й, там

print(next(my_second_gen))
print(next(my_second_gen))
# print(next(my_second_gen)) #

print('---')

# def last_gen():
#     for i in range(10):
#         yield i
#         if i == 5:
#             raise StopIteration

# my_last_gen = last_gen()

# for i in range(10):
#     print(next(my_last_gen))

# my_last_gen = last_gen()
# for i in my_last_gen:
#     print(i)

print("---")

def my_animal_generator():
    yield 'корова'
    print('---')
    for animal in ['кот', 'собака', 'медведь']:
        yield animal
    print('---')
    yield 'кит'

a = my_animal_generator()
print(next(a))
print(next(a))
for i in a:
    print(i)














