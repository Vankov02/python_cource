rectangle_length = float(input("Введите длину прямоугольника: "))
rectangle_width = float(input("Введите ширину прямоугольника: "))

rectangle_perimeter = (rectangle_length + rectangle_width) * 2
rectangle_area = rectangle_length * rectangle_width

print(f"Длина прямоугольника = {rectangle_length:.2f}\n"
      f"Ширина прямоугольника = {rectangle_width:.2f}\n"
      f"Периметр прямоугольника = {rectangle_perimeter:.2f}\n"
      f"Площадь прямоугольника = {rectangle_area:.2f}")
