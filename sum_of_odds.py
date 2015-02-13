# sum_of_odds.py

n = input("Type n: ")
n = int(n)

total = 0

one = 1

while one <= n:
    if one % 2 == 1:
        total = total + one

    one = one + 1

print(str(total))
