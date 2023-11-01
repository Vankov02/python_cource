numbers_quantity = int(input("Введите количество элементов в ряду: "))

series_sum = 0

for i in range(1, numbers_quantity + 1):
    series_sum += pow(-1, i - 1) * pow(i, 2) if i % 2 == 0 else pow(i, 2)

print(f"Сумма ряда = {series_sum}")
