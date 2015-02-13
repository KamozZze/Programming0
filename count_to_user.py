# count_to_user.py

n = input("Enter number: ")
n = int(n)
start = 1

print("Count from 1 to " + str(n))

while start <= n:
    print(start)

    start = start + 1

print("Count from " + str(n) +" to 1")

start = n
end = 1

while start >= end:
    print(start)

    start = start - 1
