import random

# Define the list of possible words
word_list = ['nectarine', 'pineapple', 'pear', 'strawberry', 'banana']

# Choose a random word from the list
word = random.choice(word_list)
# Print the word for testing purposes
print(word)

def check_guess(guess):
    guess = guess.lower()
    # Check whether the guess is in the word
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
    # Iteratively check if the input is a valid guess
    while True:
        guess = input('Enter a single letter: ')
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()