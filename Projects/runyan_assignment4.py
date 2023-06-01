#
# Name: Connor Runyan
# File: project1_lastname.py
# Date: 4/10/2023
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
#Connor Runyan
#
# Desc: Runs a Caesar Cipher on input messages and files
#

# Add header block and honor pledge above this line.

"""Encrypt or decrypt a message using Caesar cipher for a given shift amount."""

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def main():
    # Plain alphabet used by the program
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Part 1: Define functions for encryption/decryption below this line
    
    def encrypt(message, key_shift):

        #take alphabet and reorder by the value of key_shift to the left
        key_alphabet = [alphabet[(letter - key_shift) % 26] for letter in range(len(alphabet))]
        
        encrypted_text = []
        for letter in message:
            #if the character 'letter' is not in the alphabet, just add it to the list
            if letter not in alphabet:
                encrypted_text.append(letter)
            #replace 'letter' with the letter at the index of 'letter' from key alphabet
            else:
                letter_index = alphabet.index(letter)
                encrypted_text.append(key_alphabet[letter_index])
        return encrypted_text
        
    def decrypt(message, key_shift):
        #take alphabet and reorder by the value of key_shift to the left
        key_alphabet = [alphabet[(letter - key_shift) % 26] for letter in range(len(alphabet))]
        
        decrypted_text = []
        for letter in message:
            #if the character 'letter' is not in the alphabet, just add it to the list
            if letter not in alphabet:
                decrypted_text.append(letter)
            #replace 'letter' with the letter at the index of 'letter' from regular alphabet
            else:
                letter_index = key_alphabet.index(letter)
                decrypted_text.append(alphabet[letter_index])
        return decrypted_text


    # print logo and welcome

    print(logo)
    print('Welcome to the Caesar cipher program!')
    print('')
    RUN = True
    
    #while user_choice is not 3, print main menu and run program
    while RUN == True:
        print('Main Menu')
        print('1 - Encode a message.' + '\n')
        print('2 - Decode a message.' + '\n')
        print('3 - Exit.' + '\n')
        
        user_choice = int(input("Enter the number corresponding to the desired menu option: "))
        
        #invoke encrypt function and print result
        if user_choice == 1:
            user_message = (input('\n' + 'Type your message: ')).lower()
            shift = int(input('\n' + 'Type the shift number: '))
            enc_message = encrypt(user_message, shift)
            print('\n' + 'The encoded text is: ' + ''.join(enc_message))
        
        #invoke decrypt function and print result
        elif user_choice == 2:
            user_message = (input('\n' + 'Type your message: ')).lower()
            shift = int(input('\n' + 'Type the shift number: '))
            dec_message = decrypt(user_message, shift)
            print('\n' + 'The decoded text is: ' + ''.join(dec_message))

        #if user_choice equals 3, then flag RUN is false, and the loop stops and prints 'good bye'  
        elif user_choice == 3:
            RUN = False
            print('\n' + 'Good Bye!')

        #handles if user_choice is not 1, 2, or 3
        else:
            print('Please enter a valid menu option.')
        
# Do not make any changes to the code below
if __name__ == "__main__":
    main()















