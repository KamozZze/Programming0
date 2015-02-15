# dice_1001.py

from random import randint

mariya_score = 1001
ivan_score = 1001

while True:
    counter = 1
    diceroll_sum = 0

    while counter <= 6:
        diceroll = randint(1, 6)
        
        diceroll_sum += diceroll
        
        counter += 1

    if mariya_score > 0:
        mariya_score -= diceroll_sum

    elif mariya_score < 0:
        mariya_score += diceroll_sum

    print("Mariya rolls " + str(diceroll_sum) + " and have score " + str(mariya_score))

    if mariya_score == 0:
        break


    counter = 1
    diceroll_sum = 0

    while counter <= 6:
        diceroll = randint(1, 6)
        
        diceroll_sum += diceroll
        
        counter += 1

    if ivan_score > 0:
        ivan_score -= diceroll_sum

    elif ivan_score < 0:
        ivan_score += diceroll_sum

    print("Ivan rolls " + str(diceroll_sum) + " and have score " + str(ivan_score))

    if ivan_score == 0:
        break

if mariya_score == 0:
    print("Mariya wins")
elif ivan_score == 0:
    print("Ivan wins")
