"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        self.ball_radius = ball_radius
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.brick_offset = brick_offset

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = 'True'
        self.window.add(self.paddle, (self.window.width - paddle_width) / 2,
                        self.window.height - paddle_offset - paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = 'True'
        self.window.add(self.ball, self.window.width / 2 - ball_radius, self.window.height / 2 - ball_radius)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.handle_clicked)
        onmousemoved(self.handle_moved)

        # Draw bricks
        for i in range(self.brick_cols):
            for j in range(self.brick_rows):
                self.row_brick = GRect(brick_width, brick_rows)
                self.row_brick.filled = 'True'
                if j % 10 == 0 or j % 10 == 1:
                    self.row_brick.fill_color = 'Red'
                if j % 10 == 2 or j % 10 == 3:
                    self.row_brick.fill_color = 'orange'
                if j % 10 == 4 or j % 10 == 5:
                    self.row_brick.fill_color = 'yellow'
                if j % 10 == 6 or j % 10 == 7:
                    self.row_brick.fill_color = 'green'
                if j % 10 == 8 or j % 10 == 9:
                    self.row_brick.fill_color = 'blue'
                self.window.add(self.row_brick, 0 + i * (self.brick_width + self.brick_spacing),
                                self.brick_offset + j * (self.brick_height + self.brick_spacing))

        # At the beginning the ball in standstill
        self.on_the_run = False

    # Determine the bricks are all clear or not
    def all_clear(self):
        save = ''
        for i in range(self.brick_cols):
            for j in range(self.brick_rows):
                bricks = self.window.get_object_at(0 + i * (self.brick_width + self.brick_spacing),
                                                   self.brick_offset + j * (self.brick_height + self.brick_spacing))
                if bricks is None:
                    save += '0'
                else:
                    save += '1'
        if '1' not in save:
            return True
        else:
            return False

    # Click the mouse
    def handle_clicked(self, event):
        if not self.on_the_run:
            self.on_the_run = True

    # Reset ball to the middle of the window
    def reset_ball(self):
        self.set_ball_position()
        self.set_ball_velocity()
        self.window.add(self.ball)

    def set_ball_position(self):
        self.ball.x = self.window.width / 2 - self.ball.width / 2
        self.ball.y = self.window.height / 2 - self.ball.height / 2

    # Move the mouse
    def handle_moved(self, event):
        if event.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif event.x <= 0:
            self.paddle.x = 0
        else:
            self.paddle.x = event.x

    # Set the ball original velocity
    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def velocity_x_getter(self):
        return self.__dx

    def velocity_y_getter(self):
        return self.__dy

    # Check whether the ball hit the GObject
    def bouncing_check(self):
        upper_left = self.window.get_object_at(self.ball.x, self.ball.y)
        upper_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        down_left = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        down_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        if upper_left is not None:
            return upper_left

        elif upper_right is not None:
            return upper_right

        elif down_left is not None:
            return down_left

        elif down_right is not None:
            return down_right

        else:
            return None

    # Label Game Over in the window
    def game_over(self):
        self.window.clear()
        over = GLabel('Game Over!')
        over.font = '-50'
        self.window.add(over, (self.window.width - over.width) / 2, (self.window.height - over.height) / 2)

    # Label You Win in the window
    def you_win(self):
        self.window.clear()
        win = GLabel('You Win!')
        win.font = '-50'
        self.window.add(win, (self.window.width - win.width) / 2, (self.window.height - win.height) / 2)
