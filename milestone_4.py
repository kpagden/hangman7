import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        # Check whether the guess is in the word
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for letter in self.word:
                if letter == guess:
                    for i in range(len(self.word)):
                        if self.word[i] == guess:
                            self.word_guessed[i] = guess
            self.num_letters -= 1
            # Testing the game
            print(self.word_guessed)
            print(self.num_letters)
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
        
    def ask_for_input(self):
        # Iteratively check if the input is a valid guess
        while True:
            guess = input('Enter a single letter: ')
            if not (len(guess) == 1 and guess.isalpha()):
                print('Invalid letter. Please enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

# Testing the game
hangman_1 = Hangman(word_list=['nectarine', 'pineapple', 'pear', 'strawberry', 'banana'])
print(hangman_1.word)
print(hangman_1.word_guessed)
print(hangman_1.num_letters)
hangman_1.ask_for_input()
