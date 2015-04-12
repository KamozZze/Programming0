# count_words.py

def count_words(words):
    count_words = {}

    for word in words:
        if word not in count_words:
            count_words[word] = 1
        else:
            count_words[word] += 1
    return count_words

print(count_words(["words", "are", "meaningful", "words", "words", "are"]))
