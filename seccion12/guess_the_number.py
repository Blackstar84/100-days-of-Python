from random import randint
from art import logo
import os

EASY = 10
HARD = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it, The answer was {answer}")

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)

    level = input("Choose a difficulty. Type 'ease' or 'hard': ")
    if level  == "easy":
        turns = EASY
    else: 
        turns = HARD

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))     

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")              

while input("Do you want to play the game? Type 'y' or 'n': ") == "y":
  os.system('cls')
  play_game()

#play_game()    