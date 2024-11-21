import keyword

name = input("Введіть рядок для перевірки: ").strip()

if name in keyword.kwlist:
    print(False)

elif name[0] in '0123456789':
    print(False)

elif any(char != char.lower() for char in name):
    print(False)

elif any(char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" for char in name) and name != "_":
    print(False)

elif name.count("_") > 1:
    print(False)
else:
    print(True)




