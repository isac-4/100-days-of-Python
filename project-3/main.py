print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad. Do you want to go? Type "left" or "right"? ').lower()

if choice1 == "left":

    choice2 = input('You\'ve come to a lake. There is an Island in the middle of the lake. Type "wait" if you want to wait for a boat. Type "swim" to swim across?').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is a house with three doors. One red, one yellow, and one blue. Which color do you choose? ').lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
         print("You got attacked by a trout. Game Over.")
else:
        print("You fell into the Hole! Game Over.")