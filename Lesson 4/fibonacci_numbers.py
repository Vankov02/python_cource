f_minus_2 = 0
f_minus_1 = 1
number = int(input("Введите номер искомого элемента Фибоначчи: "))
fibonacci_number = 0

for i in range(2, number + 1):
    fibonacci_number = f_minus_2 + f_minus_1
    f_minus_2 = f_minus_1
    f_minus_1 = fibonacci_number

print(f"Число Фибоначчи под номером {number} = {fibonacci_number}")
