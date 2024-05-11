rock='''
    _____
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
     _____
---'    ___)___
           ______)
          _______)
         _______)
---.__________)
'''

scissors='''
    _____
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
'''
import random
tools = [rock, paper, scissors]
user_choice = int(input("Enter the number (0 for rock, 1 for paper, 2 for scissors)  :"))
system_choice = random.randint(0,2)

if user_choice >= 3 or user_choice < 0:
    print("Please enter the valid number!")
    user_choice = int(input("Enter the number (0 for rock, 1 for paper, 2 for scissors)  :"))
else:
    print("Your choice is ")
    print(tools[user_choice])
    print("System choice is ")
    print(tools[system_choice])

    if user_choice == 0 and system_choice == 1:
        print("System wins the game!")
    elif user_choice == 1 and system_choice == 0:
        print("You win the game!")
    elif user_choice == 0 and system_choice == 2:
        print('You win the game!')
    elif user_choice == 2 and system_choice == 0:
        print("Syetem wins the game!")
    elif user_choice == 1 and system_choice == 2:
        print("System wins the game!")
    elif user_choice == 2 and system_choice == 1:
        print("You win the game!")
    else:
        print("Draw")
