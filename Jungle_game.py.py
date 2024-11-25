def jungle_adventure():
    print("Welcome to the Jungle Adventure!")

    # First choice
    choice1 = int(input("Press 1 to go left, 2 to go right: "))

    # Second choice
    choice2 = int(input("Press 1 to go left, 2 to go right: "))

    # River encounter
    print("A raging river blocks your path.")
    river_choice = int(input("Press 1 to cross the river, 2 to turn back: "))

    if river_choice == 1:
        # Person encounter
        print("A friendly stranger offers to help you cross the river.")
        help_choice = int(input("Press 1 to accept help, 2 to decline: "))

        if help_choice == 1:
            print("You accept the stranger's help and cross the river safely. You win!")
        else:
            print("You try to cross the river alone but fail. Game Over!")
    else:
        print("You turn back. Game Over!")

jungle_adventure()