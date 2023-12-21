from window import Window, Point, Line

def main():
    win = Window(800, 600)
    
    win.draw_line(Line(Point(100, 200), Point(200, 400)))
    win.draw_line(Line(Point(150, 433), Point(210, 456)))
    win.draw_line(Line(Point(150, 250), Point(150, 550)))
    
    win.wait_for_close()



main()