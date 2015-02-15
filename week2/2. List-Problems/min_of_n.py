# min_of_n.py

n = input("Enter n: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input()
    number = int(number)

    numbers = numbers + [number]

    count += 1

min_n = numbers[0]

for number in numbers:
    if number < min_n:
        min_n = number

print("Min is: " + str(min_n))
