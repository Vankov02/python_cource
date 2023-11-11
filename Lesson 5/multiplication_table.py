start_number = 1
end_number = int(input("Введите размерность таблицы: "))

for i in range(1, end_number + 1):
    if i == 1:
        print("%3s" % " ", end=" | ")

        for j in range(1, end_number + 1):
            print("%3d" % j, end=" ")

        print()
        print("%3s" % "---", end=" | ")

        for j in range(1, end_number + 1):
            print(end="----")

        print()

    for j in range(1, end_number + 1):
        result = i * j

        if j == 1:
            print("%3d" % result, end=" | ")
            
        print("%3d" % result, end=" ")

    print(end="\n")
