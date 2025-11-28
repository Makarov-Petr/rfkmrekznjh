print("добро пожаловать в калькулятор, дорогой пользователь")
while True:
    i = 0
    print("Наш калькулятор предоставляет такие возможности как: +, -, *, /, **, sqrt, digits, если хотите выйти, напишите exit")
    operation = input("введите операцию сюда: ")
    if operation == "exit":
        print("приходите ещё!")
        break
    if operation in ['+', '-', '*', '/', '**']:
        a = float(input("введите первое число: "))
        b = float(input("введите второе число: "))
        if operation == "+":
            i = a + b
            print(a, operation, b, '=', i)
        elif operation == "-":
            i = a - b
            print(a, operation, b, '=', i)
        elif operation == "*":
            i = a * b
            print(a, operation, b, '=', i)
        elif operation == "/":
            if b != 0:
                i = a / b
                print(a, operation, b, '=', i)
            else:
                print("Ошибка: деление на ноль!")
        elif operation == "**":
            i = a ** b
            print(a, operation, b, '=', i)
    elif operation == "sqrt":
        a = float(input("введите число из которого мы извлечём квадратный корень: "))
        if a >= 0:
            i = a ** 0.5
            print(i)
        else:
            print("Ошибка: нельзя извлечь корень из отрицательного числа")
    elif operation == "digits":
        a = float(input("введите число для подсчёта разрядов: "))
        integer_part = abs(int(a))
        if integer_part == 0:
            print(1)
        else:
            print(len(str(integer_part)))
    else:
        print("данной операции не существует, прочитайте возможные и введите одну из них")