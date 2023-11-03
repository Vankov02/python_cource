initial_boundary = int(input("Введите начальное число: "))
final_boundary = int(input("Введите конечное число: "))
count_numbers_per_string = int(input("Введите количество чисел в строке: "))

string_end = 1
while initial_boundary <= final_boundary:
    while string_end <= count_numbers_per_string and initial_boundary <= final_boundary:
        print("%3d" % initial_boundary, end=" ")
        string_end += 1
        initial_boundary += 1
    print(end="\n")
    string_end = 1
