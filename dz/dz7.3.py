def second_index(text, some_str):
    first_index = text.find(some_str)
    if first_index == -1:
        return None

   
    second_index = text.find(some_str, first_index + 1)

    if second_index == -1:
        return None
    return second_index
assert second_index("sims", "s") == 3, 'Test1'  # друге "s" знаходиться на індексі 3
assert second_index("find the river", "e") == 12, 'Test2'  # друге "e" знаходиться на індексі 12
assert second_index("hi", "h") is None, 'Test3'  # другого входження "h" немає
assert second_index("Hello, hello", "lo") == 10, 'Test4'  # друге "lo" знаходиться на індексі 10
print('ОК')
