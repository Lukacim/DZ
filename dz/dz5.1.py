
import string
import keyword

def is_valid_variable_name(var_name):
    # Перевірка на порожнє ім'я змінної
    if not var_name:
        return False

    # Перевірка на початок з цифри
    if var_name[0].isdigit():
        return False

    # Перевірка на великі літери
    if any(char.isupper() for char in var_name):
        return False

    # Перевірка на пробіли та знаки пунктуації
    if any(char in string.punctuation.replace("_", "") for char in var_name) or " " in var_name:
        return False

    # Перевірка на жодне із зареєстрованих слів
    if var_name in keyword.kwlist:
        return False

    # Перевірка на кількість підкреслень
    if var_name.count("_") > 1:
        return False

    return True

