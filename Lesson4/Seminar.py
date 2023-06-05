import os
os.system('clear')

# Задача №1
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


text = 'a a a b c a a d c d d'
myList = text.split()

dictionary = {}
count = str()

for letter in myList:
    if letter in dictionary.keys() :
        dictionary[letter] += 1
        count += f'{letter}_{dictionary[letter]} '
        print(count)
    else :
        dictionary[letter] = 0
        count += f'{letter}'
        print(count)
print(text)
print(count)