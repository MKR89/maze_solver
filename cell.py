from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
            
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        from_x_mid = (self._x1 + self._x2) / 2
        from_y_mid = (self._y1 + self._y2) / 2
        
        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2
        
        fill_colour = "red"
        if undo:
            fill_colour = "gray"
        
        # -> Left 
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, from_y_mid), 
                        Point(from_x_mid, from_y_mid))
            self._win.draw_line(line, fill_colour)
            line = Line(Point(to_x_mid, to_y_mid), 
                        Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line, fill_colour)
        
        # -> right 
        elif self._x1 < to_cell._x1:
           line = Line(Point(from_x_mid, from_y_mid), 
                       Point(self._x2, from_y_mid))
           self._win.draw_line(line, fill_colour)
           line = Line(Point(to_cell._x1, to_y_mid),
                       Point(to_x_mid, to_y_mid))
           
        # -> up
        elif self._y1 > to_cell._y1:
            line = Line(Point(from_x_mid, from_y_mid), 
                        Point(self._x2, from_y_mid))
            self._win.draw_line(line, fill_colour)
            line = Line(Point(to_cell._x1, to_y_mid), 
                        Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_colour)
            
        # -> down
        elif self._y1 < to_cell._y1:
            line = Line(Point(from_x_mid, from_y_mid), 
                        Point(from_x_mid, self._y2))
            self._win.draw_line(line, fill_colour)
            line = Line(Point(to_x_mid, to_y_mid), 
                        Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_colour)