"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics(paddle_width=200)
    lives = NUM_LIVES
    graphics.set_ball_velocity()
    dx = graphics.velocity_x_getter()
    dy = graphics.velocity_y_getter()

    # Wait until user click the mouse
    while not graphics.on_the_run:
        pause(FRAME_RATE)

        # Add animation loop!
        while graphics.on_the_run:

            # Pause
            pause(FRAME_RATE)

            # Update
            if graphics.ball.y >= graphics.window.height:  # Game Over!
                lives -= 1
                graphics.on_the_run = False
                if lives == 0:
                    graphics.game_over()
                if lives > 0:
                    graphics.reset_ball()
                else:
                    break

            if graphics.all_clear():  # Win!
                graphics.you_win()
                break

            graphics.ball.move(dx, dy)

            # Bounce
            if graphics.bouncing_check() is not None:
                if graphics.bouncing_check() is graphics.paddle:
                    if dy > 0:
                        dy = -dy

                else:
                    dy = -dy
                    graphics.window.remove(graphics.bouncing_check())

            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                dx = -dx
            elif graphics.ball.y <= 0 and dy < 0:
                dy = -dy


if __name__ == '__main__':
    main()
