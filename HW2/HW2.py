# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type()
# для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# result_list = [-2, 'text', 456, 45.3, None]
# print(result_list)
# el = 0
# x =len(result_list)
#
# while el < x:
#     print(f"Type of {el} element is: ", type(result_list[el]))
#     el += 1

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов
# последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

# numbers_list = list(map(int, input("Введите список чисел\ через пробел, когда закончите нажмите 'Enter'").split()))
# print(numbers_list)
#
# if  len(numbers_list) % 2 == 0:
#     for i in range(0, len(numbers_list), 2):
#         numbers_list[i], numbers_list[i+1] = numbers_list[i+1], numbers_list[i]
# else:
#     for i in range(0, len(numbers_list) - 1, 2):
#         numbers_list[i], numbers_list[i+1] = numbers_list[i+1], numbers_list[i]
# print(numbers_list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list
# и через dict.

# x = int(input('Input number from 1 to 12: '))
# terms_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
# print(f'\nYou selected this term of year - ', terms_list[x - 1])

# y = int(input('Input number from 1 to 12: '))
# terms_dict = {1 : 'january', 2 : 'february', 3 : 'march', 4 : 'april', 5 : 'may', 6 : 'june', 7 : 'july', 8 : 'august', 9 : 'september', 10 : 'october',
# 11 : 'november', 12 : 'december'}
# print(f'\nYou selected this term of year - ', terms_dict[y])

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное,
# выводить только первые 10 букв в слове.

# x = input("Input a phrase : ")
# for ind, el in enumerate(x.split( )):
#     print(ind, el[:10])

    # if len(x.split( )) <= 10:
    #     print(ind, el)
    # else:
    #     print(ind, el[:10])

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

# my_list = [7, 5, 3, 3, 2]
# print('List length', len(my_list))
# x = len(my_list)
# while x <= 15:
#     y = int(input('Input nat number: '))
#     i = 0
#     for i in range(x):
#         print(my_list[i])
#         if y >= my_list[i]:
#             my_list.insert(i, y)
#             break
#         if y <= my_list[(len(my_list) - 1)]:
#             my_list.append(y)
#             break
#         i += 1
#     print(my_list)

# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# x = int(input("Input number of products: "))
# i = 1
# goods = []
#
# while i <= x:
#     data = dict()
#     while True:
#         key = input('введите ключ: ')
#         if key == "0":
#             break
#         value = input('введите значение: ')
#         data[key] = value
#     g = [i,data]
#     gg = tuple(g)
#     goods.append(gg)
#     i += 1
#
# print(f"\n", goods)
