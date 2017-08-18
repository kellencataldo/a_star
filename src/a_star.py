import time as t

# each node has a certain value associated with it
# white (0) is an unvisited node, black(1) is a wall, pink(1) is a visited node
# green(3) is reserved for the entrance and exit nodes, red (4) is a node on the completed path
color_dict = {4: "red", 3: "green", 2: "pink", 1: "black", 0: "white"}


def draw_node(canvas, given):
    canvas.create_rectangle(given.x * 32, given.y * 32, (given.x + 1) * 32, (given.y + 1) * 32, fill="orange")


# redraws the entire canvas based on the above color_dict
def draw_canvas(canvas, maze, col_len, row_len):
    for i in range(0, col_len):
        for j in range(0, row_len):
            # each rectangle is 32 pixels wide
            canvas.create_rectangle(j * 32, i*32, (j+1) * 32, (i + 1) * 32, fill=color_dict[maze[i][j].wall])
    canvas.pack()


# this function is used to get the next round of nodes to be explored, and sets their g and f values
def add_nodes(parent, maze, col_len, row_len):
    # every combination of 1, 0, -1. I did it this way so that a combination calculation
    # did not have to be performed every time this function was called
    add_list = [1, 0, -1, 0, 1]  # diagonal list[1, 1, 0, -1, -1, 0, 1, -1, 1] (not used)
    return_list = []
    for i in range(4):  # range(8) for diagonals if wanted
        x = add_list[i] + parent.x
        y = add_list[i+1] + parent.y
        # stops execution at first false so out of bounds error is not thrown
        if x in range(0,row_len) and y in range(0,col_len) and maze[y][x].wall != 1 and maze[y][x].check_g(parent):
            maze[y][x].parent = parent
            maze[y][x].g = parent.g + 1
            maze[y][x].set_f()
            return_list.append(maze[y][x])
    return return_list


def a_star_main(canvas, maze, start_node, exit_node, col_len, row_len, root, speed):
    draw_canvas(canvas, maze, col_len, row_len)

    for i in range(0, col_len):
        for j in range(0, row_len):
            # note: this only really matters for nodes that aren't walls
            maze[i][j].set_manhattan(exit_node)

    start_node.g = 0
    start_node.wall = exit_node.wall = 3 # green in the color dict

    # all nodes adjacent to the start list
    open_list = add_nodes(start_node, maze, col_len, row_len)
    closed_list = [start_node]

    found = False # boolean for exit value

    while open_list and not found:
        # sort based on f value
        open_list.sort(key=lambda node: node.f)

        next_node = open_list.pop(0)

        if next_node == exit_node:
            found = True
        else:
            next_node.wall = 2 # this node has been visited, colored pink
            closed_list.append(next_node)
            add_list = [x for x in add_nodes(next_node, maze, col_len, row_len) if x not in closed_list]
            open_list.extend(add_list)

        canvas.delete("all") # tkinter keeps track of ALL objects drawn, including ones that have been covered up
        draw_canvas(canvas, maze, col_len, row_len)
        root.update()
        t.sleep(speed)

    if not found:
        # This prints it in the middle. 16 is half of 32, the size of the blocks
        canvas.create_text((row_len*16),(col_len*16),text="Exit can't be reached",fill="green",font="Helvetica 26 bold")
        canvas.pack()
        return

    else: # this walks back through the linked list of parent nodes, from the exit to the entrance
        curr_node = exit_node.parent
        while curr_node != start_node:
            curr_node.wall = 4
            canvas.delete("all")
            draw_canvas(canvas, maze, col_len, row_len)
            root.update()
            t.sleep(speed)
            curr_node = curr_node.parent
    return





