from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                col.append(Cell(self.win))
                self._draw_cell(self, i, j)
            self._cells.append(col)
            
    def _draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x 
        x2 = self.x1 + (i + 1) * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        y2 = self.y1 + (j + 1) * self.cell_size_y
        self._cells[i][j].draw(x1, x2, y1, y2)
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.1)