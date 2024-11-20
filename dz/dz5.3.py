import string
def create_hashtag(input_string):
    cleaned_string = ''.join(char for char in input_string if char not in string.punctuation)
    words = cleaned_string.split()
    capitalized_words = [word.capitalize() for word in words]

    hashtag = '#' + ''.join(capitalized_words)
    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag
print(create_hashtag('Python Community'))
print(create_hashtag('i like python community!'))
print(create_hashtag('Should, I. subscribe? Yes!'))
