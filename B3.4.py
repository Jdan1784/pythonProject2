# Функции

# Объявляем функцию для подсчета кол-ва символов в тексте.

def char_frequency():
    text = """
    У лукоморья дуб зелёный;
   Златая цепь на дубе том:
   И днём и ночью кот учёный
   Всё ходит по цепи кругом;
   Идёт направо -- песнь заводит,
   Налево -- сказку говорит.
   Там чудеса: там леший бродит,
   Русалка на ветвях сидит;
   Там на неведомых дорожках
   Следы невиданных зверей;
   Избушка там на курьих ножках
   Стоит без окон, без дверей;
   Там лес и дол видений полны;
   Там о заре прихлынут волны
   На брег песчаный и пустой,
   И тридцать витязей прекрасных
   Чредой из вод выходят ясных,
   И с ними дядька их морской;
   Там королевич мимоходом
   Пленяет грозного царя;
   Там в облаках перед народом
   Через леса, через моря
   Колдун несёт богатыря;
   В темнице там царевна тужит,
   А бурый волк ей верно служит;
   Там ступа с Бабою Ягой
   Идёт, бредёт сама собой,
   Там царь Кащей над златом чахнет;
   Там русский дух... там Русью пахнет!
   И там я был, и мёд я пил;
   У моря видел дуб зелёный;
   Под ним сидел, и кот учёный
   Свои мне сказки говорил.
    """

    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace("\n", "")

    count = {} # Переменная для подсчета символов и их количества.
    for char in text:
        if char in count: # Если символ уже встречался, то увеличиваем его количество на 1.
            count[char] += 1
        else:
            count[char] = 1

    for char, cnt in count.items():
        print(f"Символ {char} встречается {cnt} раз")

char_frequency()

print("---")

def print_2_add_2():
    result = 2 + 2
    print(result)

print_2_add_2()

print("---")

def hello_world():
    print("Hello World")

hello_world()

print("---")

# Улучшаем функицю char_frequency

# объявили функцию для подсчета количества символов в неком абстрактном тексте
def char_frequency(text):
   text = text.lower()
   text = text.replace(" ", "")
   text = text.replace("\n", "")

   count = {}  # для подсчета символов и их количества
   for char in text:
       if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
           count[char] += 1
       else:
           count[char] = 1

   for char, cnt in count.items():
       print(f"Символ {char} встречается {cnt} раз")

char_frequency("Эта книга адресована всем, кто изучает русский язык. Но состоит она не из правил, упражнений и учебных текстов. Для этого созданы другие замечательные учебники.У этой книги совсем иная задача. Она поможет вам научиться не только разговаривать, но и размышлять по-русски. Книга, которую вы держите в руках, составлена из афоризмов и размышлений великих мыслителей, писателей, поэтов, философов и общественных деятелей различных эпох. Их мысли - о тех вопросах, которые не перестают волновать человечество.Вы можете соглашаться или не соглашаться с тем, что прочитаете в этой книге. Возможно, вам покажется, что какие-то мысли уже устарели. Но вы должны обязательно подумать и обосновать, почему вы так считаете.А еще вы узнаете и почувствуете, как прекрасно звучат слова любви, сострадания, мудрости и доброты на русском языке.")

print("---")

def pow_func(base):
    print(base ** 2)

pow_func(3)
pow_func(5)

print("---")

# Пусть наша функция теперь возводить число в любую степень,
# но по умолчанию возводит в степень 2. Тогда её объявление будет выглядеть следующим образом

def pow_func(base, n = 2):
    print(base ** n)

pow_func(5)
pow_func(5, 3)

print("---")

def divisor(a, n):
    if a % n == 0:
        print(f"Число {n} является делителем числа {a}.")
    else:
        print(f"Число {n} НЕ является делителем числа {a}.")

divisor(9, 3)

print("---")

def star(n):
    for i in range(n, 0,-1):
        print('*' * i)

    print("")

star(3)

print("---")

# Функция всегда что-то возвращает при помощи ключевого слова return.

def pow_func(base, n = 2):
    print(base ** n)

print(pow_func(3))

# В явном виде прога будет выглядеть так.

def pow_func(base, n = 2):
    print(base ** n)
    return None

print(pow_func(3))

print("---")

# Делаем так, чтобы наша функция возвращала результат вычисления.

def pow_func(base, n = 2):
    inside_result = base ** n
    return inside_result

print(pow_func(3))

print("---")
# Мы даже можем присвоить этот результат некоторой переменной и использовать это значение вне тела функции.

outside_result = pow_func(3)
print(outside_result)

print("---")

def number_of_divisors(a):
    count = 0
    for n in range(1, a + 1):
        if a % n == 0:
            count += 1

    return count

print(number_of_divisors(5))

print("---")

def palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")

    if string == string[::-1]:
        return True
    else:
        return False

print(palindrome("Кит на море не романтик"))

print("---")

def my_func(a, b):
    result = a + b

    return result

c = my_func(5, 10)
print(c)

print("---")

# Области видимости.

# Локальные области видимости. Что происходит внутри остается внутри.

def local():
    x = 5 # Локальная переменная.
    print(x)

x = 10
local()
print(x)

print("---")

# Глобальная область видимости.

def local():
    print(x) # Так как x нет в локальной области видимости, мы берем её из глобальной области.

x = 10
local()
print(x)

print("---")

x = 3
def function():
    print(x)
    return x

print(function())

print("---")

# x = 3
#
#
# def func():
#     print(x)
#     x = 5
#     x += 5
#     return x
#
#
# print(func())

print("---")

# Исправляем ошибку из кода выше.

x = 3


def func():
    global x # Объявляем, что переменная является глобальной.
    print(x)
    x = 5
    x += 5
    return x

func()
print(x)

print("---")

# Нелокальная область видимости.

# Предположим, мы хотим сделать функцию, которая будет возвращать нам функции.

def get_my_func(): # Пишем функцию, которая бужет вызывать функцию ниже.
    def hello_world(): # Которая выводит ...
        print("Hello")
    return hello_world

hello_world_func = get_my_func() # Присваиваем переменной значение функции.

print(type(hello_world_func))
hello_world_func()

print("---")

# Рассмотрим пример, в котором будут возвращаться различные функции.
# Функция нам будет создавать функции, которые будут умножать на какое-то фиксированное число.

def get_mul_func(m): # Получить многофункциональную функцию.
    nonlocal_m = m
    def local_mul(n):
        return n * nonlocal_m

    return local_mul

two_mul = get_mul_func(7) # Возвращаем функцию, которая будет умножать числа на 2.

print(two_mul(7))

print("---")

PI = 3.14 # Глобальная переменнная

def area_circile(r):
    global PI # Так делать лучше не надо.
    print("Число выведеное из локальной области видимости до изменения ", PI)
    PI = 3.1415 # Локальная переменная(После объявления global, PI становится глобально)
    print("Число выведеное из локальной области видимости после ", PI)
    return PI * (r ** 2)

print("Число выведеное из глобальной области видимости до вызова ", PI)
print(area_circile(10))
print("Число выведеное из глобальной области видимости после вызова", PI)

print("---")

# Запакованые переменные или что такое *args и **kwargs
# Есть позиционные (positional) и именованные (keyword) аругменты.


# Пример позиционных  аргументов.
def func(a, b, c):
    print('a =', a)
    print('b =', b)
    print('c =', c)

func(1, 2, 3)

func(3, 2, 1)

print("---")

# Пример именованных аргументов.

func(a = 1, b = 2, c = 3)

func(c = 3, b = 2, a = 1)

print("---")

# Важно! Все именованные аргументы должны идти строго после позиционных, как при объявлении функций, так и при их вызове.

# Правильно
# func(a, b, c = 3)

# Не правильно.
# func(a = 1, b, c)

# * - этот оператор позволяет "распаковать"( получить все значения из какой-либо
# последовательности, а не саму последовательноть).

a = [1, 2, 3]
b = [a, 4, 5, 6]
print(b)

a = [1, 2, 3]
b = [*a, 4, 5, 6]
print(b)

print(a)
print(*a)

print("---")

# Чтобы функция принимал не ограниченое кол-во позиц. арг. есть *args
# Чтобы функция принимал не ограниченое кол-во имен. арг. есть **kwargs
# args - это кортеж.
# kwargs - это словарь.

def my_func(*args, **kwargs):
    print(type(args))
    print(type(kwargs))

my_func()

# Задача. Сделаем сумматор, который будет + любое кол-во переданных ей арг.

def adder(*nums):
    sum_ = 0
    for n in nums:
        sum_ += n

    return sum_

print(adder())
print(adder(1))
print(adder(1, 2))
print(adder(1, 2, 3))

print("---")

def product(*nums):
    result = 0
    for i in nums:
        result = i * i

    return result

print(product())
print(product(1))
print(product(1, 2))
print(product(2, 2))
print(product(3, 3))
print(product(6, 6))

print("---")

# Изменяемые типы данных как аргументы по умолчанию.

# Создадим неправильную функцию с указанием аргумента по умолчанию в виде списка. И вызовем эту функцию два раза.

def incorrect_func(name_arg = []): # name_arg является локальной переменной.
    print("Аргумент до изменения", name_arg)
    name_arg.append(1)
    print("Аргумент после изменения", name_arg)

incorrect_func()
print('----')
incorrect_func()

print('---')

def correct_func(name_arg = None): # Не желательно использовать в качестве аргумента изменяемые типы данных.
    if name_arg is None: # Если пользователь не изменил значение name_arg с None, значит она страновится списком.
        name_arg = []
    print("Аргумент до изменения", name_arg)
    name_arg.append(1)
    print("Аргумент после изменения", name_arg)

correct_func()
print('-----')
correct_func()
print('-----')
correct_func([123])
print('-----')
correct_func(name_arg = [123])

print('---')

# Рекурсивные функции — это функция, вызывающая сама себя и обрабатывающая полученный результат до тех пор, пока не достигнем терминального условия (условия остановки).
# Количество раз, сколько функция вызвала сама себя, называется глубиной рекурсии.
# Рекурсия состоит из рекурсии вызова и терминального условия.
# Факториал числа — это произведение натуральных чисел от 1 до самого числа (включая данное число).
# Обозначается "!"

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(4))

print('---')

def rec_fibb(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return rec_fibb(n - 1) + rec_fibb(n - 2)

print(rec_fibb(10))

print('---')

def sum_numb(n):
    if n == 1:
        return 1
    return n + sum_numb(n - 1)


print(sum_numb(5))

print('---')

def reverse_str(string):
    if len(string) == 0:
        return ''
    else:
        return string[-1] + reverse_str(string[:-1])

print(reverse_str('test'))

print("---")

def sum_cifr(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_cifr(n // 10)

print(sum_cifr(15555))

print("---")








