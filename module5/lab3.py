import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == 'y':
        dice = random.randint(1, 6)
        print("Dice rolled:", dice)
    elif choice == 'n':
        print("Exiting simulator.")
        break
    else:
        print("Invalid input! Enter y or n.")