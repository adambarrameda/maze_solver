from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
     
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, line, color):
        line.draw(self.canvas, color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a, point_b):
        self.a = point_a
        self.b = point_b

    def draw(self, canvas, color):
        canvas.create_line(
            self.a.x, self.a.y, self.b.x, self.b.y, fill=color, width=2
        )
        canvas.pack()


def main():
    win = Window(800, 600)
    first = Point(51, 22)
    second = Point(300, 102)
    big_line = Line(first, second)
    big_line.draw(win.canvas, 'black')
    win.wait_for_close()

main()


