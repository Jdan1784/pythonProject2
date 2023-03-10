#Type - показывает тип переменной
a = 1
b = 73
c = -12
d = 2
e = ((b**d)*c)+a
print(e)
print(type(e))

print("")

x = 0.1
y = 21.5
z = y/x
print(type(x))
print(type(y))
print(z)
print(type(z))

print("")

print (0.1+0.1*5-0.3*4)
print ((3.14+0.3)/2+0.15)

print("")

#Обмен занчениями
a = -13
b = 7
a = a - b
b = a + b
a = b - a
print(a)
print(b)

print("")

#Переменные строки
s = "python"
print(s[2])
print(s[0:5])

print("")

#Проверям True или False
print(3 > 10)

print("")

print('r' in 'world')

print("")

print('PY' in "Python")

print("")

#Кортеж и доступ к отдельному индексу
date = (23, 'January', 2023)
print(date[0])
print(date[1])
print(date[2])

print("")

#Проверяем неизменяемоестьи еще приколный пример
s1 = "foo"
s2 = "bar"
s1 = s1+s2
print(s1)

print("")

#Деление целых числе
a = 5//2
print(a)
print(type(a))

print("")

#Остаток от деления
print(1 % 3)

print("")

a = 5
b = -2
q = a // b # в данном случае q = -3
r = a % b # а остаток r = -1
print(q)
print(r)

print("")

print ((31 % 2) + (-31 % 2))
print (13 % -3 * 3 - 3**2)

print("")

#Числа с плавающей точкой
a = 5.4321
print(a)
print(a**100)
print("""В таком случае это число можно прочитать как: 3.138886636534116 умножить на 10 в степени 73""")

print("")

print(1.2+1.4)

print("")

#Преобразвоние типов
print(float(1))
print(int(3.14))

print("")

print(1.00+0.01-3.01)
#Пробуем перевести в целое
print(int(1.00+0.01-3.01))
#round - позволяет округлять по правилам математики
print(round(1.00+0.01-3.01))

print("")

print(round(11*2.5/3, 2))

print("")

#Половина квадрата числа Пи
print(round((3.14159**2)/2))
