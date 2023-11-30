import math

EPSILON = 1.0e-10

a = float(input("Введите коэффициент при x^2: "))
b = float(input("Введите коэффициент при x: "))
c = float(input("Введите свободный член: "))

if (abs(a - 0) < EPSILON and abs(b - 0) < EPSILON and
        abs(c - 0) < EPSILON or a - 0 > EPSILON and b - 0 > EPSILON and c - 0 > EPSILON):
    print("x принадлежит R")
elif abs(a - 0) < EPSILON and abs(b - 0) < EPSILON:
    print("Решение данного уравнения: пустое множество")
elif abs(a - 0) < EPSILON and abs(c - 0) < EPSILON or abs(b - 0) < EPSILON and abs(c - 0) < EPSILON:
    print("Решение данного уравнения: x = 0")
elif abs(a - 0) < EPSILON:
    result = -c / b
    print(f"Решение данного уравнения: x = {result}")
else:
    discriminant = b ** 2 - 4 * a * c
    result_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    result_2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Решение данного уравнения: x_1 = {result_1}, x_2 = {result_2}")

# elif 0 - discriminant > EPSILON:
#     print("Корней решения данного уравнения нет!")
# elif abs(discriminant - 0) < EPSILON:
#     result_1 = -b / (2 * a)
#     print(f"Корень решения данного уравнения: {result_1}")
# else:
#     result_1 = (-b + math.sqrt(discriminant)) / (2 * a)
#     result_2 = (-b - math.sqrt(discriminant)) / (2 * a)
#     print(f"Корни решения данного уравнения: {result_1} и {result_2}")
