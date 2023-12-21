from window import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    
    c1 = Cell(win, Point(100, 200), Point(200, 400))
    c2 = Cell(win, Point(150, 433), Point(210, 456))
    c3 = Cell(win, Point(150, 250), Point(170, 550))
    
    c1.draw()
    c2.draw()
    c3.draw()

    win.wait_for_close()



main()