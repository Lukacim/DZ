
number = int(input("Введіть число: "))
result1 = divmod(number, 2)
result2 = divmod(result1[0], 3)
result3 = divmod(result2[0], 4)
result4 = divmod(result3[0], 5)

print("Результат 1:", result1)
print("Результат 2:", result2)
print("Результат 3:", result3)
print("Результат 4:", result4)
