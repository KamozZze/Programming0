# divisors.py

def divisors(n):
    divisors = []

    start = 1
    end = n - 1

    while start <= end:
        if n % start == 0:
            divisors = divisors + [start]

        start += 1

    return divisors


n = input("Enter n: ")
n = int(n)

print("Divisors are: ")
print(divisors(n))
