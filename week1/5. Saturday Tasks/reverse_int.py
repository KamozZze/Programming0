# reverse_int.py

n = input("Enter n: ")
n = int(n)

rev_n = 0

while n != 0:
    digit = n % 10

    rev_n = rev_n * 10 + digit

    n = n // 10

print("The reversed number is: " + str(rev_n))
