# 1. Вычислить число c заданной точностью d.


from decimal import Decimal


def accuracy (number):
    number = number.quantize(Decimal(str(input("Введите точность в формате '0.0001' > "))))
    print(number) 
    return number

number = Decimal((input("Введите число > ")))
print(accuracy(number))