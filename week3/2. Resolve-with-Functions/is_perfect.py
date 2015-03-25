# is_perfect.py

def divisors(n):
    divisors = []

    start = 1
    end = n - 1

    while start <= end:
        if n % start == 0:
            divisors = divisors + [start]

        start += 1

    return divisors

def sum_ints(divisors):
    sum_divisors = 0

    for divisor in divisors:
        sum_divisors += divisor

    return sum_divisors

def sum_divisors(n):
    return sum_ints(divisors(n))


def is_perfect(n):
    return sum_divisors(n) == n

n = input("Enter n: ")
n = int(n)

if is_perfect(n):
    print("The number " + str(n) + " is perfect!")

else:
    print("The number " + str(n) + " isn't perfect!")
