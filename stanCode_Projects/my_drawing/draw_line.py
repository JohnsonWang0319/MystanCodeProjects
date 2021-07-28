"""
File: draw_line.py
Name: Johnson
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# This constant controls the size of the GOval
SIZE = 10

# Global Variable
window = GWindow()
oval = GOval(SIZE, SIZE)
oval_in_window = False  # determine that we need to draw a line or not

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(start)


def start(mouse):
    global oval_in_window
    if not oval_in_window:
        window.add(oval, mouse.x - SIZE / 2, mouse.y - SIZE / 2)    # add a oval in window
        oval_in_window = True
    else:
        line = GLine(oval.x + SIZE / 2, oval.y + SIZE / 2, mouse.x, mouse.y)    # add a line in window
        window.add(line)
        window.remove(oval) # remove the original oval
        oval_in_window = False






if __name__ == "__main__":
    main()
