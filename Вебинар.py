a = 1# int
b = 1.01# float
my_var0 = 'hi '# Так записываются строки, без разницы какие ковычки.
my_var1 = 'world'

print(my_var0+my_var1)# Скаладываем строки.

my_ass = 'bitch '

print(my_ass*10)# Можем умножать строки.

nocs = '7'
print(int(nocs)+10**100)

# n = int(nocs)
# print(type(n))
# print(n+10**100)

# а Можно все замутить в одну строку.

# СПИСКИ
# В массиваах могут храниться только одинаковые типы данных, в то время как спискам похуй.

fuck = [1, 'hellow', 'world', 4, 45]
print(len(fuck))

# dict - словарь

fuck = {'hi': 'world'}
print(fuck['hi'])

# Можем заставить типы взаимодействовать друг с другом.
mem = [{'Users_vk':[1,2,3,4]}, {'Users_mail': []}]

print(mem[0]['Users_vk'])

# bool

mask = True
mask_2 = False

print(mask)

# None - ничего.

kek = {1,2,3,2}

print(kek)

# Преобразование.

rofl = 'hello'

print(rofl.upper())# Пишет все большими буквами.
print(rofl.lower())# пишет все с маленькой.
print(rofl.isalpha())# Проверяет состит ли строка только из букв.
rofl = '12345'
print(rofl.isdigit())# состоит ли строка только из цифр.
rofl = 'Hello world'
print(rofl.split('o'))# Разделяет строку и привращает в список по аргументу "()".

# Память.

import sys

lol = 'sfwe'

print(sys.getsizeof(lol))# При помощи этого метода можем понять сколько весит переменная.

import sys

a= '1'
b = 1
c = 1.0

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))

a = 2222222222
b = 2222222222
print(a is b)# Проверяет являются ли эти объекты ссылающиеся на одну ячейку памяти.

# Изменяемость

b = [2, 3, 2]
a = [b]
b.append(2)
print(id(a))




