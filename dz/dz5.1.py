import string
import keyword


def is_valid_variable(name):

    if name[0].isdigit():
        return False

    if any(char.isupper() for char in name):
        return False

    if any(char in string.punctuation and char != '_' for char in name):
        return False

    if name in keyword.kwlist:
        return False

    if name.count('_') > 1:
        return False

    return True

print(is_valid_variable("_"))  # True
print(is_valid_variable("get_value"))  # True
print(is_valid_variable("get value"))  # False
print(is_valid_variable("assert"))  # False
print(is_valid_variable("3m"))  # False
