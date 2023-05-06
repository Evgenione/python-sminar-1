def power(A, B):
    if (B == 1):
        return (A)
    if (B != 1):
        return (A * power(A, B - 1))
A = int(input("Введите число: "))
B = int(input("Введите его степень: "))
print( 'A =',A, 'B =',B, "->", power(A, B))