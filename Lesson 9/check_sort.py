def is_ascending_sort(elements):
    i = 1
    
    while i < len(elements):
        if elements[i] < elements[i - 1]:
            return False

        i += 1

    return True


def is_descending_sort(elements):
    i = 1

    while i < len(elements):
        if elements[i] > elements[i - 1]:
            return False

        i += 1

    return True


list_1 = [1, 2, 3, 4, 5]
list_2 = [5, 4, 3, 2, 1]
list_3 = ["AB", "AB", "aD", "ac", "e", "z"]
list_4 = input("Введите элементы списка через пробел для проверки по возрастанию: ").split()
list_5 = input("Введите элементы списка через пробел для проверки по убыванию: ").split()

print("\nТесты шаблонов:")
print(is_ascending_sort(list_1))
print(is_descending_sort(list_2))
print(is_ascending_sort(list_3))

print("\nТесты ваших списков:")
print(is_ascending_sort(list_4))
print(is_descending_sort(list_5))
