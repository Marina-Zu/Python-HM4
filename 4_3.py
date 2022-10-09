# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности в том же порядке.

from random import randint

def fine_number(num):
    my_list = []
    if num > 0:
        arr = [randint(0, 9) for i in range(num)]
        print(arr) 
        for i in arr:
             itog = arr.count(i)
             if itog == 1:
                 my_list.append(i)
    else:
        print("Error value!")
    return my_list

num = int(input("Введите число элементов > "))
print(fine_number(num))