def convert_degrees_celsius_to_degrees_kelvin(celsius_temperature):
    return 273.15 + celsius_temperature


def convert_degrees_celsius_to_degrees_fahrenheit(celsius_temperature):
    return 32 + 1.8 * celsius_temperature


celsius = float(input("Введите температуру в градусах Цельсия: "))

print(f"Температура в градусах Кельвина = {convert_degrees_celsius_to_degrees_kelvin(celsius)} K\n"
      f"Температура в градусах Фаренгейта = {convert_degrees_celsius_to_degrees_fahrenheit(celsius)} F")
