import string

# Прямо тут вказуємо дві літери через дефіс
start, end = "a", "c"  # Приклад: "a" та "c"

# Отримуємо всі символи (верхній та нижній регістри)
all_letters = string.ascii_letters

# Визначаємо індекси початкового і кінцевого символів
start_index = all_letters.index(start)
end_index = all_letters.index(end) + 1

# Виводимо результат: всі символи між початковим і кінцевим включно
print(all_letters[start_index:end_index])

