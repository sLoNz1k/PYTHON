# def sumNumber(n) :
#     summa = 0
#     for i in range(1, n+1) :
#         summa += i
#     return summa
#     print('stop')
# a = sumNumber(5)
# print(a)


# Неограниченное количество аргументов в функции
# def sum_str(*args):
#     res = ''
#     for i in args :
#         res += i
#     return res
# print(sum_str('5+1'+ '+e+'+ '3'))
# print(sum_str(1 + 3 + 4))

# import module

# print(module.max1(5,9))

# from module import max1 # если вместо max1 поставить * , то будут импортированы все функции
# print(max1(10,9))

# import module as m1 # вариант со сменой названия модуля прямо в коде
# print(m1.max1(10,9))


# Рекурсия. Числа фиббоначи
# def fib(n) :
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# list_1 = []
# for i in range(1, 10) :
#     list_1.append(fib(i))
# print(list_1)

# Быстрая сортировка
# def quick_sort(array) :
#     if len(array) <= 1 :
#         return array
#     else :
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# print(quick_sort([10, 5 ,2 ]))

# Сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        print(right,left)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)

