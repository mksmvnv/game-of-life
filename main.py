import time
import pygame as pg
import numpy as np


SCREEN_SIZE = (800, 600)
CELL_SIZE = 10
CELL_COUNT = (60, 80)

COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (20, 60, 0)
COLOR_ALIVE_NEXT = (80, 240, 0)

PAUSE = 0.001
FPS = 60


# Function to update the state of cells on the screen
def update(screen, cells, size, with_progress=False):
    # Create a new array of cells for updating
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    # Iterate over each cell in the array
    for row, col in np.ndindex(cells.shape):
        # Count the number of neighbors for the cell
        neighbours = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        # Set the color based on the state of the cell
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        # If the cell is alive
        if cells[row, col] == 1:
            # If it has less than 2 or more than 3 neighbors, it dies
            if neighbours < 2 or neighbours > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            # If it has 2 or 3 neighbors, it stays alive
            elif 2 <= neighbours <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        # If the cell is dead
        else:
            # If it has 3 neighbors, it comes to life
            if neighbours == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        # Draw the cell on the screen
        pg.draw.rect(screen, color,
                     (col * size, row * size, size - 1, size - 1))

    return updated_cells


# Main function
def main():
    # Initialize Pygame
    pg.init()
    # Create the screen
    screen = pg.display.set_mode(SCREEN_SIZE)

    # Create an array of cells
    cells = np.zeros(CELL_COUNT)
    # Fill the screen with the grid color
    screen.fill(COLOR_GRID)
    # Update the state of cells on the screen
    update(screen, cells, CELL_SIZE)

    # Update the screen
    pg.display.flip()
    pg.display.update()

    # Create a timer
    clock = pg.time.Clock()

    # Variable to determine the state of the game (running or stopped)
    running = False

    while True:
        # Handle events
        for event in pg.event.get():
            # If the event is quitting the game, exit the program
            if event.type == pg.QUIT:
                pg.quit()
                return
            # If the spacebar is pressed,
            # change the state of the game (running or stopped)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    running = not running
                    update(screen, cells, CELL_SIZE)
                    pg.display.update()
            # If the left mouse button is pressed,
            # set the cell to alive
            if pg.mouse.get_pressed()[0]:
                pos = pg.mouse.get_pos()
                cells[pos[1] // CELL_SIZE, pos[0] // CELL_SIZE] = 1
                update(screen, cells, CELL_SIZE)
                pg.display.update()

        # Fill the screen with the grid color
        screen.fill(COLOR_GRID)

        # Set the window title with the current FPS
        pg.display.set_caption(f"FPS: {str(int(clock.get_fps()))}")

        # If the game is running, update the state of cells and the screen
        if running:
            cells = update(screen, cells, CELL_SIZE, with_progress=True)
            pg.display.update()

        clock.tick(FPS)

        time.sleep(PAUSE)


if __name__ == '__main__':
    main()
