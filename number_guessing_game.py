import random
from replit import clear
def attempting(attempts,target):
    if attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == target:
            print("You win!")
        elif guess < target:
            print("Too low!")
            attempting(attempts-1,target)
        elif guess > target:
            print("Too high!")
            attempting(attempts-1,target)
    else:
        print("You ran out of attempts. The answer was", target)
def num_guessing():
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type \'easy\' or \'hard\': ")
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    target = random.randint(1, 100)
    attempting(attempts,target)

again = True
while again:
    num_guessing()
    play = input("Do you want to play again? Type \'y\' or \'n\': ").lower
    if play == "n":
        again = False
    else:
        clear()