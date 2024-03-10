#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from Easy.GuessGame.art import logo
import random
import os

clear = lambda:os.system('clear') #clears out the console for the game

def game():
    generated_random_number = random.randint(1, 100)
    game_difficulty_mode = input('Please select a difficulty mode for the game: ("e" for easy) and ("h" for hard).\n')
    amount_of_guess = 0

    if game_difficulty_mode.lower() == 'e':
        print('You have chosen easy mode, you have 10 guess.')
        amount_of_guess = 10
    elif game_difficulty_mode.lower() == 'h':
        print('You have chosen easy mode, you have 5 guess.')
        amount_of_guess = 5
    else:
        print('you have entered the wrong letter, defaulting to easy mode. You will be given 10 turns.')
        amount_of_guess = 10

    while amount_of_guess > 0:
        guessed_number = int(input('enter a number from 1 - 100 to guess for the secret number: '))

        if guessed_number > generated_random_number:
            print('Too High')
            amount_of_guess -= 1
            print(f'You have {amount_of_guess} guess left.')
        elif guessed_number < generated_random_number:
            print('Too Low')
            amount_of_guess -= 1
            print(f'You have {amount_of_guess} guess left.')
        else:
            print('You guessed correctly!')
            break
    
    if amount_of_guess == 0:
        print(f'You ran out of guesses! The correct number is {guessed_number}')
    
    keep_playing = input('Do you want to keep playing? (y for yes) and (n for no).').lower()

    if keep_playing == 'y':
        clear()
        game()
    else:
        clear()
        print('Thank you for playing.')

print(logo)
game()