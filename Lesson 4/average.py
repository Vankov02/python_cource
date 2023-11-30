first_number = int(input("Введите начальную границу: "))
last_number = int(input("Введите конечную границу: "))

numbers_sum = 0
numbers_count = 0

even_numbers_sum = 0
even_numbers_count = 0

i = first_number

while i <= last_number:
    if i % 2 == 0:
        even_numbers_sum += i
        even_numbers_count += 1

    numbers_sum += i
    numbers_count += 1
    i += 1

numbers_average = numbers_sum / numbers_count
even_numbers_average = even_numbers_sum / even_numbers_count

print(f"Среднее арифметическое чисел с {first_number} по {last_number} = {numbers_average:.2f}")
print(f"Среднее арифметическое четных чисел с {first_number} по {last_number} = {even_numbers_average:.2f}")
