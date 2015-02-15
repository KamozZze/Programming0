# words_count.py

word_n = input("Enter word: ")
n = input("Enter n: ")
n = int(n)

count = 1
words = []

while count <= n:
    word = input()
    words = words + [word]

    count += 1

count = 0

for word in words:
    if word == word_n:
        count += 1

print(word_n + " is found " + str(count) + " times")
