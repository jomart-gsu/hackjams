from graphics_lib import *

CIRCLE_X = 250
CIRCLE_Y = 250
CIRCLE_RADIUS = 10
CIRCLE_X_SPEED = 3
CIRCLE_Y_SPEED = -2

PADDLE_X = 200
PADDLE_Y = 350
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_SPEED = 0

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400

def key_press(key):
    global PADDLE_SPEED
    if key == "Left":
        PADDLE_SPEED = -5
    if key == "Right":
        PADDLE_SPEED = 5

def draw_frame():
    # Need "global" statements whenever we want to update variables that weren't declared
    # inside the current function. This is considered bad style in real life, but 
    # it will work for now.
    global CIRCLE_X, CIRCLE_Y, CIRCLE_X_SPEED, CIRCLE_Y_SPEED, PADDLE_X, PADDLE_SPEED
    
    # draw the ball and paddle
    draw_circle(CIRCLE_X, CIRCLE_Y, CIRCLE_RADIUS, "blue")
    draw_rectangle(PADDLE_X, PADDLE_Y, PADDLE_X + PADDLE_WIDTH, PADDLE_Y + PADDLE_HEIGHT, "red")
    
    # If the ball hits either side of the screen, it should bounce off
    if CIRCLE_X + CIRCLE_RADIUS >= WINDOW_WIDTH:
        CIRCLE_X_SPEED *= -1
    if CIRCLE_X - CIRCLE_RADIUS <= 0:
        CIRCLE_X_SPEED *= -1
    
    # If the ball hits a paddle, it should bounce off
    if (
        PADDLE_Y <= CIRCLE_Y + CIRCLE_RADIUS < PADDLE_Y + CIRCLE_Y_SPEED and
        PADDLE_X <= CIRCLE_X <= PADDLE_X + PADDLE_WIDTH
    ):
        CIRCLE_Y_SPEED *= -1

    # If the ball hits the bottom, freeze it
    if CIRCLE_Y + CIRCLE_RADIUS >= WINDOW_HEIGHT:
        CIRCLE_Y_SPEED = 0
        CIRCLE_X_SPEED = 0

    # If the ball hits the top of the screen, it bounces off
    if CIRCLE_Y - CIRCLE_RADIUS <= 0:
        CIRCLE_Y_SPEED *= -1
    
    # If the paddle hits the side of the screen, it should stop moving
    # Subtle point: these inequalities must be strict (i.e. not <= 0 or >= 0)
    # This is because we're putting the paddle back at the right or left edge
    # of the screen if it wanders off. If we set the speed to zero whenever the
    # paddle is EXACTLY AT either edge, it will get "stuck" to the side of the screen.
    if PADDLE_X < 0 or PADDLE_X + PADDLE_WIDTH > WINDOW_WIDTH:
        PADDLE_SPEED = 0
        PADDLE_X = max(0, PADDLE_X)
        PADDLE_X = min(WINDOW_WIDTH - PADDLE_WIDTH, PADDLE_X)
    

    # Update the ball and paddle locations
    CIRCLE_X += CIRCLE_X_SPEED
    CIRCLE_Y += CIRCLE_Y_SPEED
    PADDLE_X += PADDLE_SPEED

start_graphics(
    draw_frame,
    window_width=WINDOW_WIDTH,
    window_height=WINDOW_HEIGHT,
    key_press=key_press,
)
