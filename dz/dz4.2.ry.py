lst = [0, 1, 7, 2, 4, 8]
result = sum(lst[::2]) * lst[-1] if lst else 0

print("Результат:", result)

