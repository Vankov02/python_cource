import math

coefficient_for_x_2 = float(input("Введите коэффициент при x^2: "))
coefficient_for_x = float(input("Введите коэффициент при x: "))
free_term_coefficient = float(input("Введите свободный член: "))

discriminant = coefficient_for_x ** 2 - 4 * coefficient_for_x_2 * free_term_coefficient

if coefficient_for_x_2 == 0:
    result_1 = -free_term_coefficient / coefficient_for_x
    print(f"Корень решения данного уравнения: {result_1}")
elif discriminant < 0:
    print("Корней решения данного уравнения нет!")
elif discriminant == 0:
    result_1 = -coefficient_for_x / (2 * coefficient_for_x_2)
    print(f"Корень решения данного уравнения: {result_1}")
else:
    result_1 = (-coefficient_for_x + math.sqrt(discriminant)) / (2 * coefficient_for_x_2)
    result_2 = (-coefficient_for_x - math.sqrt(discriminant)) / (2 * coefficient_for_x_2)
    print(f"Корни решения данного уравнения: {result_1} и {result_2}")
