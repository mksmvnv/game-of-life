import time
import pygame as pg
import numpy as np


SCREEN_SIZE = (800, 600)
CELL_SIZE = 10
CELL_COUNT = (60, 80)
COLOR_BG = (20, 20, 20)
COLOR_GRID = (60, 60, 60)
COLOR_DIE_NEXT = (180, 180, 180)
COLOR_ALIVE_NEXT = (240, 240, 240)


def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        neighbours = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if neighbours < 2 or neighbours > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= neighbours <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:
            if neighbours == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        pg.draw.rect(screen, color,
                     (col * size, row * size, size - 1, size - 1))

    return updated_cells


def main():
    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)

    cells = np.zeros(CELL_COUNT)
    screen.fill(COLOR_GRID)
    update(screen, cells, CELL_SIZE)

    pg.display.flip()
    pg.display.update()
    
    clock = pg.time.Clock()

    running = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    running = not running
                    update(screen, cells, CELL_SIZE)
                    pg.display.update()
            if pg.mouse.get_pressed()[0]:
                pos = pg.mouse.get_pos()
                cells[pos[1] // CELL_SIZE, pos[0] // CELL_SIZE] = 1
                update(screen, cells, CELL_SIZE)
                pg.display.update()

        screen.fill(COLOR_GRID)
        
        pg.display.set_caption(f"FPS: {str(int(clock.get_fps()))}")

        if running:
            cells = update(screen, cells, CELL_SIZE, with_progress=True)
            pg.display.update()
        
        clock.tick(60)

        time.sleep(0.01)


if __name__ == '__main__':
    main()
