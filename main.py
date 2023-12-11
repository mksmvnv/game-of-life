import time
import pygame as pg
import numpy as np


COLOR_BG = (20, 20, 20)
COLOR_GRID = (60, 60, 60)
COLOR_DIE_NEXT = (180, 180, 180)
COLOR_ALIVE_NEXT = (240, 240, 240)

def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        neighbours = np.sum(cells[row-1:row+2, col-1:col+2]) - cells(row, col)
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT
        
        if cells[row, col] == 1:
            if neighbours < 2 or neighbours > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= neighbours <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        







