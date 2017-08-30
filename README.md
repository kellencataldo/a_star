# A\* Algorithm visual animation

## Overview

This is a demonstration of the [A\* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) for machine learning. Specifically, this program operates on a maze made up of a series of 1's and 0's. The algorithm will attempt to find the shortest route to the exit, or determine that there is no path available. After running the program, a window will appear where each step of the algorithm are visualized. Here is an example of what you will see.

![Example](http://i.imgur.com/Gg3wS5C.png?1)

This is the end result of the algorithm. **Black** squares represent walls, nodes that the algorithm cannot explore. **White** squares represent nodes that the algorithm has not explored. The two **green** squares represent the entrance and exit nodes. The **pink** squares represent nodes that the algorithm has processed, and **red** squares represent nodes that make up the shortest path from the entrance to the exit.

If the exit cannot be reached, a message will display.

![EXample2](http://i.imgur.com/tqfo98d.png?1)

## Usage

The maze itself can be found in maze.txt. Configuration of the maze is fairly simple. The maze can be any width and any height, although the entrance must appear in the bottom row of the maze, and the exit must appear in either the top row, the left column, or the right column.

The other option avaliable to change the performance of the program is the **speed** value, appearing the main.py file. Increasing this value will increase the delay between each step of the algorithm, and slow the program down. This is can be done to better visualize the decision making process of the algorithm.

## How it works

The A\* Algorithm itself is a fairly simple process. Each non-wall node in the algorithm consists of three values; the g, h, f, and parent value. The data structure for these nodes can be found in node.py.

**g value** is the value given by the exact distance from the entrance to the node. The algorithm can only process nodes adjacent (not diagonal) to previously visited nodes. This value is set as the algorithm processes a node by examining the g value of the previous node, and increasing that value by one to represent to the additional step required to reach the node.

**h value** is the heuristic value used to estimate the movement cost to reach the exit for any given node. Since the location of the exit (although not the path) is known from the beginning, this value can be set for all nodes at the start of the algorithm. The heuristic function that I am using is the euclidean distance between the given node and exit node. Another common heuristic is Manhattan distance.

**f value** is simply the sum of the g and h values. Every round of the algorithm, the list of unprocessed nodes is sorted by their f value. The node with the lowest f value is selected. This means that this node's neighbors are selected, their g and f values are set (the h value has been set from the beginning), and they are added to the unprocessed list. One thing to note as that, frequently, you will see the algorithm process a node very close to the exit, and then process a node very far away from the exit. This is because the algorithm is not searching for the exit the fastest, it is searching for the path to the exit which requires the least amount of steps. Therefore, a certain node close to the exit may have a very small h value, but a very high f value, while a node further away has a smaller f value. This node further away will be explored first.

**parent** node is the node from which any other node was reached. This value is dynamic as the algorithm may discover that there is a shorter path to a given node. Therefore, this node will be "re-parented". The process of selecting nodes based on their f value and processing its neighbors will be repeated until the exit node is processed. At this point, the algorithm will walk down the list of parents, starting with the exit node, until the entrance node is reached. This chain of parents is the shortest path that the algorithm has found.
