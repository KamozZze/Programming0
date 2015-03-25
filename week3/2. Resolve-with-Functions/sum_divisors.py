# sum_divisors.py

def sum_divisors(n):
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

n = input("Enter n: ")
n = int(n)

print("Sum of divisors is:")
print(sum_ints(sum_divisors(n)))
