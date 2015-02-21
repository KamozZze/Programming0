# sum_divisors.py

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

print("Sum of divisors is:")
print(sum_divisors)
