# ___________________________________________________________________
# Задача №1
# Найдите сумму цифр трехзначного числа. 

# enter = int(input("Введите трёхзначное число: "))
# index = 0
# sum_ = 0
# if 100<= enter <= 999 :
#     while enter > index:
#         sum = enter % 10 + sum
#         enter = enter // 10
#     print(sum_)
# else: 
#     print("Неверное число!")
# ___________________________________________________________________

# Задача №2
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# S = int(input("Сколько всего сделано журавликов?: "))
# print("У Пети получилось:" , S // 4,"журавликов;", "\nУ Пети получилось:", S // 4,"журавликов;" "\nУ Кати получилось:", S // 2,"журавликов.")
# ___________________________________________________________________

# Задача №3
# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# ticketNum = int(input("Введите шестизначный номер билета: "))
# a = ticketNum % 1000
# b = ticketNum // 1000
# sum1 = 0
# sum2 = 0
# if 100000 <= ticketNum <= 999999:
#     while b > 0:
#         sum1 = a % 10 + sum1
#         sum2 = b % 10 + sum2
#         a = a // 10
#         b = b // 10
#     if sum1 == sum2:
#         print("Ура, счастливый билет!")
#     else:
#         print("В следующий раз :(")
# else:
#     print("Не шестизначное число!")
# ___________________________________________________________________

# Задача №4
# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).


# n = int(input("Введите количество долек шоколадки в длинну:"))
# m = int(input("Введите количество долек шоколадки в ширину:"))
# k = int(input("Введите количество долек, которые вы хотите отламать: "))

# if k % n == 0 or k % m == 0:
#     print("Можешь кушать, плитка отломана по правилам!")
# else:
#     print("Не правильная шоколадка, брось!")



