# user_to_user.py

a = input("Enter a: ")
b = input("Enter b: ")

a = int(a)
b = int(b)

first = a
second = b

if a < b:
    print("Count from " + str(first) + " to " + str(b))

    while first <= b:
        print(first)

        first = first + 1


    print("Count from " + str(b) + " to " + str(a))

    while b >= a:
        print(b)

        b = b - 1


elif a > b:
    print("Count from " + str(b) + " to " + str(first))

    while b <= first:
        print(b)

        b = b + 1


    print("Count from " + str(a) + " to " + str(second))

    while a >= second:
        print(a)

        a = a - 1
