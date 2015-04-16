# pairs.py

def is_prime(n):
    start = 2
    is_prime = True

    while start < n:
        if n % start == 0:
            is_prime = False
            break

        start += 1

    return is_prime


def prime_pair(numbers):
    for x in numbers:
        for y in numbers:
            if is_prime(x + y):
                return True

    return False

print(prime_pair([0, 2, 1, 0, 0]))
