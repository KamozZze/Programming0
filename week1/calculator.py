# calculator.py

a = input("Enter a: ")
b = input("Enter b: ")
oper = input("Enter operation: ")

result = False

a = int(a)
b = int(b)

if oper == "+":
    result = a+b
elif oper == "-":
    result = a-b
elif oper == "/":
    result = a/b
elif oper == "*":
    result = a*b

if result == False:
    print("We do not support that operation.")
else:
    print("Result is:")
    print(result)
