inventory = []

def intro():
    print("\nWelcome to 'Choose Your Path' Adventure!")
    print("You're standing at a crossroads in a mysterious forest.")
    print("You see a path leading left and another leading right.")
    choice = input("Which path do you choose? (left/right): ").strip().lower()
    if choice == "left":
        path_left()
    elif choice == "right":
        path_right()
    else:
        print("Please choose 'left' or 'right'.")
        intro()

def path_left():
    print("\nYou walk along the left path and find a shiny sword stuck in a rock.")
    choice = input("Do you take the sword? (yes/no): ").strip().lower()
    if choice == "yes":
        inventory.append("sword")
        print("You now have a sword!")
    else:
        print("You leave the sword behind.")
    print("You keep walking and reach a cave.")
    cave()

def path_right():
    print("\nThe right path leads to a peaceful lake.")
    print("You find a glowing potion on the ground.")
    choice = input("Do you pick up the potion? (yes/no): ").strip().lower()
    if choice == "yes":
        inventory.append("potion")
        print("You now have a potion!")
    else:
        print("You leave the potion behind.")
    print("You cross a bridge and reach a cave.")
    cave()

def cave():
    print("\nInside the cave, a dragon appears!")
    if "sword" in inventory:
        print("You draw your sword and bravely face the dragon!")
        print("After an epic battle, you defeat the dragon and escape with treasure!")
        ending(True)
    elif "potion" in inventory:
        print("You throw the potion, and it magically puts the dragon to sleep!")
        print("You quietly sneak past and escape with treasure!")
        ending(True)
    else:
        print("You have nothing to defend yourself with.")
        print("The dragon sees you and... well, you don’t make it.")
        ending(False)

def ending(won):
    if won:
        print("\n🏆 You Win! You escaped the cave with treasure!")
    else:
        print("\n💀 Game Over. Better luck next time!")
    replay = input("Play again? (yes/no): ").strip().lower()
    if replay == "yes":
        inventory.clear()
        intro()
    else:
        print("Thanks for playing!")

intro()