# normal Задание-1
x = int(input("Введите трёхзначное число "))
a = x % 10
a1 = x // 10
b = a1 % 10
b1 = a1 // 10
c = b1 % 10
c1 = b1 // 10
if 100 <= x <= 999:
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    elif c >= a and c >= b:
        print(c)
else:
    print('Введено не трёхзначное число')

# normal Задание-2
a = int(input('Введите значение переменной а '))
b = int(input('Введите значение переменной b '))
a = a + b
b = a - b
a = a - b
print(a, b)

# normal Задание-3
print("Решаем уравнение ax^2 + bx + c = 0, где:")
a = int(input('а = '))
b = int(input('b = '))
c = int(input('с = '))
print('Вычисляем дискриминант:')
d = b ** 2 - (4 * a * c)
print('Дискриминант ', d)
print('Находим корни уравнения:')
if d > 0:
    import math

    x1 = (-b + (math.sqrt(d)) / (2 * a))
    x2 = (-b - (math.sqrt(d)) / (2 * a))
    print("x1= ", x1, "x2= ", x2)
elif d == 0:
    x1 = -b / (2 * a)
    print("x1 =  ", x1, "x2 = ", d)
else:
    print('Корней нет.')
