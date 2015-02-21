# is_perfect.py

n = input("Enter n: ")
n = int(n)

divisors = []

start = 1
end = n - 1

while start <= end:
    if n % start == 0:
        divisors = divisors + [start]

    start += 1

sum_divisors = 0

for divisor in divisors:
    sum_divisors += divisor

if sum_divisors == n:
    print("The number " + str(n) + " is perfect!")

else:
    print("The number " + str(n) + " isn't perfect!")
