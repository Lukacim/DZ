import keyword
import string


variable_name = input("Введіть ім'я змінної: ").strip()


if variable_name in keyword.kwlist:
    print(False)

elif variable_name[0].isdigit():
    print(False)

elif any(char.isupper() for char in variable_name):
    print(False)

elif any(char in string.punctuation for char in variable_name) and variable_name != "_":
    print(False)

elif variable_name.count('_') > 1:
    print(False)
else:
    print(True)





