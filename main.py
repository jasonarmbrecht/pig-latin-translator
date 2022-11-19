#  Course:         ICTPRG302 - Apply introductory programming techniques
#  Assessment:     3
#  Application:    Pig Latin Translator
#  Created by:     Jason Armbrecht (Junior Programmer, Skillage IT)
#  Contact:        jason.armbrecht@gmail.com
#  Date created:   14-NOV-2022

#  Requirements:   Create and test a python program which takes a word or phrase, converts it to Pig Latin and displays the output.


# Import the sys module to use the exit() function.
import sys

# Import Path from pathlib module in order to use path function for file read and write.
from pathlib import Path

# Define variables for vowels (in a list) and the 'ay' and 'way' sounds.
vowels = ("a","e","i","o","u")
pyg1 = "ay"
pyg2 = "way"

# Define variable for file path to translation history stored in text file.
file_path = Path(__file__).with_name('history.txt')

# Function to open or create a file and write the translation to the new word list.
def file_write():
    file_path.open('a+').write(" ".join(new_word_list) + "\n")
    file_path.open('a+').close()

# Function to read the translation history text file and retieve and print the last 3 translations.
def file_read():
    for line in reversed(list(file_path.open('rt').readlines() [-3:])):
        print(line.rstrip())
        file_path.open('rt').close()

# Start of the main program inside a while loop which conducts basic validation on input and if the user requests to exit the program or view translation history.
while True: 
    
    # Create a blank list everytime the while loop starts again.
    new_word_list = []     
    
    # Simple 'for loop' to create 10 lines of black space to declutter the command line interface.
    for _ in range(10):
        print("\n")
    
    # Print the program title and instructions.
    print("-------------------------------------------------")
    print('\x1b[1;34;40m' + "Welcome to the Pig Latin Translator application." + '\x1b[0m')
    print('\x1b[0;34;40m' + "Enter a word or phrase to translate." + '\x1b[0m')
    print('\x1b[0;34;40m' + "You can also type " + '\x1b[5;30;42m' + "!history" + '\x1b[0;34;40m' + " to display previous translations." + '\x1b[0m')
    print('\x1b[0;34;40m' + "Otherwise, type " + '\x1b[5;30;43m' + "!exit" + '\x1b[0;34;40m' + " to stop the app." + '\x1b[0m')
    print("-------------------------------------------------")
    print("\n")
    
    # Ask for user input and record into a variable.
    print('\x1b[1;37;44m' + "Enter a word, phrase or !command:" + '\x1b[0m', end=" ")
    user_input = input()
    
    # If the user types '!exit', the program will exit.
    if user_input == '!exit':
        print("\n")
        print('\x1b[5;30;43m' + "You have stopped the application. Goodbye." + '\x1b[0m')
        sys.exit()

    # If user types '!history', the program will display the last 3 translations from the history text file, using the file_read function.
    elif user_input == '!history':
        print("\n")
        print('\x1b[0;34;40m' + "Last 3 translations: " + '\x1b[0m')
        print("-----------------------")
        file_read()
        print("\n")
        print('\x1b[5;30;42m' + "Press ENTER to continue..." + '\x1b[0m', end="")
        input()

    # If the user input is not blank, contains no numbers or special characters then continue with code execution, 
    # otherwise go to the very last 'else' statement.
    elif user_input != '' and user_input.replace(" ","").isalpha():
        
        # If the user input is a phrase with multiple words then split the words and check if the first character of each is a vowel.
        # If so, create a new word by adding "way" to the end of the original word. 
        if len(user_input.split()) > 1: 
            for word in user_input.split(): 
                if word.startswith(vowels): 
                    new_word = word.lower() + pyg2
                
                # If the phrase with multiple words contains a word which does not start with a vowel, move the first character
                # to the end of the word and append "ay" to the end.
                else:
                    first_letter = word[0]
                    new_word = word.lower() + first_letter + pyg1
                    new_word = new_word[1:]
                
                # Save each word modified in the above 'for loop' to the new word list.
                new_word_list.append(new_word.lower())
        
        # If the user input was a single word, move the first character to the end of the word and append "ay" to the end.
        else:
            first_letter = user_input[0] 
            new_word = user_input.lower() + first_letter + pyg1 
            new_word = new_word[1:] 
            new_word_list.append(new_word.lower())
        
        # Print the final translation and allow the user to press the ENTER key to go back to the user input stage.
        print("\n")
        print("**********************")
        print('\x1b[0;34;40m' + "Pig Latin translation: " + '\x1b[1;37;40m'," ".join(new_word_list) + " " + '\x1b[0m')
        print("**********************")
        print("\n")
        print('\x1b[5;30;42m' + "Press ENTER to continue..." + '\x1b[0m', end="")
        file_write()
        input()
    
    # If the user input contained numbers or special characters, print an explanation of why the input was invalid 
    # and stop the program.
    else:
        print("\n")
        print('\x1b[1;37;41m' + "Input invalid, do not use special characters such as !, @, # or . (full stop)" + '\x1b[0m')
        break 
