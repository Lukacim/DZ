
import string
import keyword

def is_valid_variable_name(var_name):

    if not var_name:
        return False

    if var_name[0].isdigit():
        return False

    if any(char.isupper() for char in var_name):
        return False

    if any(char in string.punctuation.replace("_", "") for char in var_name) or " " in var_name:
        return False

    if var_name in keyword.kwlist:
        return False

    if var_name.count("_") > 1:
        return False

    return True

