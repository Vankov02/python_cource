age = int(input("Введите ваш возраст: "))
age_per_100_multiple = age % 100
age_per_10_multiple = age % 10

if age > 112:
    print("Вы слишком стары!")
elif age < 1:
    print("Вы слишком молоды!")
elif 10 <= age_per_100_multiple < 15 or age_per_10_multiple == 0 or 4 < age_per_10_multiple <= 9:
    print(f"Вам {age} лет!")
elif age % 10 == 1:
    print(f"Вам {age} год!")
else:
    print(f"Вам {age} года!")
