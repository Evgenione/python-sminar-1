a = list(map(int, input('Введите массив: ').split()))

mini = int(input('Min: '))
maxi = int(input('Max: '))
print(*[i for i in range(len(a)) if mini <= a[i] <= maxi])