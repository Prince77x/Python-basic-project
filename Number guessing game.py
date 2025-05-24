# Number Guessing Game
# import random
from random import randint

# def a function to check the difficulty level hard or easy
def difficulty_level():
    level = input('choose a difficulty level. Type "easy or hard": ').lower()
    if level =="easy":
        return 10
    else:
        return 5

'''
# def function to check the answer and guess
def check_answer(guess, answer):
    if guess > answer:
        return 'Too high ! try smaller number'
    elif guess <answer:
        return 'Too low ! try larger number'
    else:
        return f"congratulations! you guessed the number {answer} correctly."
'''
# def play_game():
def play_game():
    # print welcoming statement
    print('welcome to the number guessing game!')
    print('I am thinking of a number between 1 and 100.')
    print('you have to guess the number in limited attempts. Chellenge yourself!')
    answer = randint(1,100)  # answer is a random number between 1 and 100
    attempts = difficulty_level()  # get the difficulty level and number of attempts
    print(f"you have {attempts} attempts left to guess the number.")

    while attempts > 0:
        # take integer input from player and assingn it as guess
        guess = int(input("Make a guess: "))

        if guess > answer:
            print('Too high ! try smaller number')
        elif guess <answer:
            print('Too low ! try larger number')
        else:
            print(f"congratulations! you guessed the number {answer} correctly.")
        
        attempts -=1
        if attempts == 0:
            print(f"you have insufficient attempts. The number was {answer}.")
        else:
            print(f'you have {attempts} attempts left to guess the number.')
            print('Guess again!')
        
        
        
if __name__ == "__main__":
    play_game()
        

        
        




