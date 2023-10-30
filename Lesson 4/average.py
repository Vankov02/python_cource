initial_boundary = int(input("Введите начальную границу: "))
final_boundary = int(input("Введите конечную границу: "))
numbers_amount = 0
numbers_count = 0
even_numbers_amount = 0
even_numbers_count = 0

for i in range(initial_boundary, final_boundary + 1):
    numbers_amount += i
    numbers_count += 1

for i in range(initial_boundary, final_boundary + 1):
    if i % 2 == 0:
        even_numbers_amount += i
        even_numbers_count += 1

all_numbers_average = numbers_amount / numbers_count
even_numbers_average = even_numbers_amount / even_numbers_count

print(f"Среднее арифметическое чисел с {initial_boundary} по {final_boundary} = {all_numbers_average:.2f}")
print(f"Среднее арифметическое четных чисел с {initial_boundary} по {final_boundary} = {even_numbers_average:.2f}")
