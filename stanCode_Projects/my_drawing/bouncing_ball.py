"""
File: Bouncing_ball.py
Name: Johnson
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variables
window = GWindow(800, 500, title='bouncing_ball.py')
times = 0
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
on_the_run = False




def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(start)


def start(mouse):
    global times, on_the_run

    if not on_the_run:  # Make sure when the ball is bouncing the mouseclicked won't work
        on_the_run = True
        ball.filled = 'True'
        window.add(ball)
        vy = 0

        while on_the_run:
            if times < 3:    # Let the ball can only bounce three times

                if ball.y + SIZE >= window.height:
                    vy = -vy * REDUCE
                    vy += GRAVITY

                if ball.x + SIZE >= window.width:   # Let the ball recover to its original condition
                    times += 1
                    ball.x = START_X
                    ball.y = START_Y
                    vy = 0
                    on_the_run = False

                ball.move(VX, vy)
                vy += GRAVITY
                print(vy, ball.y)
                pause(DELAY)
            else:
                break


if __name__ == "__main__":
    main()
