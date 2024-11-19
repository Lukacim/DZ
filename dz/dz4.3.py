import random
initial_list = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
new_list = [initial_list[0], initial_list[2], initial_list[-2]]
print("Initial list:", initial_list)
print("New list:", new_list)
