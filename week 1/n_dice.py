# n_dice.py

from random import randint

sides = input("Enter sides: ")
sides = int(sides)
dice = randint(1, sides)
print("The dice rolled:")
print(dice)
