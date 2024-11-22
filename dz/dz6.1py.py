import string

start, end = input("Введіть дві літери через дефіс (наприклад, 'a-c'): ").split('-')

all_letters = string.ascii_letters

start_index = all_letters.index(start)
end_index = all_letters.index(end) + 1

print(all_letters[start_index:end_index])
