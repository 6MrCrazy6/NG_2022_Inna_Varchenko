import math
print("Введіть коефіцієнти квадратного рівняння: ")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = math.pow(b,2) - 4 * a * c
print('Дискримінант = ', D)
if D<0:
    print('Корнів немає')
elif D == 0:
    x = -b / (2*a)
    print('Рівняння має один корінь, x = ', x)
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print('Корні рівняння x1 = ',  x1, 'x2 = ',  x2)
