a1 = int(input('Первый элемент: '))
d = int(input('Разность: '))
n = int(input('Количество элементов: '))

print(*[a1 + (i - 1) * d for i in range(1, n + 1)])
