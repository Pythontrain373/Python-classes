"""Number game
Outline:
Write a program to generate a random integer and match it with the input given by the user?"""
"""import random
def number_guess_game():
    print("Welcome to the very hard number guessing game")
    randome=random.randint(1,100)
    choies=int(input("Choose a number between 1 and 100: "))
    if choies<randome:
        print("Too low")
    elif choies==randome:
        print("You got the right answer")
        number_guess_game()
    elif choies>randome:
        print("Too high")
    while True:
        choies=int(input("Choose a number between 1 and 100: "))
        if choies<randome:
            print("Too low")
        elif choies==randome:
            print("You got the right answer")
            number_guess_game()
        elif choies>randome:
            print("Too high")
number_guess_game()
import random
playing=True
number=random.randint(10,20)
while playing:
    guess=int(input("Give me your best guess: "))
    if number==guess:
        print("You won")
        print("The number was",number)
        break
    else:
        print("Your guess isnt right try again")
Rock paper scissors
Outline:
Create a program to play rock, paper, and scissors.
Use a random module to select from the given options Check whether the random guess matches the users answer
import random
playing=True
options=["Rock","Paper","Scissors"]
while playing:
    guess=input("what is your guess: ")
    computor=random.choice(options)
    print("Your choice=",guess,"\nComputor choice=",computor)
    if guess==computor:
        print("It is a tie")
    elif guess=="Rock" and computor=="Scissors":
        print("You win")
    elif guess=="Paper" and computor=="Rock":
        print("You win")
    elif guess==("Scissors") and computor=="Paper":
        print("You win")
    else:
        print("You lose")

Mathematical operations
Outline:
Write a program to understand the different functions of the math module.

import math
print(math.sqrt(25))
print(math.pow(2,2))
print(math.factorial(5))
print(math.sin(45))
print(math.ceil(4.3))
print(math.floor(4.3))
print(math.fabs(-7))
print(math.pi)
print(math.e)"""