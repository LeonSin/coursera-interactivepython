# template for "Stopwatch: The Game"
import simplegui

# define global variables
t=0
time=''
suc = 0
all = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    time=str(t//600)+':'+str((t%600)//100)+str((t%100)//10)+':'+str(t%10)
    #print time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    global all,suc
    if not timer.is_running():
        return
    timer.stop()
    all+=1
    if t%10 == 0:
        suc+=1
def reset():
    global t,suc,all
    t=0
    suc=0
    all=0

# define event handler for timer with 0.1 sec interval
def count():
    global t
    t+=1


# define draw handler
def draw(c):
    format(t)
    c.draw_text(time, (100, 200), 96, "Red")
    c.draw_text(str(suc)+'/'+str(all), (400, 50), 36, "Red")
    
# create frame
c=simplegui.create_frame("Stop Watch", 500, 500,100)

# register event handlers
c.set_draw_handler(draw)
c.add_button('Start',start,100)
c.add_button('Stop',stop,100)
c.add_button('Reset',reset,100)

timer=simplegui.create_timer(100, count)
# start frame
c.start()

# Please remember to review the grading rubric
