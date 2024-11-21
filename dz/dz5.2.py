while True:
    # Запит операції
    operation = input("Введіть операцію (+, -, *, /): ").strip()
    if operation not in ('+', '-', '*', '/'):
        print("Неправильна операція. Спробуйте ще раз.")
        continue

    num1_input = input("Введіть перше число: ").strip()
    if not num1_input.replace('.', '', 1).isdigit() or num1_input.count('.') > 1:
        print("Помилка: введене значення не є числом.")
        continue
    num1 = float(num1_input)

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

    continue_input = input("Бажаєте продовжити? (yes/no для продовження): ").strip()
    if continue_input not in ('not', 'yes', 'NOT', 'YES'):
        print("Роботу завершено.")
        break



