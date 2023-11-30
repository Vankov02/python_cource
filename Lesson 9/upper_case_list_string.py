def get_upper_case_list(elements):
    for i in range(len(elements)):
        elements[i] = elements[i].upper()


list_1 = ["Hello", "my", "friend", "Maslennikov", "Ivan", "pmi", "01"]
get_upper_case_list(list_1)
print(list_1)

list_2 = ["Ivan", "Oleg", "Alexandr", "Yaroslav", "John", "Mike", "Nastya"]
get_upper_case_list(list_2)
print(list_2)
