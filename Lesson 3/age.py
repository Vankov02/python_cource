user_age = int(input("Введите ваш возраст: "))

if user_age > 112:
    print("Вы слишком стары!")
elif user_age < 1:
    print("Вы слишком молоды!")
elif ((user_age % 100 > 10) and (user_age % 100 < 15)) or (user_age % 10 == 0) or (
        (user_age % 10 > 4) and (user_age % 10 <= 9)):
    print(f"Вам {user_age} лет!")
elif user_age % 10 == 1:
    print(f"Вам {user_age} год!")
else:
    print(f"Вам {user_age} года!")
