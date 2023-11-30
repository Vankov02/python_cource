def get_even_numbers_arithmetic_mean(numbers):
    even_numbers_sum = 0
    even_numbers_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_numbers_sum += number
            even_numbers_count += 1

    if even_numbers_count != 0:
        return even_numbers_sum / even_numbers_count

    return -1


numbers_list_1 = [2, 4, 5, 3, 10, 11]
numbers_list_2 = [1, 3, 5, 3, 11, 11]

print(get_even_numbers_arithmetic_mean(numbers_list_1))
print(get_even_numbers_arithmetic_mean(numbers_list_2))
