# sum_digits.py

n = input("Type n: ")
n = int(n)

total = 0

while n != 0:
    last = n % 10
   
    total += last
    
    n = n // 10

print("Sum of digits is " + str(total))
