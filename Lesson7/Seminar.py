# Задача №1
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился


import random
# transformation = lambda x: x **4
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# print(values)
# print(transormed_values)


# mapped_numbers = list(map(lambda x: x * 2 + 3, values))
# print(mapped_numbers)
# функция map - позволяет менять каждое значение в списках не создавая его копию, что улучшает производительность кода. 

size = int(input("Введите размер списка: "))
myList = [0]*size

for i in range(size):
    myList[i] = random.randint(20, 25)
print(myList)
transformation = lambda x : x - 15
newList = list(map(transformation,myList))
print(newList)

for i in range(len(newList)) :
    if newList[i] == max(newList):
        newList[i] = min(newList)
        print(newList[i])

print(sorted(newList))
