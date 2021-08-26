import random  # This will bring the randomizer function within this code and it would be used later

import Left_Path  # Imports the Left_Path file
from Left_Path import *  # Imports everything from the Left_Path
import right_path  # Imports the Right_Path file
from right_path import *  # Imports everything from the Right_Path

# This is the introduction of the game
print("Hello, welcome to lumberjack game!"
      "\nIn this game you make your own choices and guide the character to the finish line while staying alive."
      "\nYou are a Lumberjack trying to find their cabin which is in the middle of a thick dangerous forest and"
      "\nyou have to navigate through the forest and get to your cabin alive.")


# This defines the lumberjack in order to be recognised when used at a later point.
def Lumberjack():
    disc = {}
    print("\nBefore we start, create your lumberjack")
    Name = input("What is the lumberjacks name: ")
    value1 = Name
    armor = input("What armor would you choose: ")
    value2 = armor
    axe = input("What axe would you choose: ")
    value3 = axe
    disc[Name] = value1
    disc[armor] = value2
    disc[axe] = value3
    print("You are named", Name, "you are wearing a", armor, "armor and have a", axe, "axe")
    print("\n\nYou just entered the dangerous forest and come across three paths;"
          "\nThe left path, middle path and right path")
    paths = ["Left Path", "Middle Path", "Right Path"]
    user_choice = int(input("\nWhich path will you be willing to take: (Left path= 0, Middle path= 1, Right path= 2: "))
    print("You have decided to take the", paths[user_choice])  # This display's to the user what path they chose
    return user_choice  # It sends the value of the function back to the caller


# This will define the middle path as a whole function
def Middle_Path():
    playing = "1"
    scoreboard = 0
    while playing == "1":
        print("You decided to go straight (Middle path)")
        alternative1 = str("You run into a creature that speaks in some unknown language and then you feel something..."
                           "\nsuddenly roots burst out from the ground and get attached to you and it seems that "
                           "you are starting to become a tree"
                           "\nYou are now one of the trees in the forest and spend the rest of your life as one")
        alternative2 = str("You walk and walk for hours and seems like you are lost"
                           "after a few hours or maybe days of walking you seem to see the end of the forest"
                           "\nand then you come out from the forest and come out into a city where you ask for help")
        alternative3 = str("You found your way back to the cabin and arrive there safely")
        alternative4 = str("You walk into a forest and see a strange object in the sky coming towards you"
                           "\nit seems that they are aliens and they are trying to kidnap you"
                           "\nyou don't remember anything after that but you know that "
                           "you have been taken by the aliens"
                           "\nthey have turned you into some type of deadly cyborg with a mission to destroy earth")
        alternative5 = str("You find a place that looks like paradise, "
                           "you decide to stay there forever")
        alternative6 = str("You come across some hunters that are armed to their teeth, "
                           "they ask you where are you going"
                           "\nYou tell them that you are in a quest to find you"
                           " cabin and they offer to help you find it"
                           "\nThey also asked you to join them for hunting and"
                           " you agree and spend a few hours with them hunting")
        alternatives = [alternative1, alternative2, alternative3, alternative4, alternative5, alternative6]
        # list of all 6 alternatives

        # This is the function in which randomises the alternatives from the above list
        print(random.choice(alternatives))
        scoreboard += 1
        playing = input("Do you want to try this path again?[1=yes|0=No]: ")  # This asks the player if they want to
        # try again

        while playing not in ("0", "1"):  # If the input is not between 0 and 1 then the following code will be shown
            playing = input("Input error...please try again... Do you want to try it again?[1=yes|0=No]: ")

        # This will show how many times they attempted the middle path
        print("You have attempted the middle path", scoreboard, "time(s)!")
        print("The End!")


# This while loop acts repeats the coding again for another attempt
while True:
    choice = Lumberjack()
    if choice == 0:
        Left_Path()
    if choice == 1:
        Middle_Path()
    if choice == 2:
        Right_Path()
    disc = {'Name': 'Name', 'axe': 'axe', 'armor': 'armor'}
    break  # This ends the loop from repeating when the player ends it
