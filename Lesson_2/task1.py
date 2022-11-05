from collections import Counter
st = input('Введіть рядок: \n')
s = len(st)
print('Довжина рядка = ', s)
print(dict(Counter(st)))
print(sorted(st))
