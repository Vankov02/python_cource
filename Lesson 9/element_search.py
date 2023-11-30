def get_element_index(elements, element):
    epsilon = 1.0e-10

    for i, list_element in enumerate(elements):
        if abs(list_element - element) < epsilon:
            return i

    return -1


search_element = float(input("Введите искомое число: "))

list_1 = [1.44, 2.54, 3.46, 5.0, 2.11, 9.543, 23.0, 11.12, 23.01]
print(get_element_index(list_1, search_element))

list_2 = [0.87, 4.23, 6.78, 5.43, 2.11, 8.99, 1.44, 12.34, 22.45]
print(get_element_index(list_2, search_element))
