import math

entrances_count = int(input("Введите количество подъездов в доме: "))
floors_count = int(input("Введите количество этажей в доме: "))
flat_number = int(input("Введите номер искомой квартиры: "))

APARTMENTS_PER_FLOOR_AMOUNT = 4

if (flat_number < 1) or (flat_number > floors_count * entrances_count * APARTMENTS_PER_FLOOR_AMOUNT):
    print("Такой квартиры нет в данном доме!")
else:
    entrance_number = math.ceil(flat_number / (floors_count * APARTMENTS_PER_FLOOR_AMOUNT))

    floor_number = ((flat_number - floors_count * APARTMENTS_PER_FLOOR_AMOUNT * (entrance_number - 1) - 1)
                    // APARTMENTS_PER_FLOOR_AMOUNT + 1)

    apartment_location = flat_number % APARTMENTS_PER_FLOOR_AMOUNT

    if apartment_location == 0:
        apartment_position = "Ближняя справа"
    elif apartment_location == 1:
        apartment_position = "Ближняя слева"
    elif apartment_location == 2:
        apartment_position = "Дальняя слева"
    else:
        apartment_position = "Дальняя справа"

    print(f"\nКвартира находится в подъезде № {entrance_number}\n"
          f"На этаже № {floor_number}\n"
          f"И имеет расположение: {apartment_position}")
