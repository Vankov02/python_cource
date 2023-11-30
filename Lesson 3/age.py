age = int(input("Введите ваш возраст: "))

if age > 112:
    print("Вы слишком стары!")
elif age < 1:
    print("Вы слишком молоды!")
else:
    age_last_two_digits = age % 100
    age_last_digit = age % 10
    
    if age_last_two_digits in [10, 11, 12, 13, 14] or age_last_digit in [0, 5, 6, 7, 8, 9]:
        print(f"Вам {age} лет!")
    elif age_last_digit == 1:
        print(f"Вам {age} год!")
    else:
        print(f"Вам {age} года!")
