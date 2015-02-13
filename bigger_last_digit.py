# bigger_last_digit.py

n = input("Type n: ")
m = input("Type m: ")

n = int(n)
m = int(m)

if n % 10 > m % 10:
    print(str(n))

elif n % 10 < m % 10:
    print(str(m))

elif n % 10 == m % 10:
    if n > m:
        print(str(n))

    else:
        print(str(m))


