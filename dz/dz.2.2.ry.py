
number = 78964
reversed_number = 0
while number > 0:
    reversed_number = reversed_number * 10 + number % 10
    number = number // 10
print(reversed_number)


