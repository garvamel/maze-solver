from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas_widget = Canvas(height=self.height, width=self.width)
        self.canvas_widget.pack()
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def draw_line(self, line, fill_color):
        line.draw(self.canvas_widget, fill_color)

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        if self._win:
            self._x1 = x1
            self._x2 = x2
            self._y1 = y1
            self._y2 = y2

            point_ul = Point(self._x1, self._y1)
            point_ur = Point(self._x2, self._y1)
            point_bl = Point(self._x1, self._y2)
            point_br = Point(self._x2, self._y2)

            left_wall = Line(point_ul, point_bl)
            right_wall = Line(point_ur, point_br)
            top_wall = Line(point_ul, point_ur)
            bottom_wall = Line(point_bl, point_br)


            if self.has_left_wall:
                self._win.draw_line(left_wall, "black")
            else:
                self._win.draw_line(left_wall, "#d9d9d9")
            
            if self.has_right_wall:
                self._win.draw_line(right_wall, "black")
            else:
                self._win.draw_line(right_wall, "#d9d9d9")
            
            if self.has_top_wall:
                self._win.draw_line(top_wall, "black")
            else:
                self._win.draw_line(top_wall, "#d9d9d9")
            
            if self.has_bottom_wall:
                self._win.draw_line(bottom_wall, "black")
            else:
                self._win.draw_line(bottom_wall, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        to_cell_center_x = (to_cell._x1 + to_cell._x2)//2
        to_cell_center_y = (to_cell._y1 + to_cell._y2)//2
        to_cell_center = Point(to_cell_center_x, to_cell_center_y)

        self_center_x = (self._x1 + self._x2)//2
        self_center_y = (self._y1 + self._y2)//2
        self_center = Point(self_center_x, self_center_y)

        line_to_cell = Line(self_center, to_cell_center)

        if undo == True:
            self._win.draw_line(line_to_cell, "gray")
        elif undo == False:
            self._win.draw_line(line_to_cell, "red")
