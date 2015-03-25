# begin_functions.py

def square(x):
    return x**2


def fact(x):
    counter = 1
    result = 1

    while counter <= x:
        result *= counter
        counter += 1

    return result


def count_elements(items):
    items_n = 0
    for item in items:
        items_n += 1
    return items_n


def member(x, xs):
    for memb in xs:
        if x == memb:
            return True
        else:
            return False


def grades_that_pass(students, grades, limit):
    passed = []
    index = 0

    for grade in grades:
        student = students[index]
        
        if grade >= limit:
            passed += [student]

        index += 1

    return passed
