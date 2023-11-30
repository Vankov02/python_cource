correct_string = "Hello"

flag = False

while flag is False:
    user_string = input("Введите строку: ")

    if user_string == correct_string:
        print("Строки совпадают!")
        break
    else:
        print("Строка неверна!")
