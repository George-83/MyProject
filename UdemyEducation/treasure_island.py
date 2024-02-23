if __name__ == '__main__':
    # Treasure Island
    print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    cross_road_answer = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ").lower()
    if cross_road_answer == "left":
        lake_answer = input("You've reached a lake, but there is no boat. What is your action? Swim or wait? Type "
                            "\"swim\" or \"wait\" ").lower()
        if lake_answer == "wait":
            door_answer = input("Suddenly you see a boat coming to you. You are getting in it and swimming to the "
                                "island. \nYou've reached an island. There is an old house with 3 doors, red, "
                                "blue and yellow. Which one you want to go? Type \"red\", \"blue\" or \"yellow\" ").lower()
            if door_answer == "yellow":
                print("You are opening a yellow door and see a treasure chest. \nCongratulations you win!")
            elif door_answer == "red":
                print("You are coming into the red door. Suddenly door is closing. Something is wrong. It smells "
                      "strange. Oh no, it's a fire coming to you! You were burned by fire. Game Over.")
            elif door_answer == "blue":
                print("You are coming into the blue door. Suddenly the floor fell through and you find yourself "
                      "in a cage with terrible unknown beasts. You were eaten by beasts. Game Over.")
            else:
                print("Please chose correct answer. Game Over.")
        elif lake_answer == "swim":
            print("You are getting into the water, swimming to the island. But suddenly you feel that there is "
                  "something under the water. Oh no, this is a giant squid. You were attacked by squid. Game Over.")
        else:
            print("Please chose correct answer. Game Over.")
    elif cross_road_answer == "right":
        print("You are going 250 metres. Suddenly the ground collapses under your feet and you are falling into a "
              "hole. Game Over.")
    else:
        print("Please chose correct answer. Game Over.")
