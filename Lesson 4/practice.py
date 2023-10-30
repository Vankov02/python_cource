# input_string_1 = input("Введите команду: ")
#
# match input_string_1:
#     case "print":
#         input_string_2 = input("Введите строку: ")
#         print(input_string_2)
#     case "sum":
#         number_1 = float(input("Введите первое вещественное число: "))
#         number_2 = float(input("Введите второе вещественное число: "))
#         print("Сумма чисел = ", number_1 + number_2)
#     case other:
#         print("Неизвестная команда!")
i = 3
numbers_sum = 0
count = 0

while i <= 21:
    if i % 2 == 0:
        numbers_sum += i
        count += 1

    i += 1

print(f"Сумма четных чисел = {numbers_sum}\n"
      f"Количество четных чисел = {count}")
