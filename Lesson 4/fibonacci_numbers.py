fibonacci_number_element = int(input("Введите номер искомого элемента Фибоначчи: "))

fibonacci_number = 0

if fibonacci_number_element == 0:
    fibonacci_number = 0
elif fibonacci_number_element == 1:
    fibonacci_number = 1
else:
    pre_previous_element = 0
    previous_element = 1

    for i in range(2, fibonacci_number_element + 1):
        fibonacci_number = pre_previous_element + previous_element
        pre_previous_element = previous_element
        previous_element = fibonacci_number

print(f"Число Фибоначчи под номером {fibonacci_number_element} = {fibonacci_number}")
