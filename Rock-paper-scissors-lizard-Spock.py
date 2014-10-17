import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print '[Error] ' + str(name) + ' has no matches found'
        return -1



def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print '[Error] ' + str(number) + ' has no matches found'
        return 'unknown'

    

def rpsls(player_choice): 
    # print out the message for the player's choice
    print 'Player chooses ' + player_choice
    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print 'Computer chooses ' + comp_choice
    
    difference = ( player_number - comp_number ) % 5
    # determine who wins
    if difference == 1 or difference == 2:
        print 'Player wins!'
    elif difference == 3 or difference == 4:
        print 'Computer wins!'
    elif difference == 0:
        print 'Player and computer tie!'
    else:
        print 'System error, plz check!'
    # print a blank line to separate consecutive games
    print
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


