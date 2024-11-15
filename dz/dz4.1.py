
lst = [0, 1, 0, 12, 3]

lst = [x for x in lst if x != 0] + [0] * lst.count(0)

print("Змінений список:", lst)
