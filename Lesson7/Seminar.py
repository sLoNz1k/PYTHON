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
# _________________________________________________________________________________________


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
# копией values.


# mapped_numbers = list(map(lambda x: x * 2 + 3, values))
# print(mapped_numbers)
# функция map - позволяет менять каждое значение в списках не создавая его копию, что улучшает производительность кода.

# size = int(input("Введите размер списка: "))
# myList = [0]*size

# for i in range(size):
#     myList[i] = random.randrange(10,20)
# print(myList)
# transformation = lambda x : x
# newList = list(map(transformation,myList))
# print(newList)

# for i in range(len(newList)) :
#     if newList[i] == max(newList):
#         newList[i] = min(newList)


# print(sorted(newList))

# _____________________________________________________________________________________________________________________________

# Задача № 2
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

result = 0

elips =list(filter((lambda x: x[0] != x[1]),orbits))
print(elips)
newOrbits = list(map(lambda x: x[0] * x[1], elips))

print(elips[newOrbits.index(max(newOrbits))])

# _____________________________________________________________________________________________________________________________


# Задaча  # 3
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику


# def same_by(func, objects):
#     for item in objects:
#         if not func(item):
#             return False
#     return True

# values = [0, 2, 6, 10]

# if same_by(lambda x: x % 2==0,values):
#     print('same')
# else :
#     print('differrent')