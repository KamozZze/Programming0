# grader.py

p = input("Type points: ")

p = int(p)

if p <=50:
    print("Слаб 2")

elif p >= 51 and p <= 60:
    print("Среден 3")

elif p >= 61 and p <= 70:
    print("Добър 4")

elif p >= 71 and p <= 80:
    print("Много Добър 5")

elif p >= 81:
    print("Отличен 6")

elif p == 100:
    print("Много Отличен 7")
