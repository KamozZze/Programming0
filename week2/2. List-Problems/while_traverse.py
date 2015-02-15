# while_traverse.py

books = ["Learn You a Haskell", 
         "The Healthy Programmer",
         "Code Complete",
         "The Pragmatic Programmer",
         "Pro Git",
         "Introduction to Algorithms",
         "Concrete Mathematics"]

start = 0

while start < len(books):
    book = books[start]
    print(book)

    start += 1
