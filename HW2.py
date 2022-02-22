# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
li = [1, 2.3, 'n']
print('список:', li)
for n, i in enumerate(li, 1):
    print(f'{n} элемент {type(i)}')

# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().
li = input('\nвведите список: ').split()  # всегда возвращает строку
print('список: ', li)
n = len(li)
if n % 2 == 0:
    n = n - 1
else:
    n = n - 2
m = n
while m >= 0:
    li[n - m], li[n - m + 1] = li[n - m + 1], li[n - m]
    m = m - 2
else:
    print('после обмена значениями', li)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
# через list
li = ['зима', 'весна', 'лето', 'осень']
w = [1, 2, 12]
sp = [3, 4, 5]
su = [6, 7, 8]
a = [9, 10, 11]
while True:
    m = int(input('введите месяц (число от 1 до 12): '))
    if 0 < m < 13:
        for el in range(0, 3):
            if m == w[el]:
                print('время года :', li[0])
            if m == sp[el]:
                print('время года :', li[1])
            if m == su[el]:
                print('время года :', li[2])
            if m == a[el]:
                print('время года :', li[3])
        break
    else:
        print('все-таки от 1 до 12')

# через dict
di = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
while True:
    m = int(input('введите месяц (число от 1 до 12): '))
    if 0 < m < 13:
        for el in di:
            if m in di[el]:
                print('время года :', el)
        break
    else:
        print('все-таки от 1 до 12')

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.
st = input('введите строку из нескольких слов, разделенных пробелами: ').split()
print('каждое слово с новой строки:')
for i, word in enumerate(st, 1):
    if len(word) <= 10:
        print(i, word)
    else:
        print(i, word[0:10])

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
# который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
new = int(input('введите новый элемент рейтинга: '))
if new > 0:
    for el in range(0, len(my_list)):
        if new == my_list[el]:
            my_list.reverse()
            el = len(my_list) - el
            my_list.insert(el, new)
            my_list.reverse()
            print('рейтинг с добавленным элементом: ', my_list)
            break
        if new > my_list[el]:
            my_list.insert(el, new)
            print('рейтинг с добавленным элементом: ', my_list)
            break

# 6. (Дополнительно) Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.

# список из 3 кортежей
# tov = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]

# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

tov1 = []
tov = []
x = 1
while True:
    num = int(input('введите номер товара'))
    tov1.insert(0, num)
    name = input('введите название товара')
    price = input('введите цену товара')
    amo = input('введите количество товара')
    dim = input('введите единицы измерения товара')
    data = {'название': name, 'цена': price, 'количество': amo, 'eд': dim}
    tov1.append(data)
    tov2 = tuple(tov1)
    tov.append(tov2)
    tov1.clear()
    q = input('хотите добавить товар? Формат ввода: да/нет ').lower()
    if q != 'да' or 'нет':
        q = input('хотите добавить товар? Формат ввода: да/нет ').lower()
    if q == 'нет':
        break
    x = x + 1
print('товары: ', tov)
names = []
prices = []
amounts = []
dimensions = []
for i in range(0, x):
    names.append(tov[i][1].get('название'))
    prices.append(tov[i][1].get('цена'))
    amounts.append(tov[i][1].get('количество'))
    dimensions.append(tov[i][1].get('eд'))
analytics = {'название': names, 'цена': prices, 'количество': amounts, 'единицы измерения': dimensions}
print('аналитика: ', analytics)
