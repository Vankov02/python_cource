file = open("input.txt", "r", encoding='utf-8')

numbers_line = file.readline()

file.close()

numbers_strings = numbers_line.split(" ")
numbers = []

for number_string in numbers_strings:
    numbers.append(float(number_string))

print(numbers)