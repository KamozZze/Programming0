# n_dice_more.py

from random import randint

sides = input("Enter sides: ")
sides = int(sides)
dice1 = randint(1, sides)
dice2 = randint(1, sides)
print("First roll:")
print(dice1)

print("Second roll:")
print(dice2)

print("Sum is:")
print(dice1 + dice2)
