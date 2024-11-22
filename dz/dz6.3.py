
num = input("Введіть число: ")


while int(num) > 9:
    product = 1

    for digit in num:
        product *= int(digit)

    num = str(product)


print(num)

