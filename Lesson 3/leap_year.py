input_year = int(input("Введите год, который хотите проверить: "))
result = ""

if (((input_year % 100 == 0) and (input_year % 400 == 0)) or
        ((input_year % 4 == 0) and (input_year % 100 != 0)) or input_year % 4 == 0):
    result = f"{input_year} является високосным!"
else:
    result = f"{input_year} не является високосным!"

print(result)
