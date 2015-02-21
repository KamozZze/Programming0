# first_n_perfect.py

n = input("Enter n: ")
n = int(n)

start = 6

while True:
    sum_divisors = 0
    divisor = 1

    while divisor < start:
        if start % divisor == 0:
            sum_divisors += divisor

        divisor += 1

    if sum_divisors == start:
        print(start)
        n -= 1
    
    if n == 0:
        break

    start += 1

# note: if n >= 4 the program requires more time to load!
