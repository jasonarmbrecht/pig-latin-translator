#  Course:         ICTPRG302 - Apply introductory programming techniques
#  Assessment:     3
#  Application:    Pig Latin Translator
#  Created by:     Jason Armbrecht (Junior Programmer, Skillage IT)
#  Contact:        jason.armbrecht@gmail.com
#  Date created:   14-NOV-2022 (Last updated 27-FEB-2023)
#  Development:    https://github.com/jasonarmbrecht/pig-latin-translator/
#  Requirements:   Create and test a python program which takes a word or phrase, converts it to Pig Latin and displays the output.
#  Note:           This program will create a text file in the same folder that the program is located. It is to store translation history.


# Import the sys module to use the exit() function.
import sys

# Import Path from pathlib module in order to use path function for file read and write.
from pathlib import Path

# Define variable for file path to translation history stored in text file (history.txt).
file_path = Path(__file__).with_name('history.txt')

# Function to open or create a file and write the new translation to history.txt.
def file_write():
    file_path.open('a+').write(" ".join(new_word_list) + "\n")
    file_path.open('a+').close()

# Function to read the translation history text file and retieve and print the last 3 translations from history.txt.
def file_read():
    for line in reversed(list(file_path.open('rt').readlines() [-3:])):
        print(line.rstrip())
        file_path.open('rt').close()

# Function to handle the translation.
def pig_latin(word):
    # Define the vowels into a variable. Capitals are also defined just incase the word(s) are capitalised.
    vowels = "aeiouAEIOU"
    if word[0] not in vowels and word[1] in vowels:
        # If word starts with a consonant and a vowel, move first letter to the end and add "ay".
        return word[1:] + word[0] + "ay"
    elif word[0] not in vowels and word[1] not in vowels:
        # If word starts with two consonants, move the first two letters to tne end of the word and add "ay".
        return word[2:] + word[0:2] + "ay"
    else:
        # If word starts with a vowel, just add "way" to the end of the word.
        return word + "way"

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
        if len(user_input.split()) > 1:
            for word in user_input.split():
                new_word_list.append(pig_latin(word).lower())
        else:
            new_word_list.append(pig_latin(user_input).lower())


        # Print the final translation, record to history.txt and allow the user to press the ENTER key to go back to the user input stage.
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
