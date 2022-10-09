# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def simple_div (a):
    my_list = []
    i = 2
    while a > 1:
        if a % i == 0:
            a = a / i
            my_list.append(i)
        else:
              i += 1
    print(my_list)
    return my_list

simple_div(int(input("Введите число > ")))