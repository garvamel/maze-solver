from classes import Cell
import time

class Maze:
    
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):

        self._cells = [[Cell(self.win) for i in range(self.num_rows)]for i in range(self.num_cols)]

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cells(i, j)


    def _draw_cells(self, i, j):
        
        cell = self._cells[i][j]
        cell_x1 = self.x1 + i * self.cell_size_x
        cell_y1 = self.y1 + j * self.cell_size_y
        cell_x2 = self.x1 + i * self.cell_size_x + self.cell_size_x
        cell_y2 = self.y1 + j * self.cell_size_x + self.cell_size_y

        cell.draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
