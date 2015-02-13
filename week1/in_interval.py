# in_interval.py

a = input("Lower bound: ")
b = input("Upper bound: ")
x = input("Enter x: ")

a = int(a)
b = int(b)
x = int(x)

if x == a:
    print("The number is equal to the lower bound of the interval")

elif x == b:
    print("The number is equal to the upper bound of the interval")

elif a < x < b:
    print("The number is in the interval")

elif x < a:
    print("The number is outside the interval, x < a")

elif x > b:
    print("The number is outside the interval, x > b")
