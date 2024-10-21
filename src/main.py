from classes import Window, Point, Line, Cell
from maze import Maze
def main():

    win = Window(800, 600)
    # p1 = Point(100, 100)
    # p2 = Point(500, 500)
    # cell1 = Cell(p1, p2, win)
    # cell1.draw()

    Maze(150, 50, 10, 10, 50, 50, win)

    win.wait_for_close()

main()