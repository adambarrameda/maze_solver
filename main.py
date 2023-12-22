from window import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c2 = Cell(win)
    c3 = Cell(win)
    
    c1.draw(100, 200, 200, 400)
    c2.draw(150, 210, 433, 456)
    c3.draw(160, 170, 250, 550)

    c1.draw_move(c2)

    win.wait_for_close()



main()