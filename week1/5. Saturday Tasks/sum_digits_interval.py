# sum_digits_interval.py

n = input("Type n: ")
m = input("Type m: ")
n = int(n)
m = int(m)

if n < m:
    start = n
    end = m

elif n > m:
    start = m
    end = n


while start <= end:
    n = start
    total = 0

    while n != 0:
        digit = n % 10
        total += digit
        n = n // 10

    print("Sum of digits of " + str(start) + " = " + str(total))
    start += 1

