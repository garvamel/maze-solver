from base_classes import Cell
import time
import random

class Maze:
    
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):

        self._cells = [[Cell(self.win) for i in range(self.num_rows)]for i in range(self.num_cols)]

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        
        cell = self._cells[i][j]
        cell_x1 = self.x1 + i * self.cell_size_x
        cell_y1 = self.y1 + j * self.cell_size_y
        cell_x2 = self.x1 + i * self.cell_size_x + self.cell_size_x
        cell_y2 = self.y1 + j * self.cell_size_x + self.cell_size_y

        cell.draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            # time.sleep(0.01)

    def _break_entrance_and_exit(self):
        if self.win:
            self._cells[0][0].has_top_wall = False
            self._draw_cell(0, 0)

            br_cell_i = self.num_cols - 1
            br_cell_j = self.num_rows - 1
            self._cells[br_cell_i][br_cell_j].has_bottom_wall = False
            self._draw_cell(br_cell_i, br_cell_j)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_coords = []

            if i > 0 and self._cells[i-1][j].visited == False:
                    possible_coords.append((i-1, j))
            if i < self.num_cols - 1 and self._cells[i+1][j].visited == False:
                    possible_coords.append((i+1, j))
            if j > 0  and self._cells[i][j-1].visited == False:
                    possible_coords.append((i, j-1))
            if j < self.num_rows -1  and self._cells[i][j+1].visited == False:
                    possible_coords.append((i, j+1))

            if len(possible_coords) == 0:
                self._draw_cell(i, j)
                return

            next_cell = random.randrange(len(possible_coords))
            next_i, next_j = possible_coords[next_cell]
            if i < next_i:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][j].has_left_wall = False
            if i > next_i:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][j].has_right_wall = False
            if j < next_j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][next_j].has_top_wall = False
            elif j > next_j:
                self._cells[i][j].has_top_wall = False
                self._cells[i][next_j].has_bottom_wall = False

            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
         return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if (i,j) == (self.num_cols - 1,self.num_rows - 1):
            return True
        # directions = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        directions = {"right": (i + 1, j), "left": (i - 1, j), "up": (i, j - 1), "down": (i, j + 1)}
        for dir in directions:
            x, y = directions[dir][0], directions[dir][1]
            if x < 0 or x >= self.num_cols or y < 0 or y >= self.num_rows:
                continue
            ref_cell = self._cells[i][j]
            dest_cell = self._cells[x][y]
            if dir == "right" and not ref_cell.has_right_wall and not dest_cell.has_left_wall and not dest_cell.visited:
                Cell.draw_move(ref_cell, dest_cell)
                if self._solve_r(x,y):
                    return True
                else:
                    Cell.draw_move(ref_cell, dest_cell, undo=True)
            elif dir == "left" and not ref_cell.has_left_wall and not dest_cell.has_right_wall and not dest_cell.visited:
                Cell.draw_move(ref_cell, dest_cell)
                if self._solve_r(x,y):
                    return True
                else:
                    Cell.draw_move(ref_cell, dest_cell, undo=True)
            elif dir == "down" and not ref_cell.has_bottom_wall and not dest_cell.has_top_wall and not dest_cell.visited:
                Cell.draw_move(ref_cell, dest_cell)
                if self._solve_r(x,y):
                    return True
                else:
                    Cell.draw_move(ref_cell, dest_cell, undo=True)
            elif dir == "up" and not ref_cell.has_top_wall and not dest_cell.has_bottom_wall and not dest_cell.visited:
                Cell.draw_move(ref_cell, dest_cell)
                if self._solve_r(x,y):
                    return True
                else:
                    Cell.draw_move(ref_cell, dest_cell, undo=True)
        else:
            return False
