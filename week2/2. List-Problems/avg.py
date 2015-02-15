# avg.py

n = input("Enter n: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input()
    number = int(number)

    numbers = numbers + [number]

    count += 1


total = 0
count = len(numbers)

for number in numbers:
    total += number

avg = total / count

print("AVG is " + str(avg))
