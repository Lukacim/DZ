num = input("Введіть число: ")
while int(num) > 9:
    number = 1
    for digit in num:
        number *= int(digit)

    num = str(number)

print(num)
