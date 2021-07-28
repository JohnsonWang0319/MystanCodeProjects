"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_space = (width - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)
    return GRAPH_MARGIN_SIZE + x_space * year_index


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW,
                           font='Helvetica 16')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Write your code below this line
    y_space = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK  # the y_space is proportional to rank number 1000
    for j in range(len(lookup_names)):  # whether the name in lookup_names is in name_data
        name = lookup_names[j]
        if name in name_data:
            year_rank = name_data[name]  # {'year':'rank', 'year':'rank', .....}
            first_year = str(YEARS[0])
            if first_year in year_rank:  # find out the first ranking point of each name in 1900
                rank_first = int(year_rank[first_year])
                first_x = GRAPH_MARGIN_SIZE
                first_y = GRAPH_MARGIN_SIZE + int(rank_first) * y_space
                if rank_first <= MAX_RANK:
                    canvas.create_text(first_x, first_y, text=f'{name} {rank_first}', anchor=tkinter.SW,
                                       font='Helvetica 14', fill=COLORS[j % len(COLORS)])
                else:
                    first_x = GRAPH_MARGIN_SIZE
                    first_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(first_x, first_y, text=f'{name} within 1000', anchor=tkinter.SW,
                                       font='Helvetica 14', fill=COLORS[j % len(COLORS)])
            else:  # YEARS[0] doesn't have ranking
                first_x = GRAPH_MARGIN_SIZE
                first_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_text(first_x, first_y, text=f'{name} *', anchor=tkinter.SW,
                                   font='Helvetica 14', fill=COLORS[j % len(COLORS)])

            for i in range(1, len(YEARS)):  # except for the first year 1990
                year = str(YEARS[i])
                x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)

                # whether the name in that certain year have ranking

                if year in year_rank:
                    rank = int(year_rank[year])
                    if rank <= MAX_RANK:
                        canvas.create_line(first_x, first_y, x_coordinate, GRAPH_MARGIN_SIZE + rank * y_space,
                                           width=LINE_WIDTH, fill=COLORS[j % len(COLORS)])
                        canvas.create_text(x_coordinate + TEXT_DX, GRAPH_MARGIN_SIZE + rank * y_space,
                                           text=f'{name} {year_rank[year]}', anchor=tkinter.SW, font='Helvetica 14',
                                           fill=COLORS[j % len(COLORS)])
                        # change the original point so that next for loop can form another line
                        first_x = x_coordinate
                        first_y = GRAPH_MARGIN_SIZE + rank * y_space
                    else:
                        canvas.create_line(first_x, first_y, x_coordinate, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           width=LINE_WIDTH, fill=COLORS[j % len(COLORS)])
                        canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           text=f'{name} within 1000', anchor=tkinter.SW, font='Helvetica 14',
                                           fill=COLORS[j % len(COLORS)])
                        # change the original point so that next for loop can form another line
                        first_x = x_coordinate
                        first_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                else:
                    # the name in that certain year doesn't have ranking, so change the text and gave a default value
                    canvas.create_line(first_x, first_y, x_coordinate, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       width=LINE_WIDTH, fill=COLORS[j % len(COLORS)])
                    canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=f'{name} *',
                                       anchor=tkinter.SW, font='Helvetica 14', fill=COLORS[j % len(COLORS)])
                    # change the original point so that next for loop can form another line
                    first_x = x_coordinate
                    first_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
