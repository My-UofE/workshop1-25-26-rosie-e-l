import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)
    poss_values.remove(x)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if ((next_val > current_val) and (user_input == 'h')) or ((next_val < current_val) and (user_input == 'l')):
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    if letter in word:
        #update entries in board to enter correctly guessed letter
        startpos = 0
        for i in range(startpos, len(board)-1):
            if word[i] == letter:
                board[i] = letter
            startpos += 1
        #if letter can be found, function should print:
        print("Well done! '{}' is in the word".format(letter))
        return True
        
    else:
        print("Sorry, '{}' is not in the word".format(letter))
        return False
