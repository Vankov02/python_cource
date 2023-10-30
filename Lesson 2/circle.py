import math

radius_1 = float(input('Введите радиус окружности: '))
circle_area_1 = math.pi * radius_1 ** 2
diameter_1 = 2 * radius_1
circle_length_1 = math.pi * diameter_1
print(f"Площадь круга с радиусом {radius_1:.2f} = {circle_area_1:.2f}")
print(f"Длина окружности с радиусом {radius_1:.2f} = {circle_length_1:.2f}\n")

circle_area_2 = float(input('Введите площадь круга: '))
radius_2 = math.sqrt(circle_area_2 / math.pi)
print(f"Радиус круга с площадью {circle_area_2:.2f} = {radius_2:.2f}\n")

radius_3 = float(input('Введите радиус окружности: '))
sector_angle_3 = float(input('Введите угол искомого сектора в градусах: '))
sector_area_3 = math.pi * math.pow(radius_3, 2) * sector_angle_3 / 360
print(f"Площадь искомого сектора равна {sector_area_3:.2f}")
