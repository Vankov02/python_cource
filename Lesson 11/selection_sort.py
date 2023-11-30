def selection_sort(elements):
    for i in range(len(elements) - 1):
        j = i + 1
        minimum = elements[i]
        for j in range(len(elements)):
            if elements[j] < minimum:
                minimum = elements[j]
                minimum_index = j

        temp = elements[i]
        elements[i] = minimum
        elements[minimum_index] = temp

    return elements


list_1 = [5, 4, 1, 6, 8, 2]
print(selection_sort(list_1))
