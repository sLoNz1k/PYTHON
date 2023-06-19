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
# rows = int(input('rows: '))
# columns = int(input('columns: '))
# arr = []* rows




# def multiple(rows,columns,arr):
#     for i  in range(1, rows): 
#         for j in range(1,columns):
#             arr[j][i] = i * j
#             print(arr[i,j])

# multiple(rows, columns, arr)

# def multiple(arr):
#     for row in range(len(arr)):
#         for column in range(len(arr)):
#             print(row * column, end= '\t')
#         print()

# multiple(arr)


# multiple = int(input())
# for row in range(1, multiple + 1):
#     for column in range(1, multiple + 1):
#         print(row * column, end='\t')
#     print()


n = 5
m = 5 
A = [[1 for j in range(n)] for i in range(m)]
multiple = list(map(lambda x : x * x) ,A)

def printing(arr):
    # len(A) - возвращает количество строк в матрице А
    for i in range(len(arr)):
        # len(A[i]) - возвращает количество элементов в строке i
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

printing(multiple)