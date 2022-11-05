import math
exam = input('Що мені робити з цими числами? (Введіть "+", "-", "*", "/", "^", "k") ')
if exam == '^' or exam == 'k':
    x = int(input('Введіть число: '))
    if exam == '^':
        z = math.pow(x,2)
        print('Квадрат числа дорівнює: ', z)
    elif exam == 'k':
        z = math.sqrt(x)
        print('Корінь числа дорівнює: ', z)
else:
    x = int(input('Введіть перше число: '))
    y = int(input('Введіть друге число: '))
    if exam == '+':
        z = x+y
        print('Результат додавання: ', z)
    elif exam == '-':
        z = x-y
        print('Результат віднімання: ', z)
    elif exam == '*':
        z = x*y
        print('Результат множення: ', z)
    elif exam == '/':
        if y == 0:
            print('На 0 делить нельзя!')
        else:
            z = x/y
            print('Результат ділення: ', z)
