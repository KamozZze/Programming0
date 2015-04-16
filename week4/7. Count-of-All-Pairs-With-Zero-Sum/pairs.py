# pairs.py

def count_zero_pairs(numbers):
    count = 0
    n = len(numbers)

    for x in numbers:
        for y in range(x, n):
            if x + y == 0:
                count += 1

    return count


numbers = [0, 2, -2, 5, 10]

print(count_zero_pairs(numbers))
