import math
print("Введите координаты точек треугольника")
first_point_x = float(input("Введите координаты X первой точки: "))
first_point_y = float(input("Введите координаты Y первой точки: "))

second_point_x = float(input("\nВведите координаты X второй точки: "))
second_point_y = float(input("Введите координаты Y второй точки: "))

third_point_x = float(input("\nВведите координаты X третьей точки: "))
third_point_y = float(input("Введите координаты Y третьей точки: "))

if ((third_point_y - second_point_y) * (first_point_x - second_point_x) == (third_point_x - second_point_x) *
        (first_point_y - second_point_y)):
    print("\nДанные точки лежат на одной прямой!")
else:
    side_length_a = math.sqrt(pow((first_point_x - second_point_x), 2) + pow((first_point_y - second_point_y), 2))
    side_length_b = math.sqrt(pow((second_point_x - third_point_x), 2) + pow((second_point_y - third_point_y), 2))
    side_length_c = math.sqrt(pow((third_point_x - first_point_x), 2) + pow((third_point_y - first_point_y), 2))

    triangle_semiperimeter = (side_length_a + side_length_b + side_length_c) / 2
    triangle_area = math.sqrt(
        triangle_semiperimeter * (triangle_semiperimeter - side_length_a) * (triangle_semiperimeter - side_length_b) *
        (triangle_semiperimeter - side_length_c))

    print(f"\nПлощадь треугольника = {round(triangle_area, 2)}")
