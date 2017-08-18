# this is the main file, which checks to make sure the maze is valid, initiates the tkinter frame
# and then hands off functionality to the a* algorithm

# note: these should all be import as __
from tkinter import *
from src.a_star import *
from src.node import *
from src.validate import *

# USER OPTION
# This changes the speed of the program
# the larger the number, the larger the delay after every round of the algorithm
speed = .1


def main():
    with open("maze.txt") as text:
        # strips the new line characters off the the maze
        maze = [list(line.strip()) for line in text]

    # validate.py, returns a list of row/col len
    col_row_len = init_validate(maze)

    # row/col len list empty, invalid maze
    if not col_row_len:
        print("There was an error with the layout of the maze")
        exit(0)

    col_len = col_row_len[0]
    row_len = col_row_len[1]

    # creating the maze
    for i in range(0,col_len):
        for j in range(0,row_len):
            # node.py class
            maze[i][j] = node(int(maze[i][j]), j, i)

    entrance_node = find_entrance(maze, col_len)
    exit_node = find_exit(maze, col_len, row_len)

    if entrance_node is None or exit_node is None:
        print("There is an error with either the entrance or the exit")
        exit(0)
    # initial frame
    root = Tk()
    canvas = Canvas(root, width=(32*row_len), height=(32*col_len))
    root.title("A-Star Demonstration")

    # hand off to functionality, a_star.py
    a_star_main(canvas, maze, entrance_node, exit_node, col_len, row_len, root, speed)
    # frame main loop after functionality
    root.mainloop()


if __name__ == '__main__':
    main()