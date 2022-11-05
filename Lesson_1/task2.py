import math
exam = input('Що мені робити з цими числами? (Введіть "+", "-", "*", "/", "^", "k") ')
if exam == '^' or exam == 'k':
    a = int(input('Введіть число: '))
    if exam == '^':
        z = math.pow(a,2)
        print('Квадрат числа дорівнює: ', z)
    elif exam == 'k':
        z = math.sqrt(a)
        print('Корінь числа дорівнює: ', z)
else:
    a = int(input('Введіть перше число: '))
    b = int(input('Введіть друге число: '))
    if exam == '+':
        z = a+b
        print('Результат додавання: ', z)
    elif exam == '-':
        z = a-b
        print('Результат віднімання: ', z)
    elif exam == '*':
        z = a*b
        print('Результат множення: ', z)
    elif exam == '/':
        if b == 0:
            print('На 0 делить нельзя!')
        else:
            z = a/b
            print('Результат ділення: ', z)
