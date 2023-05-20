#Указание типа данных
# print("Введите первую строку: ")
# a = int(input())
# b = int(input("Введите вторую строку: "))
# sum = int(a) + int(b)
# print(a , "+" , b, "=" , sum)

#Типизация данных
# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# округление float
# a = 5.1231
# b = 6.12321
# print(round(a*b, 3))

#Прибавление
# iter = 2
# iter += 3 #прибавление к переменной ( как в шарпе iter++)
# iter **= 5 # Возведение в степень

#Логические операции
# a = 1>4
# print(a)

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

#Отступы и управляющие конструкции "if, if-else"

# username = input("Введите имя: ")
# if username == 'Маша':
#     print("Здарова, Маня")
# elif username == "браток":
#     print('Здарова, браток')
# elif username == "Анюта":
#     print("Приветик, Анютик")
# else:
#     print("Здарова, ", username  , ", ты кто такой?")

#Цикл While
# i = 0
# while i < 5:
#         i = i + 1
# else:
#     print("Пожалуй")
#     print("Хватит")
# print(i)

#Взамен break. Метод "Флажка"
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n% i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1

#Цикл for, функция range()
# r = range(0, -10, - 1)
# for i in r:
#     print(i)

# a = 'qwerty'
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += '*'
#         line += '+'
#     print(line)

# text = 'СъеШь ещё ЭтиХ мЯГкИх французских булок'
# print(len(text))
# print("ещё" in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('ещё', 'ЕЩЁ'))

# text = 'СъеШь ещё ЭтиХ мЯГкИх французских булок'
# print(text[0])
# print(text[1])
# print(text[len(text)-1])
# print(text[-1])
# print(text[4:21])
# text = text[2:9] + text[-5] + text[:2]
# print(text)
