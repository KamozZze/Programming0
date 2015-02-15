# is_prime.py

n = input("Enter n: ")
n = int(n)

start = 2
is_prime = True

if n == 1:
    is_prime = False

while start < n:
    if n % start == 0:
        is_prime = False
        break
    start += 1

if is_prime:
    print("It's prime!")
else:
    print("It's not prime!")
