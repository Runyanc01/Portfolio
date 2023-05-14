#
# Name: Connor Runyan
# File: project1_lastname.py
# Date: 3/27/2023
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
#Connor Runyan
#
# Desc: Simulates a game of hangman
#


#import modules
import random

from hangman_art import stages, logo
from hangman_words import word_list


def main():

    # Define variables.
    lives = 6
    comp_word = random.choice(word_list)
    word_len = len(comp_word)
    guesses = []
    display = []
    word_letters = []
    
    #print logo
    print(logo)
    
    # Display solution with place-holders '-'
    for i in range(word_len):
        display.append('-')
     
    #create list of letters from random word   
    for i in range(word_len):
        letter = comp_word[i]
        word_letters.append(letter)
    
    
    
    
    # Game flags
    END_GAME = False
    
    # Game loop

    while not END_GAME:

        # Ask the user to guess a letter
        guess = input('Guess a letter: ').lower()
        
           
        
        # Check if the guess was entered before and add new guesses to list
        if guess in guesses:
            print('You already guessed this letter!')
            print(' '.join(display))
        else:
            guesses.append(guess)
            # Check if the letter guessed is one of the letters in the chosen word
            if guess in comp_word:
                for i in range(word_len):
                    if comp_word[i] == guess:
                        display[i] = guess
                if display != word_letters:
                    print(' '.join(display))      
          
            #if guess is not in word, print ASCII art and decrease lives
            else:
                print(f'You guessed {guess}, that\'s not in the word! You lose a life!')
                lives = lives - 1
                print(stages[lives])
                print(' '.join(display))
            
            #if all letters are displayed, print win statement
            if display == word_letters:
                print('You win!')
                print(' '.join(display))
                break
            
            
            #if lives are exhausted, hit game flag and print lose statement
            if lives == 0:
                END_GAME = True
                print('You Lose! You are out of attempts')
                print(f'The correct word was {comp_word}')

            

# Do not change the code below.
if __name__ == "__main__":
    print()    
    main()



























