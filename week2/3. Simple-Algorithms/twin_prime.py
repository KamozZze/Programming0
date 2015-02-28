# twin_prime.py

p = input("Enter p: ")
p = int(p)

q1 = p - 2
q2 = p + 2

is_p_prime = True
start = 2

while start < p:
    if p % start == 0:
        is_p_prime = False
        break
    start += 1

is_q1_prime = True
start = 2

while start < q1:
    if q1 % start == 0:
        is_q1_prime = False
        break
    start += 1

is_q2_prime = True
start = 2

while start < q2:
    if q2 % start == 0:
        is_q2_prime = False
        break
    start += 1

if is_p_prime and (not is_q1_prime) and (not is_q2_prime):
    print(str(p) + " is prime, but:")
    print(str(q1) + " is not")
    print(str(q2) + " is not")
elif is_p_prime:
    print("Twin primes with " + str(p) + ":")
    if is_q1_prime:
        print(str(q1) + ", " + str(p))
    if is_q2_prime:
        print(str(p) + ", " + str(q2))
else:
    print(str(p) + " is not a prime.")
