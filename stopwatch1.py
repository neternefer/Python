# template for "Stopwatch: The Game"
import simplegui
# define global variables
time = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    timer.stop()
def reset():
    global time
    timer.stop()
    time = 0
    


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
    

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(str(time), [138, 110], 20, "red")
    
# create frame
frame = simplegui.create_frame("Timer", 300, 200)

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(1, tick)
start = frame.add_button("Start", start, 150)
stop =frame.add_button("Stop", stop, 150)
reset =  frame.add_button("Reset", reset, 150)


# start frame
frame.start()


# Please remember to review the grading rubric
