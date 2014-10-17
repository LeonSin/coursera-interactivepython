# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# range, default value is 100
num_range = 100
secret_number = 0
# limited numbers of guesses
num_guess = 0

# helper function to start and restart the game
def new_game():
    global num_range
    global secret_number
    global num_guess
    secret_number = random.randrange(0, 100)
    print 'New game. Range is from 0 to ' + str(num_range)
    num_guess = int(math.ceil(math.log(num_range + 1, 2)))
    print 'Number of remaining guess is ' + str(num_guess)
    print 

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    global secret_number
    num_range = 100
    secret_number = random.randrange(0, 100)
    new_game()

    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    global secret_number
    num_range = 1000
    secret_number = random.randrange(0, 1000)
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global num_guess
    
    # input numeric validation 
    if(guess.isdigit()):
        print 'Guess was ' + guess
        num_guess -= 1
        print 'Number of remaining guess is ' + str(num_guess)
        if(num_guess == 0):
            print 'You ran out of guesses. The number was ' + str(secret_number)
            print 
            new_game()
        else:
            if(int(guess) > secret_number):
                print 'Lower!'
            elif(int(guess) < secret_number):
                print 'Higher!'
            else:
                print 'Correct!'
                print
                new_game()
        print
    else:
        print 'invalid input [' + guess + '] ,only numbers accepted'
        print 'Number of remaining guess is ' + str(num_guess)
        print 
        
# create frame
frame = simplegui.create_frame("Guess The Number", 200, 200)
frame.add_button('Range is [0, 100)', range100, 200)
frame.add_button('Range is [0, 1000)', range1000, 200)
frame.add_input('Enter a guess', input_guess, 200)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
