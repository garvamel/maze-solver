from base_classes import Window
from maze import Maze

def main():

    win = Window(1600, 1200)

    maze = Maze(150, 50, 25, 25, 30, 30, win)
    maze.solve()
    win.wait_for_close()

if __name__  == "__main__":
    main()