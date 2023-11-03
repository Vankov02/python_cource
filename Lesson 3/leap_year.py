year = int(input("Введите год, который хотите проверить: "))

if not (year % 4 == 0):
    print(f"{year} является високосным!")
elif not (year % 100 == 0):
    print(f"{year} является високосным!")
elif year % 400 == 0:
    print(f"{year} является високосным!")
else:
    print(f"{year} не является високосным!")
