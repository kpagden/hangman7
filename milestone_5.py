import random

class Hangman:
    '''
    This class is used to represent a game of hangman.
    
    Attributes:
        word (str): the word to be guessed, picked randomly from the word_list.
        word_guessed (list): A list of the letters of the word, with _ for each letter not yet guessed.
        num_letters (int): The number of unique letters in the word that have not been guessed yet.
        num_lives (int): The number of lives the player has at the start of the game.
        word_list (list): A list of possible words to be guessed.
        list_of_guesses (list): A list of the guesses that have already been tried.
    '''
    def __init__(self, word_list, num_lives=5):
        '''
        See help(Hangman) for accurate signature
        '''
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        This function checks if the guess is in the word.
        
        Args:
            guess (str): the letter guessed by the player.
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
        
    def ask_for_input(self):
        '''
        This function asks the user to guess a letter.
        '''
        while True:
            print(self.word_guessed)
            guess = input('Enter a single letter: ')
            if not (len(guess) == 1 and guess.isalpha()):
                print('Invalid letter. Please enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    '''
    This function initiates the hangman game.
    
    Args:
        word_list (list): A list of possible words to be guessed.
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

play_game(word_list=['apple', 'apricot', 'avocado', 'banana', 'blackcurrant', 'cherry', 
                     'clementine', 'coconut', 'dragonfruit', 'grapes', 'kumquat', 'lemon', 
                     'lychee', 'mango', 'nectarine', 'papaya', 'passionfruit', 'pear', 'pineapple', 
                     'pomegranate', 'strawberry', 'watermelon'])