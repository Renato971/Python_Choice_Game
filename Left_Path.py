from typing import List


# This defines the left path as a whole function
def Left_Path():
    playing = "1"
    scoreboard = 0
    while playing == "1":
        print("You have decided to take the Left Path")
        print("\nYou encountered a bear cave in which you have entered; there is a bear which is sleeping and hears"
              "you as you stepped into a branch.")
        bear_hits = 5
        print("The bear is charging at you....")
        print("\nThink fast...")
        pick = str(input("What would you choose to fight the bear: Axe, or Fists?: ")).lower()  # .lower() is used so
        # that it replaces the input to lower characters

        # it display's the input of the user in small cased letters
        if pick == 'axe':
            axe_hit = int(input("How many times will you swing at the bear (1-5): "))
            if axe_hit >= 4 <= bear_hits:  # axe outcome
                print("You win the battle by killing the bear and find your way into the cabin")
                print("VICTORY!")
            elif axe_hit >= 1 <= 3 != bear_hits:  # axe second outcome
                print("You missed the bear and fell into your axe")
                print("You are dead!")
            else:
                print("Error, unknown value entered.... please follow instructions")  # If player enters other value
        elif pick == 'fists':  # fists outcome
            print("You tried to find a bear with your fists..... You're dead")
        else:  # input blank outcome
            print("You had trouble deciding what to choose and the bear killed you")
            print("You lost")
        scoreboard += 1
        playing = input("Do You want to play this path again?[1=yes|0=No]: ")  # This asks
        # the player if they want to try again

        while playing not in ("0", "1"):  # If the input is not between 0 and 1 then the following code will be shown
            playing = input("Input error...please try again... Do you want to try it again?[1=yes|0=No]: ")

    # This will show how many times they attempted the left path
    print("You attempted the left path", scoreboard, "time(s)!")

    times_played = []  # This is an empty list in which will be used below
    times_played.append(scoreboard)  # It will add the scoreboard to the above list
    print(times_played)  # It will print the scoreboard at the end
    print("The End")
