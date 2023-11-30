def get_3x_plus_4y(x, y):
    return 3 * x + 4 * y


print("Сумма =", get_3x_plus_4y(4.678, 5.67))
print("Сумма =", get_3x_plus_4y(3.6868, 3))


def get_average(first_boundary, last_boundary):
    numbers_sum = 0
    numbers_count = 0

    i = first_boundary

    while i <= last_boundary:
        numbers_sum += i
        numbers_count += 1
        i += 1

    return numbers_sum / numbers_count


print("Сумма ряда = ", get_average(1, 6))


def get_max_number(number_1, number_2):
    if number_1 > number_2:
        max_number = number_1
    else:
        max_number = number_2

    return max_number


def get_min_number(number_1, number_2):
    if number_1 < number_2:
        min_num = number_1
    else:
        min_num = number_2

    return min_num


print("Максимальное число из двух = ", get_max_number(10, 8))
print("Минимальное число из двух = ", get_min_number(10, 8))