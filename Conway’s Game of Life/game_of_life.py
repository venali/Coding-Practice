import numpy as np
import time
import os

# Define the rules of the Game of Life
def update_grid(grid):
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)

    for row in range(rows):
        for col in range(cols):
            # Count the alive neighbors
            alive_neighbors = np.sum(grid[row-1:row+2, col-1:col+2]) - grid[row, col]

            # Apply the rules
            if grid[row, col] == 1: # Cell is alive
                if alive_neighbors in [2, 3]:
                    new_grid[row, col] = 1 # Stays alive
            else: # Cell is dead
                if alive_neighbors == 3:
                    new_grid[row, col] = 1 # Becomes alive

    return new_grid

# Display the grid
def print_grid(grid):
    os.system("cls" if os.name == "nt" else "clear") # Clear console for better visualization
    for row in grid:
        print("".join(["█" if cell == 1 else " " for cell in row]))

# Main function to run the simulation
def game_of_life(rows=20, cols=20, steps=100, initial_state=None):
    # Initialize the grid
    if initial_state is None:
        grid = np.random.choice([0, 1], size=(rows, cols))
    else:
        grid = np.zeros((rows, cols), dtype=int)
        for cell in initial_state:
            grid[cell[0], cell[1]] = 1

    # Run the simulation for the given number of steps
    for step in range(steps):
        print(f"Step {step + 1}")
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(0.5)

# Example usage
if __name__ == "__main__":
    # Define an initial state (optional)
    initial_state = [
        (10, 10), (10, 11), (10, 12), # Horizontal line
        (11, 10), (12, 11), (11, 12) # Glider shape
    ]

    # Run the game
    game_of_life(rows=20, cols=20, steps=50, initial_state=initial_state)

