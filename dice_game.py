# dice_game.py

from random import randint

sides = input("Enter dice sides: ")
sides = int(sides)

player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")

player1_diceroll = randint(1, sides)
player2_diceroll = randint(1, sides)


print(player1 + " rolls " + str(player1_diceroll))
print(player2 + " rolls " + str(player2_diceroll))

if player1_diceroll == player2_diceroll:
    print("Tie")

elif player1_diceroll > player2_diceroll:
    print(player1 + " " + "wins!")

elif player1_diceroll < player2_diceroll:
    print(player2 + " " + "wins!")
