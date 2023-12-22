from window import Line, Point

class Cell:
    def __init__(self, window):
        self.top = True
        self.right = True
        self.bottom = True
        self.left = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.top:
            self._win.draw_line(Line(Point(x1, y1),Point(x2, y1)), width=4)
        if self.right:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), width=4) 
        if self.bottom:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), width=4)
        if self.left:
            self._win.draw_line(Line(Point(x1, y1),Point(x1, y2)), width=4)

    def draw_move(self, to_cell, undo=False):
        from_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_center = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        if undo:
            self._win.draw_line(Line(from_center, to_center), "black")
        else:
            self._win.draw_line(Line(from_center, to_center), "#F27405")