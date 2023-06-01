
#
# Name: Connor Runyan
# File: project1_lastname.py
# Date: 2/13/2023
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
#Connor Runyan
#
# Desc: Simulates a game of rock, paper, scissors
#
# Import any needed module(s) below this line
import random as rnd

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

# Write your code below this line and comment it accordingly (you may remove the comments provided for guidance below)
def main():
    
    #create list of choices
    choices = [rock, paper, scissors]
    
    # Print a welcome message
    print('Welcome to Rock, Paper, Scissors!')
    
    # Have the user enter a number corresponding to their choice (0 for Rock, 1 for Paper, and 2 for Scissors)
    user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. '))
    
    # print the corresponding hand signal
    print('User chose:')
    print(choices[user_choice])
    
    # Have the computer randomly make their pick (hint: review the lesson on randomization if needed.)
    print('Computer chose:')
    comp_choice = rnd.choice(choices)
    
    # print the corresponding hand signal
    print(comp_choice)
    
    # Compare the user's choice to the computer's choice and print who wins or if it a tie.
    if user_choice == comp_choice:
        print('Game is a Tie!')
    elif user_choice == 0 and comp_choice == choices[1]:
        print('You lose!')
    elif user_choice == 1 and comp_choice == choices[2]:
        print('You lose!')
    elif user_choice == 2 and comp_choice == choices[0]:
        print('You lose!')
    else:
        print('You win!')


# Don't forget the line below, otherwise main() will not be executed
main()
