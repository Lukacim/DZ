# Початковий список
lst = [1, 2, 3, 4, 5]

middle_index = (len(lst) + 1) // 2
result = [lst[:middle_index], lst[middle_index:]]

# Виводимо результат
print("Розділений список:", result)
