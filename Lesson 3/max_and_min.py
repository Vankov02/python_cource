number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

if number_1 > number_2:
    max_number_1 = number_1
    min_number_1 = number_2
else:
    max_number_1 = number_2
    min_number_1 = number_1

if max_number_1 == min_number_1:
    print(f"Числа {number_1} и {number_2} равны\n")
else:
    print(f"Наибольшее из этих чисел = {max_number_1}\n"
          f"Наименьшее из этих чисел = {min_number_1}")

max_number_2 = number_1 if number_1 > number_2 else number_2
min_number_2 = number_1 if number_1 < number_2 else number_2

print(f"Максимальное число, определенное с помощью тернарного оператора = {max_number_2}\n"
      f"Минимальное число, определенное с помощью тернарного оператора = {min_number_2}")
