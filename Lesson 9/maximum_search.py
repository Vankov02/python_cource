def get_max(elements):
    maximum = elements[0]

    for element in elements:
        if element > maximum:
            maximum = element

    return maximum


list_1 = [1.44, 2.54, 3.46, 5.0, 1.566, 9.543, 23.0, 11.12, 23.01]
print(get_max(list_1))

list_2 = ["Ivan", "Oleg", "Alexandr", "Yaroslav", "John", "Mike", "Nastya"]
print(get_max(list_2))
