while True:
    num1_input = input("Введіть перше число: ").strip()
    if not num1_input.replace('.', '', 1).isdigit() or num1_input.count('.') > 1:
        print("Помилка: введене значення не є числом.")
        continue
    num1 = float(num1_input)

    operation = input("Введіть операцію (+, -, *, /): ").strip()
    if operation not in ('+', '-', '*', '/'):
        print("Неправильна операція. Спробуйте ще раз.")
        continue

    num2_input = input("Введіть друге число: ").strip()
    if not num2_input.replace('.', '', 1).isdigit() or num2_input.count('.') > 1:
        print("Помилка: введене значення не є числом.")
        continue
    num2 = float(num2_input)

    if operation == '+':
        print(f"Результат: {num1 + num2}")
    elif operation == '-':
        print(f"Результат: {num1 - num2}")
    elif operation == '*':
        print(f"Результат: {num1 * num2}")
    elif operation == '/':
        if num2 == 0:
            print("Помилка: ділення на нуль.")
            continue
        print(f"Результат: {num1 / num2}")

    continue_input = input("Бажаєте продовжити? (yes/y для продовження, будь-який інший ввід для завершення): ").strip().lower()
    if continue_input not in ('yes', 'y'):
        print("Роботу завершено.")
        break




