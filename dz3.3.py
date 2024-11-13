def split_list(lst):
    if len(lst) == 0:
        return [[], []]

    middle = (len(lst) + 1) // 2

    first_half = lst[:middle]
    second_half = lst[middle:]

    return [first_half, second_half]



print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))
