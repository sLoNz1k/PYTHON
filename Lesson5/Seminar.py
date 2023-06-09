import FibaFun

# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию
# print(Fiba(8))
# ___________________________________________________________

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

myList = [6,5,4,3,1,2,4,5]
# print(max(myList),min(myList))

# for i in range(len(myList)) :
#     if myList[i] == max(myList) :
#         myList[i] = min(myList)
#         print(myList[i])
# print(myList)

# Быстрая сортировка
def quick_sort(array) :
    if len(array) <= 1 :
        return array
    else :
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort(myList))