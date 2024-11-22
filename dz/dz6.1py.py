import string

def get_range(letters_range):

    start, end = letters_range.split('-')


    all_letters = string.ascii_letters

    start_index = all_letters.index(start)
    end_index = all_letters.index(end) + 1


    return all_letters[start_index:end_index]

print(get_range("a-c"))
print(get_range("a-a"))
print(get_range("s-H"))
print(get_range("a-A"))
