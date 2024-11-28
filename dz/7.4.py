def common_elements():

    set_3 = {x for x in range(100) if x % 3 == 0}
    set_5 = {x for x in range(100) if x % 5 == 0}

    return set_3 & set_5

assert common_elements() == {0, 15, 30, 45, 60, 75, 90}



