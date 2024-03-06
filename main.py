"""
Engeto Online Python Akademie: Projekt2 - Bulls & Cows
author: Andrea Kvapilová
email: a.ndrea@centrum.cz
discord: andreakvapilova
"""

import game_logic
import game_graphics
import time

#global variable
separator = 40 * "-"
number_digits = 4

#visualization of regard and text
print(game_graphics.welcome_print)
regard = "Hi there!"
text = f"I've generated a random {number_digits} number for you.\nLet's play a bull and cows game."
print(f"{regard}\n{separator}\n{text}")

#generate random number
generated_number = game_logic.random_number_generation(number_digits)

#input and game evaluation
checking_entered_number = False
guessed_number = False
number_of_guessed = 0
start_time = time.time() #start of time counting 
while checking_entered_number is False or guessed_number is False:
    enter_number = input(f"{separator}\nEnter a number:\n{separator}\n")
    checking_entered_number = game_logic.checking_players_number(enter_number, number_digits)
    if checking_entered_number is True:
        guessed_number = game_logic.checking_bulls_and_cows(enter_number, generated_number)
        number_of_guessed += 1
        if guessed_number is True:
            guessed_time = (time.time() - start_time) #evaluation of guessing time
            guess = "guesses" if number_of_guessed != 1 else "guess" #condition to determine singular and plural nouns
            time = f"{guessed_time:.2f} seconds" if guessed_time < 60 else f"{(guessed_time/60):.2f} minutes" #condition to determine seconds or minutes
            print(f"Correct, you've guessed the right number\
                  \nin {number_of_guessed} {guess} and in {time}!\n{separator}")
            print(game_graphics.end_print)
            quit()

