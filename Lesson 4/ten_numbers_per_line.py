first_number = int(input("Введите начальное число: "))
last_number = int(input("Введите конечное число: "))
numbers_per_line_count = int(input("Введите количество чисел в строке: "))

current_numbers_per_line_count = 1
i = first_number

while i <= last_number:
    print("%3d" % i, end=" ")

    if current_numbers_per_line_count == numbers_per_line_count:
        print()
        current_numbers_per_line_count = 1
    else:
        current_numbers_per_line_count += 1

    i += 1
