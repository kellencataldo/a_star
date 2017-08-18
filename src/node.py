class node:
    def __init__(self, wall, x, y):
        self.wall = wall
        self.x = x
        self.y = y
        self.parent = None
        self.g = 999
        self.h = None  # heuristic
        self.f = None

    def _eq__(self, other):
        if isinstance(other, self.__class__):
            return self.h == other.h
        return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.h < other.h
        return False

    # note: THIS IS NOT MANHATTAN DISTANCE, the commented out part is, the actual heuristic isn't,
    # i changed it to euclidean
    def set_manhattan(self, exit_node):
        self.h = (((self.x - exit_node.x) ** 2) + ((self.y - exit_node.y) ** 2)) ** .5
       # self.h = abs((self.x - exit_node.x) + (self.y - exit_node.y))

    def set_f(self):
        self.f = self.g + self.h

    def check_g(self, parent):
        if parent.g + 1 < self.g:
            return True
        else:
            return False

