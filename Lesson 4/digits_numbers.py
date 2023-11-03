number = int(input("Введите число: "))
out_number = number
amount = 0
max_digit = 0
odd_digits_amount = 0

while number != 0:
    temp_1 = number % 10
    number = number // 10
    if temp_1 % 2 == 1:
        odd_digits_amount += temp_1
    if temp_1 > max_digit:
        max_digit = temp_1
    amount += temp_1
    temp_1 = number

print(f"\nСумма цифр числа {out_number} = {amount}\n"
      f"Сумма нечетных цифр данного числа = {odd_digits_amount}\n"
      f"Максимальная цифра в данном числе = {max_digit}")
