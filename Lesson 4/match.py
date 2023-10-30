operand_1 = float(input("Введите первое число: "))
operand_2 = float(input("Введите второе число: "))
operation = int(input("Введите номер операции над числами: "))

match operation:
    case 1:
        result = operand_1 + operand_2
        print(f"Результат = {result:.2f}")
    case 2:
        result = operand_1 - operand_2
        print(f"Результат = {result:.2f}")
    case 3:
        result = operand_1 * operand_2
        print(f"Результат = {result:.2f}")
    case 4:
        result = operand_1 / operand_2
        print(f"Результат = {result:.2f}")
    case other:
        print("Введена некорректная операция!")
