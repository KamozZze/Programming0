# only_evens.py

n = input("Enter n: ")
n = int(n)

count = 1
even_n = []

while count <= n:
    num = input()
    num = int(num)

    if num % 2 == 0:
        even_n += [num]

    count += 1

print("Count of evens: " + str(len(even_n)))
print("Evens are: ")

for even in even_n:
    print(even)
