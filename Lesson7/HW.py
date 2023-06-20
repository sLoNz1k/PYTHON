# Задание№ 1
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

# Решение№ 1
import re

# vowels = {'а', 'и', 'о', 'у', 'ы', 'э', 'е', 'ё', 'ю', 'я'}
# vinni_enter = input('Винни, дай ритма: ').split()
# # пара-ра-рм рам-пaм-ппам па-р-п-даам - если вставить эту песенку, вместо ввода - не работает код. Если это же ввести в вводе - работает. МАГИЯ!


# def calcCount(enter):
#     count = 0
#     for i in enter:
#         if i in vowels:
#             count += 1
#     return count


# test = list(map(calcCount, vinni_enter))
# print(test)
# count = test[0]
# print(count)
# filteredTest = list(filter((lambda x: x == count), test))
# print(filteredTest)
# if len(test) != len(filteredTest):
#     print('Пам парам')
# else:
#     print('Парам-пам-пам')
# #______________________________________________________________

# #Решение №2
# def searching_vowels(vinni_enter,vowels) :
#     vowels_count = []
#     for phrase in vinni_enter:
#         count = 0
#         for i in phrase :
#             if i in vowels :
#                 count +=1
#         vowels_count.append(count)
#     return vowels_count
# test = searching_vowels(vinni_enter,vowels)
# check = True
# for i in range(1,len(test)):
#     check = check and test[i - 1] == test[i]
# if check:
#     print('Парам-пам-пам')
# else :
#     print('Пам парам')
#______________________________________________________________
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.


rows = 6
columns = 6
def function (operation, rows,columns):
    A = [[operation(i,j) for j in range(1, rows + 1)] for i in range(1, columns +1)]
    printing(A)


def printing(arr):
    # len(A) - возвращает количество строк в матрице А
    for i in range(len(arr)):
        # len(A[i]) - возвращает количество элементов в строке i
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

function(lambda x,y : x*y, rows,columns )
