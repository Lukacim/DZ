import string

input_string = input("Введіть рядок для створення хештегу: ").strip()

clean_string = ''.join(char for char in input_string if char not in string.punctuation)

hashtag = '#' + ''.join(word.title() for word in clean_string.split())

hashtag = hashtag[:140]

print("Ваш хештег:", hashtag)



