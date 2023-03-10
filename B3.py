# Операторы сравнения.
# Оператор — это обозначение некой операции.
a = 10
b = 1

is_greater = a > b# Присваиваем переменной не значение а выражеение.

print(is_greater)

print("")

var = 3 < 5# Сразу сравниваем 2 числа.

print(var)

print("")

# Задание 3.1.1
var = 5 > 10

print(var)

print("")

# Проверяем одинкаовы ли значения.
a = 1
b = 2

print(a == b)# Сами значения остаются прежними.
print(a)
print(b)

a = b# Присваиваем.
print(a)
print(b)

print("")

# Задание 3.1.2

print(True != False)# Результатом действия != является истина в том случае, если сравниваемые значения неравны.
print(True == False)# Результатом действия == является истина в том случае, если сравниваемые значения равны.

print("")

# Логические операторы.
# Логическое «НЕ»

print(not True)
print(not False)

print(not not not not True)

print("")

# Сравнение строк.

k = '123'
m = 'abc'
print(k > m)

print("")

# Логическое «И»
# Результат применения оператора and будет истинным (True),
# если и первое, и второе высказывание являются истинными.
# Во всех остальных случаях результат — ложь (False).

# Можно проверить, находится ли число 1 в промежутке (0,4).
kaxa1 = 0 < 1
kaxa2 = 1 < 4

print(kaxa1 and kaxa2)

print("")

# Например, содержат ли две строки один и тот же символ.
kaxa3 = 't' in "python"
kaxa4 = 't' in "bango"

print(kaxa3 and kaxa4)

print("")

# Логическое «ИЛИ»
# Если хотя бы одно высказывание является истинным, то и результат будет истинным.
# К слову, логические выражения можно сразу объединять в одно целое.
print(('t' in "python") or ('t' in "django"))

print("")

print(not True or (True and not True))
print(not False and True or False and not True)

print("")

string_1 = 'abc'
string_2 = 'ABC'
print(string_1 == string_2)

print("")

x = 10
y = 100
z = (x % 2 == 0) and (y >=100)
print(z)

print("")

# password = "dgh36gh7"
# answer = input()
#
# print(password == answer)

print("")

# person_age = int(input())
# # print((person_age >= 35) or (person_age <= 18))
# x1 = person_age >= 18
# x2 = person_age <= 35
# print(x1 and x2)
# print(type(person_age))

print("")

print(str(123456789))

print(list(str(123456789)))

print(map(int, list(str(123456789))))

print(5 in list(map(int, list(str(123456789)))))

# in - проверяет налииче элемента.
print('5' in str(123456789))


