# large_and_small.py

def to_digits(n):
    result = []
    
    while n != 0:
        digit = n % 10
        
        result += [digit]

        n = n // 10

    return result


def to_number(digits):
    result = 0

    for digit in digits:
        result = result * 10 + digit

    return result


def max_number(n):
    digits = to_digits(n)

    digits = sorted(digits, reverse=True)
    
    return to_number(digits)


def min_number(n):
    digits = to_digits(n)

    digits = sorted(digits)

    return to_number(digits)

n = input("Enter n: ")
n = int(n)

print(max_number(n))
print(min_number(n))
