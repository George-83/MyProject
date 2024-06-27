import random
import sys

if __name__ == '__main__':
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    game_list = [rock, paper, scissors]
    user_choice_str = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ")
    user_choice = int(user_choice_str)
    if user_choice < 0 or user_choice >= 3:
        print("Incorrect value has been entered. Please restart and enter correct value: 0, 1 or 2")
        sys.exit(1)
    print("\n Your choice is:\n" + game_list[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer choice is:")
    print(game_list[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose! Game over.")
    elif computer_choice > user_choice:
        print("You lose! Game over.")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw.")


