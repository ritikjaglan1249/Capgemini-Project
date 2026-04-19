# Dice Roll Game (Python)
import random

print("Name: Ritik Jaglan")
print("Dice Game (2 Players)")

player = 1   # start with player 1

while True:
    print(f"\nPlayer {player} turn")

    input("Press Enter to roll dice...")

    dice = random.randint(1, 6)
    print("You got:", dice)

    # Rule: if 6 → same player again
    if dice == 6:
        print("You got 6! Play again 🎉")
    else:
        # change player
        if player == 1:
            player = 2
        else:
            player = 1

    # ask to continue
    while True:
        choice = input("Continue game? (y/n): ").lower()

        if choice == 'y':
            break
        elif choice == 'n':
            print("Game Over")
            exit()
        else:
            print("Enter only y or n")