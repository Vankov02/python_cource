# for i in range(101):
#     print(i)
# else:
#     print("\n")
#
# for j in range(7, 122):
#     print(j)
# else:
#     print("\n")
#
# for z in range(100, 29, -1):
#     print(z)
# _________________________________________________________________________________________________
# for i in range(100, 0, -1):
#     if i % 4 == 0:
#         print(i)
#
# print("\n")
#
# n = int(input("Введите n: "))
#
# for i in range(1, n + 1):
#     print(pow(i, 2), end=" ")
#
# start_number = int(input("\nВведите x: "))
# end_number = int(input("Введите y: "))
#
# amount = 0
# count = 0
#
# for i in range(start_number, end_number + 1):
#     amount += i
#     count += 1
#
# average = amount / count
# print("Ср. арифметическое = ", average)
# ______________________________________________________________________________________________________
for i in range(101):
    if (i == 5) or (i % 3 == 0) or (i >= 60) and (i <= 80):
        continue
    print(i)

