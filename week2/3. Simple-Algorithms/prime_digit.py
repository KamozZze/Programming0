# prime_digit.py

n = input("Enter n: ")
n = int(n)

digits = []

while n != 0:
    digit = n % 10

    digits = [digit] + digits 

    n = n // 10

with_prime = False

for digit in digits:
    if digit in [2, 3, 5, 7]:
        with_prime = True

if with_prime:
    print("There is at least 1 prime digit")
else:
    print("There are no prime digits")
