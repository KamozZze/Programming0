# int_functions.py

def reverse_int(n):
    result = 0

    while n != 0:
        digit = n % 10
        result = result * 10 + digit

        n = n // 10

    return result

def sum_digits(n):
    result = 0
    
    while n != 0:
        digit = n % 10
        result += digit

        n = n // 10

    return result

def product_digits(n):
    product = 1
    
    while n != 0:
        digit = n % 10
        product *= digit

        n = n // 10

    return product

n = input("Enter number: ")
n = int(n)

print ("Reversed number:", reverse_int(n))
print ("Sum of digits:", sum_digits(n))
print ("Product of the digits:", product_digits(n))
