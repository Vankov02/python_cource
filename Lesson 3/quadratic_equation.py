import math

EPSILON = 1.0e-10

a = float(input("Введите коэффициент при x^2: "))
b = float(input("Введите коэффициент при x: "))
c = float(input("Введите свободный член: "))

if abs(a - 0) < EPSILON:
    if abs(b - 0) < EPSILON:
        if abs(c - 0) < EPSILON:
            print("0 = 0")
        else:
            print("Корней нет!")
    else:
        print(f"Решение данного уравнения: x = {-c / b:.3f}")
else:
    discriminant = b ** 2 - 4 * a * c

    if 0 - discriminant > EPSILON:
        print("Корней нет!")
    else:
        result_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        result_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Решение данного уравнения: x_1 = {result_1:.3f}, x_2 = {result_2:.3f}")
