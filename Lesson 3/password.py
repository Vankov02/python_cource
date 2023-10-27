correct_password = "123qwerty"
entered_password = input("Введите пароль:\n")

if correct_password == entered_password:
    print("Пароль верный!")
elif len(entered_password) > len(correct_password):
    print("Пароль неверный, строка слишком длинная")
elif len(entered_password) < len(correct_password):
    print("Пароль неверный, строка слишком короткая")
else:
    print("Пароль неверный!")
