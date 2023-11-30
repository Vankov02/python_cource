number = int(input("Введите число: "))

digits_sum = 0
max_digit = 0
odd_digits_sum = 0
i = number

while i != 0:
    digit = i % 10

    if digit % 2 == 1:
        odd_digits_sum += digit

    if digit > max_digit:
        max_digit = digit

    digits_sum += digit
    i //= 10

print(f"\nСумма цифр числа {number} = {digits_sum}\n"
      f"Сумма нечетных цифр данного числа = {odd_digits_sum}\n"
      f"Максимальная цифра в данном числе = {max_digit}")
