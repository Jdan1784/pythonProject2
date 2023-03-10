# Цикл while

#Задача.

# Условие задачи: Написать цикл, который будет складывать натуральные числа,
# пока их сумма не превысит 500.

S = 0 # Это наша переменная-счетчик, в которой мы будем считать сумму чисел.
n = 1 # Текущее натуральное число, с которого начинаем складывать натуральные числа.
# Заводим цикл while, который будет работать пока сумма не превысит 500.
while S < 500: # Делай пока ...
    S += n # Увеличиваем сумму по принципу S = S + n
    n += 1 # Так как сумма не достигла нужного значения, то увеличиваем переменную счетчик
    # по принципу n = n + 1
    print("Еще считаю ...")
print("Сумма равна:", S)
print("Количество чисел: ", n-1)

print("")

i = 0
while (i * i) < 1000:
    i += 1
    print("Еще считаю ...")
print("Максимальное число =", i)

print("")

# break - принудительная остановка цикла.

n = 1
while True:
    print("Hello World")
    n += 1
    if n > 10:
        break

print("")

# Задание 3.6.7

n = 0 # Степень нашей двойки, которую мы будем увеличивать.
cnt = 0 # Переменная-счетчик будет считать количество итераций до момента соблюдения условия.
while 2**n < 10000:
    n += 1
    cnt += 1
print(cnt)

print("")

k = 1000
m = 0
t = 8
while k < 3000:
    o = k * t / 100
    k = k + o
    m += 1
print(k)
print(m)
print(o)

print("")

employee = 5
i = 1
while i < employee:
    if i > 1:
        print('There are', i, 'people in the department')
    if i == 1:
        print('There are', i, 'people in the department')
    i += 1

print("")

# Цикл - for

# Функция, которая позволяет создать последовательность чисел от 1 до N.
# range()
# Она может работать 3-мя способами:
# range(END) - В данном случае она принимает одну переменную END и возвращает последовательность элементов от 0 до END-1 шагом в 1.
# range(START, END) - В данном случае вы получите последовательность от start до end-1 также с шагом в 1.
# range(START, END, STEP) - В данном случае вы можете задать произвольный шаг и получить, например, все нечётные натуральные числа меньше 10.

# Пример № 1 Нас интересуют числа от 1 до N включительно, значит, код будет выглядеть следующим образом:

S = 0 # Заводим переменную счетчик, в которую мы будем считать сумму.
N = 5

# Заводим цикл for в котором мы будем проходить по всем числам от одного до N.

for i in range(1, N + 1): # Равносильно выражению for i in [1, 2, 3, ... , N -1, N]
   print("Значение суммы на предыдущем шаге: ", S)
   print("Текущее число: ", i)
   S = S + i # Суммируем текущее число i и перезаписываем значение суммы.
   print("Значение суммы после сложения: ", S)
   print("---")
print("Конец цикла")
print()
print("Ответ: сумма равна = ", S)

print("")

my_list = [5, 9, 19]
for element in my_list:
    print('Element', element)

print("")

P = 1
N = 5

for i in range(1, N + 1): # Равносильно выражению for i in [1, 2, 3, ... , N -1, N]
   print("Значение на предыдущем шаге: ", P)
   print("Текущее число: ", i)
   P = P * i # Суммируем текущее число i и перезаписываем значение суммы.
   print("Значение после произведения: ", P)
   print("---")
print("Конец цикла")
print()
print("Ответ: произведение равно = ", P)

print("")

N = 3

for i in range(1, N + 1):
    print('*' * i)

print("")

# Работа со вложенными циклами.

# Рассмотрим таблицу вида.

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
# Такие таблицы называют двумерными списками.
# Двумерная матрица - это список списков.
for row in matrix: # Для ряда в матрице.
    for element in row: # Для елемента в матрице.
        print(element, end = "") # На вывод распечатывваются поледовательно элементы матрицы.

print("")

# Если мы хотим, чтобы вывод был в более «табличном» виде,
# то в конце каждой строки нужно будет вставить перенос строки.

matrix = [
    [1, 2]
   ,[3, 4]
   ,[5, 6]
]
for row in matrix:
    for element in row:
        print(element, end = "")
    print() # Этот print относится к циклу for row in matrix.

print("")

# Также перебирать элементы матрицы можно по индексам строки и столбца.
# Обычно индекс, который отвечает за строки, обозначают как i, а за столбцы — j.

ROWS = 3
COLS = 2

matrix = [
    [1, 2]
   ,[3, 4]
   ,[5, 6]
]

for i in range(ROWS):
    for j in range(COLS):
        print(matrix[i][j], end = "")
    print()

print("")
# Разберём большой пример работы с таблицами.

# Условие задачи. Дана двумерная матрица 3x3 (двумерный массив).
# Необходимо определить максимум и минимум каждой строки, а также их индексы.

random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]
# В каждой строке помечен минимальный элемент. Нам нужно пройтись по всем
# строкам сверху вниз и по элементам в строке справа налево, определить среди них
# минимум в каждой строке и записать результат в отдельный список.

# Обращаться к элементам матрицы мы можем так:
# random_matrix[i][j]

# Создадим списки, где мы будем хранить ответ на наш вопрос:

# min_value_rows = []
# min_index_rows = []

# Для начала напишем цикл, в котором пройдём по всем строкам матрицы:

# for row in random_matrix:

# Создадим две переменные:

# min_index = 0 # Индекс кандидата.
# min_value = row[min_index] # Сам кандидат.

# Перебираем индексы.

# for index_col in range(len(row)):

# Теперь сравниваем элемент с индексом index_col и нашего кандидата
# в соответствии с алгоритмом:

# if row[index_col] < min_value:

# Если он оказался меньше, то теперь кандидат — это сам текущий элемент:

# min_value = row[index_col]
# min_index = index_col

# Добавим этого кандидата и его индекс в наши списки с ответами:

# min_value_rows.append(min_value)
# min_index_rows.append(min_index)

# Теперь, после прохода в цикле по строкам матрицы, выведем наши ответы в консоль:

# print(min_value_rows)
# print(min_index_rows)

# Аналогично сделаем для максимума.

# Полный код.

random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]
min_value_rows = []
min_index_rows = []
max_value_rows = []
max_index_rows = []
for row in random_matrix:
    min_index = 0
    min_value = row[min_index]
    max_index = 0
    max_value = row[max_index]
    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)
print("Minimal elements:", min_value_rows) # минимальные элементы
print("Their indices:", min_index_rows) # их индексы
print("Maximal elements:", max_value_rows) # максимальные элементы
print("Their indices:", max_index_rows) # их индексы

print("")

# ЗАДАНИЕ 3.8.1

test_matrix = [[1, 2, 3],
               [7, -1, 2],
               [123, 2, -1]]
max_value_rows = [0]

for row in test_matrix:
    max_index = 0
    max_value = row[max_index]
    for element in row:
        if element > max_value:
            max_value = element
print(max_value)

print("")

test_matrix = [[1, 2, 3],
               [7, -1, 2],
               [123, 2, -1]]
lines = len(test_matrix) # Создаем переменную и при помощи len определяем количество элементов в матрице.
print(lines)
result = True # Создаем переменную и присваеваем значение True.
for row in test_matrix:
    if (len(row)) != lines:
        result = False
print(result)












