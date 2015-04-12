# hash_them.py

def hash_them(keys, values):
    result = {}
    
    index = 0

    for key in keys:
        if index < len(values):
            result[key] = values[index]
        else:
            result[key] = None

        index += 1

    
    return result


print(hash_them(["Ivan", "Maria"], [1, 2]))
print(hash_them(["Ivan", "Maria"], [1]))
