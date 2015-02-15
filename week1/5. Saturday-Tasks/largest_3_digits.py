# largest_3_digits.py

n = input("Type n: ")
n = int(n)

z = n % 10
n = n // 10

y = n % 10
n = n // 10

x = n % 10
n = n // 10


if (y > x > z) or (z > x > y):
    largest = y

elif (y > z > x) or (z > y > x):
    largest = z

else:
    largest = x


if (y < x < z) or (y < z < x):
    smallest = y

elif (z < x < y) or (z < y < x):
    smallest = z

else:
    smallest = x


if (largest == z and smallest == y) or (smallest == z and largest == y):
    middle = x
elif (largest == z and smallest == x) or (smallest == z and largest == x):
    middle = y


max_number = largest * 100 + middle * 10 + smallest
min_number = smallest * 100 + middle * 10 + largest

print("Max number with those digits is: " + str(max_number))
print("Min number with those digits is: " + str(min_number))
