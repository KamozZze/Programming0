# sum_numbers.py

n = input("Enter n: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input()
    number = int(number)

    numbers = numbers + [number]

    count += 1


total_sum = 0

for number in numbers:
    total_sum += number


print("The sum is: " + str(total_sum))
