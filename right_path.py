import random


# This defines the right path as a whole function
def Right_Path():
    playing = "1"
    scoreboard = 0
    while playing == "1":
        print("You have decided to take the Right Path.")
        print("\nThe way to your cabin is blocked by a massive tree on the path")
        player_choice = str(input("What would you choose to do; cut the tree, or turn back: ")).lower()
        while player_choice == "turn back":  # This is when the player chooses to turn back
            print("You have decided to go turn back")
            alternative1 = str(
                "You have been walking for hours in the thick forest and it seems like you are going no were"
                "\nYou then see a spot that seems familiar to you and realise "
                "that you have been walking in circles and that you are completely lost")
            alternative2 = str("You found your way back to the cabin and arrive there safely")
            alternative3 = str("You fell into a trap and died")
            alternative4 = str("You get attacked by a pack of wolves and die")
            alternatives = [alternative1, alternative2, alternative3, alternative4]
            print(random.choice(alternatives))  # Prints a random alternative

            while player_choice == "cut the tree":  # This shows the code when the player chooses to cut the tree
                print("This tree looks massive.... prepare for hard work")  # This is to set the setting and give a
                # visual
                tree_health = 10
                low_hit = 0
                medium_hit = 5
                high_hit = tree_health
                axe_hit = int(input("Enter 0,5 or 10: "))  # User enters a value to get an outcome
                if axe_hit == low_hit:  # if input is 0 then, the below outcome will be displayed
                    print("Your axe broke and you decided to go back,"
                          "however on the way back you fell into a ditch and starved to death")
                    print("You lost")
                elif axe_hit == medium_hit:  # if input is 5 then, the below outcome will be displayed
                    print("You cut the tree and walk towards your cabin, however a snake bites you and you die right"
                          "before you enter your cabin")
                    print("You lost")
                elif axe_hit == high_hit:  # if input is 10 then, the below outcome will be displayed
                    print("You cut the tree and find yourself walking towards a cabin, however its not yours."
                          "\nYou knock on the door and tell them what happen and they offer you to stay overnight"
                          "You find your cabin the next morning")
                    print("VICTORY!")
                break  # This stops the loop

            # This shows what will happen if the player does not choose an option from the ones provided at the start
            # of this definition
            else:
                print("You toke long to think what you wanted to do and a branch broke and fell into your head")
            scoreboard += 1
            playing = input("Do you want to try it again?[1=yes|0=No]: ")
            # This asks the player if they want to try again

            while playing not in ("0", "1"):
                # If the input is not between 0 and 1 then the following code will be shown
                playing = input("Try again... Do you want to play again?[1=yes|0=No]: ")

                # This will show how many times they attempted the left path
                print("You attempted the middle path", scoreboard, "time(s)!")
                print("The End")
            break
