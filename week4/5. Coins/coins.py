# coins.py

def calculate_coins(sum_coins):
    result = {}
    coins = [100, 50, 20, 10, 5, 2, 1]
    sum_coins *= 100

    for coin in coins:
        times_to_pay = sum_coins // coin

        result[coin] = times_to_pay

        sum_coins -= times_to_pay * coin

    return result

print(calculate_coins(0.53))
print(calculate_coins(8.94))
