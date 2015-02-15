# int_palindrom.py

n = input("Enter n: ")
n = int(n)

rev_n = 0
nonrev_n = n

while n != 0:
    digit = n % 10

    rev_n = rev_n * 10 + digit

    n = n // 10
    
if nonrev_n == rev_n:
    print("The number " + str(nonrev_n) + " is palindrom")

else:
    print("The number " + str(nonrev_n) + " is not palindrom")
