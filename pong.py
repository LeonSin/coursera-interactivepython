# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
HALF_WIDTH = WIDTH / 2.0
HALF_HEIGHT = HEIGHT / 2.0
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1 = 0
score2 = 0

def restart_button_handler():
    global score1, score2
    global paddle1_pos, paddle2_pos, ball_pos
    paddle1_pos = [0 + PAD_WIDTH, HEIGHT / 2.0]
    paddle2_pos = [WIDTH - PAD_WIDTH, HEIGHT / 2.0]
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    score1 = 0 
    score2 = 0
    new_game(RIGHT)
    
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240) / 60.0, -random.randrange(60, 180) / 60.0]
    elif direction == LEFT:
        ball_vel = [-random.randrange(120, 240) / 60.0, -random.randrange(60, 180) / 60.0]    
        
# define event handlers
def new_game(right):
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = [0 + PAD_WIDTH, HEIGHT / 2.0]
    paddle2_pos = [WIDTH - PAD_WIDTH, HEIGHT / 2.0]
    paddle1_vel = 0
    paddle2_vel = 0
    
    spawn_ball(right)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")  
    # update ball
    if ball_pos[0] <= BALL_RADIUS:
        if ball_pos[1] > paddle1_pos[1] - PAD_HEIGHT / 2 and ball_pos[1] < paddle1_pos[1] + PAD_HEIGHT / 2:
            ball_vel[0] = -ball_vel[0]
            velocityIncrease()
        else:
            score2 += 1
            new_game(RIGHT)
    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        if ball_pos[1] > (paddle2_pos[1] - HALF_PAD_HEIGHT) and ball_pos[1] < (paddle2_pos[1] + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            velocityIncrease()
        else:
            score1 += 1
            new_game(LEFT)  
    ball_pos[0] += ball_vel[0]
        
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle( ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] < HALF_PAD_HEIGHT:
        paddle1_pos[1] = HALF_PAD_HEIGHT
    elif paddle1_pos[1] > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle1_pos[1] += paddle1_vel
    
    if paddle2_pos[1] < HALF_PAD_HEIGHT:
        paddle2_pos[1] = HALF_PAD_HEIGHT
    elif paddle2_pos[1] > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle2_pos[1] += paddle2_vel
    
    
    # draw paddles
    canvas.draw_line([0 + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT],[0 + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], PAD_WIDTH, 'White')
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], PAD_WIDTH, 'White')
    # draw scores
    canvas.draw_text(str(score1), [HALF_WIDTH / 2, 60], 50, 'White')
    canvas.draw_text(str(score2), [HALF_WIDTH + HALF_WIDTH / 2, 60], 50, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -8
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 8
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -8
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 8
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

def velocityIncrease():
    global ball_vel
    print ball_vel
    ball_vel = map(lambda x: x * 1.2, ball_vel)

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
restart_button = frame.add_button('Restart', restart_button_handler)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game(RIGHT)
frame.start()