Here’s a Python program to simulate Conway’s Game of Life, 
a cellular automaton devised by mathematician John Conway. 
The program allows users to define an initial grid and then evolves the grid based on the game's rules.

### Explanation of the Program

1. Game Rules:
   - Any live cell with 2 or 3 live neighbors survives.
   - Any dead cell with exactly 3 live neighbors becomes alive.
   - All other live cells die in the next generation, and all other dead cells remain dead.

2. Grid Initialization:
   - By default, a random grid of 0s (dead cells) and 1s (live cells) is created.
   - You can also provide a specific initial state by passing coordinates of live cells.

3. Grid Updates:
   - The `update_grid()` function computes the next state of the grid by checking the neighbors of each cell.

4. Visualization:
   - The grid is displayed in the console using `█` for live cells and a blank space for dead cells.
   - The console clears between steps for a smooth animation.

5. Parameters:
   - `rows` and `cols`: Size of the grid.
   - `steps`: Number of iterations.
   - `initial_state`: Coordinates of the initial live cells (optional).

### How to Run
Run it in your terminal or IDE:
   ```bash
   python game_of_life.py
   ```

### Customizations
- Grid Size: Modify `rows` and `cols` to change the grid's dimensions.
- Speed: Adjust `time.sleep(0.5)` to make the animation faster or slower.
- Initial State: Define different initial patterns (e.g., gliders, still lifes, oscillators).

