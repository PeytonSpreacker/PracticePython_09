import random

def introduction():
# introduces the game and the rules
    print('Welcome to my Guessing Game!\n',
          'The CPU will generate a number between 1 and 9 and ask you for a guess\n',
          'Then it will let you know if you are spot on, too high, or too low.\n')
    command = input('Ready to start? y/n ')
    if command == 'y':
        game()
    else:
        print('Okay then. Goodbye.')
        quit()

def game ():
# defines the game and tallies the score
    global turn, score
    num = random.choice(range(1,10))
    sel = int(input('Pick a number between 1 and 9: '))
    if sel == num:
        print('You guessed right! You win!')
        turn = turn + 1
        score = score + 1
    elif sel < num:
        print('Too low. You lose.')
        turn = turn + 1
    elif sel > num:
        print('Too high. You lose.')
        turn = turn + 1
    else:
        print('I said a number from 1 to 9. Come on man.')
        introduction()
    print('Your Score:', score, 'Attempts:', turn, 'Percent Accuracy:', int(score/turn*100))
    playagain()

def playagain():
# asks the user if they want to play again
    user_command = input("Do you want to play again? y/n ")
    if user_command == "y":
        game()
    elif user_command == "n":
        print("Thanks for playing!")
        quit()
        
turn = 0
score = 0
introduction()