s = "Hello"
print(s.find('e'))# Возвращает индекс #1
print(s.find('er!'))# В случае подстроки возвращает индекс первого символа #4
a = 43
print(s.isalpha())

print("")

colors = 'red blue green'
print(colors.split())# Показывает, что находится в переменной.
path = '/home/user/documents/file.text'
print(path.split('/'))# Разделитель можно указать в качестве аргумента.

print("")

colors = 'red green blue'
colors_split =  colors.split()# Список цветов по отдельности
colors_joined = ' or '.join(colors_split)# Объединяем строки(НЕ ЗАБЫВАЕМ ПРО ПРЕБЕЛЫ В '_and_'). Join - метод обединения.
print(colors_joined)

print("")

numbers = '1 2 3 4 5 6 7'
number_split = numbers.split()
number_line = "\n".join(number_split)
print(number_line)

print("")

# Преобразование строк
# int_num = int(input("Введите целое число"))
# print(int_num)
# print(type(int_num))

print("")

age = 22
my_age = "I'm " + str( age )
print(my_age)

print("")

# Мы можем умонжать строку на число. Пример:
wow = 'wow'
print(wow*5)

print("")

# Форматирование строк
age = 25
my_age = "I'm %d years old" % (age)
print(my_age)

print("")

day = 11
month = 3
year = 2000
print("%d.%02d.%d" % (day,month,year))
print("%d-%02d-%d" % (year,month,day))
print("%d/%02d/%d" % (day,month,year))

print("")

seconds = 3
minutes = 2
hours = 1
print("%02d:%02d:%02d" % (hours,minutes,seconds))

print("")

# Изменяемые типы данных
s = [0, 'hello', (1,'a')]# Это список содержащий в себе целое число, строку и кортеж.

# Метод — это функция, которая применяется к определенному объекту, используя символ точку. Пример: объект.метод()
# Добавление объекта осуществляется с помощью метода append().
# Есть список, в нем первый 4 буквы латинского алфавита.
letters = ['a','b','c','d']
# C помощью метода append() мы добавляем еще один элемент в список.
letters.append('e')
print(letters)
print(letters[0])# Выводим первый элемент из списка.
print(len(letters))# Узнаем длинну списка.
print(letters[len(letters)-1])# Получаем последний объект из списка.
letters.append('f')# Добавляем одну букву.
letters.append('g')# И еще одну
print(letters[len(letters)-1])
print(len(letters))
print(letters[len(letters)-2])
print(letters[-1])
print(letters[-4])

# Можно удалять элементы со списка
print(letters)
letters.pop()# Если так пишет аргумент(в скобках ничго не указываем), то удаляется последни элемент.
print(letters)
letters.pop(0)# Удаляем элемент по индексу.
print(letters)
letters.pop(3)# Можно удалять любой элемент по его индексу.
print(letters)
print(letters[:])
letters.append('a')
print(letters)
letters.index('d')

print("")

# Задача
L = ["а","б","в",1,2,3,4]
print(L[1:4])# Выводит элементы начиная со второго по четверный включительно.
print(L[::3])# Выводит элементы через 2.
print(L[3::-1])# Выодит элементы начиная с 4-го, в развернутом виде.
print(L[7:3:-1])# Вывод элементов 4,3,2.

print("")

# Практический пример
# Возможности языка позволяют выполнить определенные действия для каждого элемента списка.
# Такую операцию можно проделать с помощью функцию map(): map(function, list)
# Имеем список с числами с плавающей точкой


# H = [3.3, 4.4, 5.5, 6.6]
# # Печатаем сам объект map
# print(map(input, H))#Каждый элемент округляем при помощи round - по правилам математики.
# print(list(map(round, H)))
# print("")
# string = input("Введите числа через пробел")
# list_of_string = string.split()#Cписок строковых представлений чисел
# list_of_numbers = list(map(int, list_of_string))#Список чисел
# print(sum(list_of_numbers[::3]))# sum() вычисляет сумму элементов списка

print("")

# Какаято хуйня
# L = list(map(float, input().split()))# все операции - деление строки по пробелам, преобразование к числам и приведение объекта map к типу список, можно делать в одной строке
# L[0], L[-1] = L[-1], L[0]# обмениваем первое и последнее число с помощью множественного присваивани
# L.append(sum(L))# Мы при помощи appened добовляем в лист L сумму всехчисел.
# print(L)

# СЛОВАРИ
person = {}#С помощью фигурных скобок создаем словари
# Словарь заполняется по принципу - ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov'}

# В него можно добавлять новый объекты по ключу
person['age'] = 27
person['email'] = 'ivan_petrov@gmail.com'
person['phone'] = '8(800)555-35-35'
print(person)
# Получаем список ключей
print(person.keys())
# Получаем список значений
print(person.values())
# Можно удалять значения при помощи ключей
person.pop('phone')
print(person)

print("")

d = {'day' : 22, 'month' : 6, 'year' : 2015}

print("||".join(d.keys()))

print("")
# Создаем словари и формируем из них список.
abit1 = {"ФИО" : 'Фадеев О.Е.', "Количество блаов" : 283,"Заявление" : True}
abit2 = {"ФИО" : 'Дружинин И.Я.', "Количество блаов" : 278,"Заявление" : False}
abit3 = {"ФИО" : 'Афанасьева Д.Н.', "Количество блаов" : 276,"Заявление" : True}

abits = [abit1, abit2, abit3]

print(abits)

# Этот список, по мере поступления документов, можно пополнять.

abit4 = {"ФИО" : 'Любимчикова А.я.', "Количество блаов" : 269,"Заявление" : True}

abits.append(abit4)

print(abits)

print("")

# Множества — это неупорядоченный набор уникальных элементов.
# Иными словами, во множествах не могут повторяться элементы,
# а хранятся они в памяти компьютера в произвольном порядке.
# (set)

# Создаем множество. 1) Способ: используя синтаксис {}

a = {'a', 'b', 'c', 'd'}

# Создаем множества. 2) Множесто можно создавать из списка с помощью приведения типов:

L = [1,1,2,3,2]

b = set(L)

print(b)

# Возвращаем множество в списоку

b_list = list(b)

print(b_list)

#Все вышеперечисленное можно сократить до одной строки.

c = list(set(L))

print(c)

print("")

# Работает, но не то ...
# string  = str("Меня зовут Николай, я родом и Никольска и у меня сестра Варвара.")
#
# m = set(string)
#
# print(m)

#Так как надо.

# text = input("Введите любой текст")
# uniqum = list(set(text))
# print("Колличнество уникальных символов: ", len(uniqum))

print("")

# Пример

abons = {"Иванов", "Петров", "Васильев", "Антонов"}# Список абонентов

debtors = {"Петров", "Антонов"}# Список должников

non_debtors = abons.difference(debtors)

print(non_debtors)

print("")

# a = input("Введите числа через пробел: ").split()# Не забываем про split, разделяет стрку на подстроку.
# b = input("Введите числа через пробел: ").split()# Не забываем про split, разделяет стрку на подстроку.
#
# numb_1, numb_2 = set(a), set(b)
#
# numbers = numb_1.symmetric_difference(numb_2)
#
# print("Уникальные символы :", list(numbers))

print("")

# Идентичность

L  = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

print("")

a = 5
b = 3+2

print(id(a))
print(id(b))

print("")

list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)
print(list_1)
print(list_2)
print(list_3)

print("")

# Результат указывает на идентичные списки.
# Проверяем равенство списков.
print(list_1 == list_2)
print(list_1 == list_3)

print("")

# Мы можем сравнивать при помощи ключевого слова is.
print(list_1 is list_2)
print(list_1 is list_3)

print("")

L =['Hello', 'world']
M = L

print(M is L)

M.append('!')
print(L)

print("")

# Неизменяемость кортежей.
shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр.,30", ["H&M", "Zara"])

shopping_center[-1].append("Uniqlo")# С конца добавили еще один магазин.

print(shopping_center)

print("")

#Задание 2.6.3

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo") 
list_id_after = id(shopping_center[-1])

print(list_id_before == list_id_after)

print("")

