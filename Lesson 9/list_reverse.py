def get_reverse_list(elements):
    i = 0
    list_middle = len(elements) // 2

    while i < list_middle:
        temp = elements[i]
        elements[i] = elements[-1 - i]
        elements[-1 - i] = temp

        i += 1


list_1 = [1.44, 2.54, 3.46, 5.0, 2.11, 9.543, 23.0, 11.12, 5]
list_2 = [0.87, 4.23, 6.78, 5.43, 2.11, 8.99, 1.44, 12.34]
list_3 = ["Ivan", "Oleg", "Alexandr", "Yaroslav", "John", "Mike", "Nastya"]

get_reverse_list(list_1)
get_reverse_list(list_2)
get_reverse_list(list_3)

print(list_1)
print(list_2)
print(list_3)
