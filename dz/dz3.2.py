
lst = [1, 2, 3, 4, 5]
if len(lst) > 1:

    last_element = lst.pop()
    lst.insert(0, last_element)

print("Змінений список:", lst)
