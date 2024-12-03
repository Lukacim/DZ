def popular_words(text, words):

    text_words = text.lower().split()
    return {word: text_words.count(word) for word in words}

# Перевірка
assert popular_words('''When I was One I had just begun When I was Two I was nearly new''',
                     ['one', 'two', 'three']) == {'one': 1, 'two': 1, 'three': 0}, "Test 1 Failed"
assert popular_words('Hello world! Hello everyone.', ['hello', 'world', 'python']) == {'hello': 2, 'world': 1, 'python': 0}, "Test 2 Failed"
assert popular_words('', ['hello', 'world']) == {'hello': 0, 'world': 0}, "Test 3 Failed"
assert popular_words('Python python PyThoN!', ['python']) == {'python': 3}, "Test 4 Failed"

print("Усі тести пройдено успішно!")
