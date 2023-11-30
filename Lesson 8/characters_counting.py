string = input("Введите строку: ")

digits_count = 0
letters_count = 0
spaces_count = 0
other_symbols_count = 0

for string_element in string:
    if string_element.isdigit():
        digits_count += 1
    elif string_element.isalpha():
        letters_count += 1
    elif string_element.isspace():
        spaces_count += 1
    else:
        other_symbols_count += 1

print(f"Количество букв в данной строке - {letters_count}\n"
      f"Количество цифр в данной строке - {digits_count}\n"
      f"Количество пробелов в данной строке - {spaces_count}\n"
      f"Количество остальных символов в данной строке - {other_symbols_count}")
