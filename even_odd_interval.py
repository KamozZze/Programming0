# even_odd_interval.py

a = input("Enter a: ")
b = input("Enter b: ")

a = int(a)
b = int(b)

while a <= b:

    if a % 2 == 0:
        print(str(a) + " - even")
    else:
        print(str(a) + " - odd")

    a += 1
