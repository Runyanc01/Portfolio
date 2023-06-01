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
    
    def enc_dec(message, key_shift, type):
        #take alphabet and reorder by the value of key_shift to the left
        key_alphabet = [alphabet[(letter - key_shift) % 26] for letter in range(len(alphabet))]
        #if type equals encrypt, run encrypt function
        if type == 'encrypt':
            encrypted_text = []
            for letter in message:
                if letter not in alphabet:
                    encrypted_text.append(letter)
                else:
                    letter_index = alphabet.index(letter)
                    encrypted_text.append(key_alphabet[letter_index])
            return encrypted_text
        #if type equals decrypt, run decrypt function
        elif type == 'decrypt':
            decrypted_text = []
            for letter in message:
                if letter not in alphabet:
                    decrypted_text.append(letter)
                else:
                    letter_index = key_alphabet.index(letter)
                    decrypted_text.append(alphabet[letter_index])
            return decrypted_text
        
    
    
    # Part 2: Modify functions to prompt user for the name of a text file containing the message to encrypt 
    #         and write encrypted message to text file (e.g. secret_enc.txt). Decryption reverses these steps
    #         and saves decrypted message to text file (e.g. secret_dec.txt).
    # Part 3: Consolidate encryption and decryption functions into one single function.


    # Add main program loop below. The logo and welcome message should be printed before the main menu loop starts 

    print(logo)
    print('Welcome to the Caesar cipher program!')
    print('')
    RUN = True
    
    while RUN == True:
        print('Main Menu')
        print('1 - Encode a message.' + '\n')
        print('2 - Decode a message.' + '\n')
        print('3 - Exit.' + '\n')
        
        user_choice = int(input("Enter the number corresponding to the desired menu option: "))
        
        if user_choice == 1:
            enc_fname = (input('\n' + 'Enter the name of the file containing the message: '))
            
            enc_shift = int(input('\n' + 'Type the shift number: '))

            typed = 'encrypt'
            try:
                enc_reader = open(enc_fname, 'r')
            except:
                print('File cannot be found')
                quit()
            
            enc_line_list = [] 
            for e_line in enc_reader.readlines():
                line_enc = enc_dec(e_line.lower(), enc_shift, typed)
                enc_line_list.append(''.join(line_enc))
            
            enc_message = ''.join(enc_line_list)
          
            name_check = enc_fname.split('_')
            
            if 'dec.txt' in name_check:
                enc_writer = open(f'{name_check[0]}_enc.txt', 'w')
                enc_writer.write(enc_message)   
                print(f'Encrypted message written to file: {name_check[0]}_enc.txt')
                enc_writer.close()
                
            elif 'enc.txt' in name_check:
                enc_writer = open(enc_fname, 'w')
                enc_writer.write(enc_message)   
                print(f'Encrypted message written to file: {enc_fname}')  
                enc_writer.close()
            
            else:
                enc_fhand = enc_fname.split('.')
                enc_writer = open(f'{enc_fhand[0]}_enc.txt', 'w')
                enc_writer.write(enc_message)
                print(f'Encrypted message written to file: {enc_fhand[0]}_enc.txt')
                enc_writer.close()

        elif user_choice == 2:
            dec_fname = (input('\n' + 'Enter the name of the file containing the message: '))
            dec_shift = int(input('\n' + 'Type the shift number: '))
            
            typed = 'decrypt'
            try:
                dec_reader = open(dec_fname, 'r')
                
            except:
                print('File cannot be found')
                quit() 
            
            dec_line_list = []
                
            for d_line in dec_reader.readlines():
                line_dec = enc_dec(d_line.lower(), dec_shift, typed)
                dec_line_list.append(''.join(line_dec))

            dec_message = ''.join(dec_line_list)
            
            name_check = dec_fname.split('_')

            if 'enc.txt' in name_check:
                dec_writer = open(f'{name_check[0]}_dec.txt', 'w')
                dec_writer.write(dec_message)
                print(f'Decrypted message written to file: {name_check[0]}_dec.txt')
                dec_writer.close()
                        
            elif 'dec.txt' in name_check:
                dec_writer = open(dec_fname, 'w')
                dec_writer.write(dec_message)
                print(f'Decrypted message written to file: {dec_fname}')
                dec_writer.close()
                
            else:
                dec_fhand = dec_fname.split('.')
                dec_writer = open(f'{dec_fhand[0]}_dec.txt', 'w')
                dec_writer.write(dec_message)   
                print(f'Decrypted message written to file: {dec_fhand[0]}_dec.txt')
                dec_writer.close()
            
        elif user_choice == 3:
            RUN = False
            print('\n' + 'Good Bye!')
        else:
            print('Please enter a valid menu option.')
        
# Do not make any changes to the code below
if __name__ == "__main__":
    main()


