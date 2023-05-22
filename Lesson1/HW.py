# Задача №1
# Найдите сумму цифр трехзначного числа. 

enter = int(input("Введите трёхзначное число: "))
index = 0
sum = 0
if 100<= enter <= 999 :
    while enter > index:
        sum = enter % 10 + sum
        enter = enter // 10
    print(sum)
else: 
    print("Неверное число!")

