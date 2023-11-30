fibonacci_number_index = int(input("Введите номер искомого элемента Фибоначчи: "))

if fibonacci_number_index == 0:
    fibonacci_number = 0
elif fibonacci_number_index == 1:
    fibonacci_number = 1
else:
    pre_previous_fibonacci_number = 0
    previous_fibonacci_number = 1
    fibonacci_number = 0

    for i in range(2, fibonacci_number_index + 1):
        fibonacci_number = pre_previous_fibonacci_number + previous_fibonacci_number
        pre_previous_fibonacci_number = previous_fibonacci_number
        previous_fibonacci_number = fibonacci_number

print(f"Число Фибоначчи под номером {fibonacci_number_index} = {fibonacci_number}")
