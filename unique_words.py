# This program reads a text file into a string variable
# The string is seperated into a list of all the words in the file
# Then the list of words is further reduced into a set
# The set contains each individual instance of a word as an item
# Punctuation is accounted for
# As a result "400horsepower" is an item in the set instead of "400-horsepower"
# Numbers are considered words such as 2000
# The use of the lower() method causes "i" to be an item rather than "I"
# The printed list is in a different order each time the program runs
# While loop to initiate examining file
# Try/except blocks to continue to program if the input is incorrect
# If/elif/else to validate input
# sys imported to close program at user's behest

import string
import sys

def main():

    # Initialize condition for validation loop
    condition = True
    # Validate input
    while condition == True:
        
        # Start to read a file or quit the program?
        input_answer = start_operation()
        
        try:
            chosen_answer = int(input_answer)
            if chosen_answer < 0:
                print('1)That is not either a 0 or 1. Please try again.')
            elif chosen_answer > 1:
                print('2)That is not either a 0 or 1. Please try again.')
            elif chosen_answer == 1:
                print('The program will close')
                sys.exit()
            else:
                try:
                    # Get user to input a file to operate on
                    input_file()
            
                except FileNotFoundError:
                    print('1)File was not found.')
                    # Rerun validation loop
                    condition = True
                except OSError:
                    print('2)File was not found.')
                    # Rerun validation loop
                    condition = True
        except ValueError:
            print('3)That is not either a 0 or 1. Please try again.')
            # Rerun validation loop
            condition = True

# Message describing how to continue program or close it
# Returns user's decision
def start_operation():
    print('Would you like to examine all the unique words in a file?')
    print('Please enter 0 for yes or 1 for no.')
    print('Entering 1 will also close the program.')
    user_answer = input('Enter 0 or 1: ')
    return user_answer

# Get file to read from input
# Then perform operations on the file
def input_file():
    user_file = input('Enter the name of the file you want to read:')
    print()
    name = user_file
    symbols = '`~!@#$%^&()_-{}[]|:;?><,+='
    if symbols not in name:

        # Collect unique words in a set
        unique_words = text_to_set(user_file)

        # Display unique words from a set
        print_set(unique_words)

# Format words read from file and add them to a set
def text_to_set(file):

    # Open the file and read its text
    file_to_read = open(file, 'r')
    
    # All of the text data is read from the file and the text becomes a string
    text = file_to_read.read()
                        
    # Using format_words function lowercase words and remove punctuation from text
    text_words = format_words(text)
    
    # Using the string method split, each word becomes a list item
    text_words = text_words.split()

    # The list is converted into a set containing one instance of each word
    unique_set = set(text_words)

    # Close the file
    file_to_read.close()

    return unique_set

# Make all letters in each word lowercase
# Delete punctuation from words read from a file
def format_words(text):

    # Initialize empty variable to write over
    formatted = ''
    # Cause all letters to be lowercase
    lower_text = text.lower()
    # Iterate over string 
    for x in lower_text:
        # If x is not in set of punctuation then add x to result
        if x not in string.punctuation:
            formatted += x
            
    return formatted

# Display the items in a set
def print_set(set_to_display):

    # Print the results using a for loop to iterate over set
    print('The following are the unique words from the text:')
    for item in set_to_display:
        print(item)
    print()

    

# Call main
main()
