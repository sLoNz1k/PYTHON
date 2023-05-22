# Задание №1
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами

# n = int(input("Введите расстояние, которое проходит авто за день: "))
# m = int(input("Введите общее количество километров, которые нужно проехать: "))

# res = (m + n - 1) // n
# print(res)

# Задание №2
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

# a = int(input("Введите количество учеников в первом классе:"))
# b = int(input("Введите количество учеников во втором классе:"))
# c = int(input("Введите количество учеников в третьем классе:"))
# d = int(input("Введите количество учеников за каждой партой: "))

# result = (a + b + c + 1) // d
# print(result)

# Задание №3
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.

# a = int(input("В какой вагон от головы состава сел Петя?: "))
# b = int(input("Какой вагон по нумераации?: "))

# if a != b:
#     print((a + b -1))
# else:
#     print("Недостаточно данных!")

# Задание №4
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.

n = int(input("Введите год: "))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("Yes")
else: print("No")

