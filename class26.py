"""Tic Tac Toe Game
Outline:
Write a Python Program to create a Tic Tac Toe game.
You can use different modules and functions to create this game.
Make sure that you print the board after every move."""
''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''
theboard={'7':' ','8':' ','9':' ',
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' ' }
Board_keys=[]
for i in theboard:
    Board_keys.append(i)
''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''
def printboard(board):
    print(board['7']+' | '+board['8']+' | '+board['9'])
    print('- + - + -')
    print(board['4']+' | '+board['5']+' | '+board['6'])
    print('- + - + -')
    print(board['1']+' | '+board['2']+' | '+board['3'])
def the_game():
    turn='X'
    count=0
    for i in range(10):
        printboard(theboard)
        print("It's your turn, "+turn+ " Where do you want to move to")
        move=input()
        if theboard[move]==' ':
            theboard[move]=turn
            count=count+1
        else:
            print("That place is already filled.\nWhich place do you want to move to?")
            continue
# Now we will check if player X or O has won,for every move after 5 moves.
        if count>=5:
            if theboard['7']==theboard['8']==theboard['9'] !=' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** "+turn + " won. ****")
            elif theboard['4']==theboard['5']==theboard['6'] !=' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** "+turn + " won. ****")
            elif theboard['1']==theboard['2']==theboard['3'] !=' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** "+turn + " won. ****")
            elif theboard['1']==theboard['4']==theboard['7'] !=' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** "+turn + " won. ****")
            elif theboard['2']==theboard['5']==theboard['8'] !=' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** "+turn + " won. ****")
            elif theboard['3']==theboard['6']==theboard['9'] !=' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** "+turn + " won. ****")
            elif theboard['7']==theboard['5']==theboard['3'] !=' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** "+turn + " won. ****")
            elif theboard['1']==theboard['5']==theboard['9'] !=' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** "+turn + " won. ****")
            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count==9:
                print("\nGame Over.\n")                
                print("It's a Tie!")
        # Now we have to change the player after every move.
        if turn=='X':
            turn='O'
        else:
            turn='X'
    # Now we will ask if player wants to restart the game or not.
    restart=input("Do want to play again?(y/n)")
    if restart=='y' or restart=='Y':
        for key in Board_keys:
            theboard[key]=" "
        the_game()
if __name__ == "__main__":
    the_game()

        
"""Guess the Number Game
Outline:
Write a Python Program to create a Guess the number game.
You can use different modules and functions to create this game.
Every time the user guesses wrong, drop a hint. You can drop additional hints as well.
import random
def number_guess_game():
    attempts=0
    print("Welcome to the very hard number guessing game")
    randome=random.randint(1,200)
    choies=int(input("Choose a number between 1 and 200: "))
    if choies<randome:
        print("Too low")
        attempts=attempts+1
    elif choies==randome:
        print("You got the right answer")
        attempts=attempts+1
        print("It took",attempts,"attempts to guess the number")
        number_guess_game()
    elif choies>randome:
        print("Too high")
        attempts=attempts+1
    while True:
        choies=int(input("Choose a number between 1 and 200: "))
        if choies<randome:
            print("Too low")
            attempts=attempts+1
        elif choies==randome:
            print("You got the right answer")
            attempts=attempts+1
            print("It took",attempts,"attempts to guess the number")
            number_guess_game()
        elif choies>randome:
            print("Too high")
            attempts=attempts+1
number_guess_game()"""