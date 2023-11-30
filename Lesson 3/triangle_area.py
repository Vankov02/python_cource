import math

EPSILON = 1.0e-10

print("Введите координаты точек треугольника")

x_1 = float(input("Введите координаты X первой точки: "))
y_1 = float(input("Введите координаты Y первой точки: "))

x_2 = float(input("\nВведите координаты X второй точки: "))
y_2 = float(input("Введите координаты Y второй точки: "))

x_3 = float(input("\nВведите координаты X третьей точки: "))
y_3 = float(input("Введите координаты Y третьей точки: "))

if abs((y_3 - y_2) * (x_1 - x_2) - (x_3 - x_2) * (y_1 - y_2)) <= EPSILON:
    print("\nДанные точки лежат на одной прямой!")
else:
    side_a_length = math.sqrt(pow(x_1 - x_2, 2) + pow(y_1 - y_2, 2))
    side_b_length = math.sqrt(pow(x_2 - x_3, 2) + pow(y_2 - y_3, 2))
    side_c_length = math.sqrt(pow(x_3 - x_1, 2) + pow(y_3 - y_1, 2))

    triangle_semi_perimeter = (side_a_length + side_b_length + side_c_length) / 2
    triangle_area = math.sqrt(triangle_semi_perimeter * (triangle_semi_perimeter - side_a_length) *
                              (triangle_semi_perimeter - side_b_length) * (triangle_semi_perimeter - side_c_length))

    print(f"\nПлощадь треугольника = {triangle_area:.2f}")
