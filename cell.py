from window import Line, Point

class Cell:
    def __init__(self, window, p1, p2):
        self.top = True
        self.right = True
        self.bottom = True
        self.left = True
        self._x1 = p1.x
        self._x2 = p2.x
        self._y1 = p1.y
        self._y2 = p2.y
        self._win = window

    def draw(self):
        if self.top:
            line = Line(
                Point(self._x1, self._y1),
                Point(self._x2, self._y1)
                )
            self._win.draw_line(line)
        if self.right:
            line = Line(
                Point(self._x2, self._y1),
                Point(self._x2, self._y2)
                )
            self._win.draw_line(line) 
        if self.bottom:
            line = Line(
                Point(self._x1, self._y2),
                Point(self._x2, self._y2)
                )
            self._win.draw_line(line)
        if self.left:
            line = Line(
                Point(self._x1, self._y1),
                Point(self._x1, self._y2)
                )
            self._win.draw_line(line)