def calculator():
    while True:
        try:
            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть оператор (+, -, *, /): ")
            num2 = float(input("Введіть друге число: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Ділення на нуль неможливе!")
                    continue
                result = num1 / num2
            else:
                print("Невідомий оператор!")
                continue

            print(f"Результат: {result}")

        except ValueError:
            print("Некоректний ввід! Спробуйте ще раз.")
            continue
        cont = input("Бажаєте виконати нове обчислення? (y/n): ").lower()
        if cont != 'y':
            print("Дякую за використання калькулятора! До побачення!")
            break

calculator()
