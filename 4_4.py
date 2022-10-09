# 4.* Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз.

from random import randint
import random

def abc (a):      # Возможно вводить только целые числа. С другими не додумалась...
    with open('result4_4.txt', 'a', encoding='utf-8') as my_f:
        for i in range(a, 0, -1):
            num = randint(0, 9)
            if num == 0:
                continue
            my_list = ['+', '-']
            my_f.write(f" {num}*x^{i} {random.choice(my_list)}")
        my_f.write(f" {num} = 0\n")

    
for i in range(3):
    abc(int(input("Введите показатель степени > ")))