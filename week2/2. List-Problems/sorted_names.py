# sorted_names.py

n = input("Enter n: ")
n = int(n)

count = 1
names = []

while count <= n:
    name = input()

    names = names + [name]

    count += 1

names = sorted(names)

print("Sorted names are:")

for name in names:
    print(name)
