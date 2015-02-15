# factorial.py

n = input("Enter n: ")
n = int(n)

start = 1
result = 1

while start <= n:
    result = result * start
    start = start + 1

print(result)
