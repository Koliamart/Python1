# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

lst = [2, 5, True, '3', 8.9]
for i in lst:
    print(type(i))

# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

lst = input('Введите любые символы через пробел: ').split()
a = 0
b = 1
while len(lst) > b:
    lst[a], lst[b] = lst[b], lst[a]
    a += 2
    b += 2
print(*lst)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

mon = int(input('Введите номер месяца: '))
lst = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
print(f'Название месяца: {lst[mon - 1]}')

mon = int(input('Введите номер месяца: '))
dct = {1: 'Зима',
       2: 'Зима',
       3: 'Весна',
       4: 'Весна',
       5: 'Весна',
       6: 'Лето',
       7: 'Лето',
       8: 'Лето',
       9: 'Осень',
       10: 'Осень',
       11: 'Осень',
       12: 'Зима'}
print(f'Название месяца: {dct[mon]}')

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

dct = input('Введите слова через пробел: ').split()
for n, d in enumerate(dct, start=1):
    if len(d) > 10:
        d = d[0:10]
    print(f'{n}. {d}')

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
# который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
r = int(input('Введите любую цифру: '))
my_list.append(r)
my_list.sort()
my_list.reverse()
print(my_list)

