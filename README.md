# Game of Life

This is a simple implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) using Pygame.

![the-game-of-life](https://life.written.ru/_pictures/gardner/relay.gif)

## Description

The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway. It consists of a grid of cells, each of which can be in one of two states: alive or dead. The state of each cell evolves over time based on a set of rules, creating various interesting patterns.

## Prerequisites

*To run this code, you need to have the following installed*:

- Python 3.12.1
- Pygame
- NumPy

   ```
   pip install pygame numpy
## How to Run

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the following command to execute the code:

   ```bash
   python main.py
## The simulation will start, and you can interact with it using the following controls:

- Press **SPACE** to pause/resume the simulation.
- Left-click on the grid to toggle the state of individual cells.
- Close the window to exit the program.

## Configuration
*You can modify the following parameters in the main.py file*:
- **SCREEN_SIZE**: The size of the Pygame window in pixels.
- **CELL_SIZE**: The size of each cell in pixels.
- **CELL_COUNT**: The number of cells in the grid.
- **COLOR_BG**: The background color of the grid.
- **COLOR_GRID**: The color of the grid lines.
- **COLOR_DIE_NEXT**: The color of cells that will die in the next generation.
- **COLOR_ALIVE_NEXT**: The color of cells that will be alive in the next generation.
- **PAUSE**: The time delay in seconds between each generation.
- **FPS**: The desired frames per second for the game.

## License
The project is licensed under the [MIT License](https://ru.wikipedia.org/wiki/%D0%9B%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F_MIT).

