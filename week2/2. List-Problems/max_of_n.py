# max_of_n.py

n = input("Enter n: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input()
    number = int(number)

    numbers = numbers + [number]

    count += 1

max_n = numbers[0]

for number in numbers:
    if number > max_n:
        max_n = number

print("Max is: " + str(max_n))
