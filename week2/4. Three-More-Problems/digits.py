# digits.py

n = input("Enter n: ")
n = int(n)

digits = []

while n != 0:
    digit = n % 10
    digits = [digit] + digits
    n = n // 10

print("List of digits is: " + str(digits))

n2 = 0

for digit in digits:
    n2 = n2 * 10 + digit

print("Number is: " + str(n2))
