
# Name: Connor Runyan
# File: runyan_assignment2.py
# Date: Due date
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Connor Runyan
# Desc: Randomly generates a password based on user-specified numbers of letters, symbols, and numbers.
#

# Add header block and honor code pledge above this line
# Import any needed module(s) below this line
import random as rnd

def main():
    # Define lists of letter, symbols, and numbers
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Display main menu and prompt user for number of letters, symbols, and numbers
    print("Welcome to the WittPy Password Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    #define function to randomly select characters from there respective lists
    def select_characters(given_list, num_chars, resulting_list):
        for i in range(num_chars):
            i = rnd.choice(given_list)
            resulting_list.append(i)
            
        return resulting_list
        

    #invoke function to add random characters to password_list
    password_list = []
    select_characters(letters, nr_letters, password_list)
    select_characters(symbols, nr_symbols, password_list)
    select_characters(numbers, nr_numbers, password_list)


    #define new function to shuffle list without random module
    def mix(char_list):
        
        for i in range(len(char_list)):
            x = char_list.index(char_list[i])
            if x in letters:
                for z in range(len(char_list)):
                    y = char_list.pop(i)
                    #use key = list to keep char_list type and not None type
                    char_list.sort(key = list)
                    char_list.insert(z , y)
            elif x in numbers:
                for z in range(len(char_list)):
                    y = char_list.pop(i)
                    char_list.reverse()
                    char_list.insert(z, y)
            else:
                for z in range(len(char_list)):
                    y = char_list.pop(i)
                    char_list.reverse()
                    char_list.insert(z, y)
            return char_list
    
    #pop random indices in password_list, and append them into new shuffled list
    generated_password = ""
    '''for i in range(len(password_list)):
        x = password_list.pop(rnd.randint(0, (len(password_list)- 1)))
        password_list.append(x)'''
    
    password_list = mix(password_list)
    
    for i in range(len(password_list)):
        generated_password = password_list[i] + generated_password

    # Display password list and generated password

    print(f"Generated password: {generated_password}")

main()