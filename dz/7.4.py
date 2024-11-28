def common_elements():
    # Знаходимо перетин множин без додаткових змінних
    return {x for x in range(100) if x % 3 == 0} & {x for x in range(100) if x % 5 == 0}

# Перевірка
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}


