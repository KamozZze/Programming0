# print_digits.py

n = input("Type n: ")
n = int(n)

while n != 0:
    last = n % 10
   
    print(last)
    
    n = n // 10
