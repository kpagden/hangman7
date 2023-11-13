import random

# Define the list of possible words
word_list = ['Nectarine', 'Pineapple', 'Pear', 'Strawberry', 'Banana']
print(word_list)

# Choose a random word from the list
word = random.choice(word_list)
print(word)

# Ask the user for an input
guess = input('Enter a single letter: ')

# Check that the input is a single character
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print("Oops! That is not a valid input.")