import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 800  # Window dimensions
DEFAULT_CELL_SIZE = 20  # Default size of each cell
MIN_CELL_SIZE = 5  # Minimum cell size
MAX_CELL_SIZE = 50  # Maximum cell size

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize variables
cell_size = DEFAULT_CELL_SIZE
grid_width = WIDTH // cell_size
grid_height = HEIGHT // cell_size

# Initialize the grid
grid = np.random.choice([0, 1], size=(grid_height, grid_width), p=[0.7, 0.3])

# Initialize pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Load the pixel-style font
pixel_font = pygame.font.Font("../Tiny5-Regular.ttf", 24)

# Display help screen
show_help = True


# Function to draw the grid
def draw_grid(grid, cell_size):
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            color = WHITE if grid[row][col] == 1 else BLACK
            pygame.draw.rect(
                screen,
                color,
                (col * cell_size, row * cell_size, cell_size - 1, cell_size - 1)
            )


# Function to update the grid
def update_grid(grid):
    new_grid = np.zeros_like(grid)
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            # Count live neighbors
            live_neighbors = np.sum([
                grid[(row - 1) % grid.shape[0]][(col - 1) % grid.shape[1]],
                grid[(row - 1) % grid.shape[0]][col],
                grid[(row - 1) % grid.shape[0]][(col + 1) % grid.shape[1]],
                grid[row][(col - 1) % grid.shape[1]],
                grid[row][(col + 1) % grid.shape[1]],
                grid[(row + 1) % grid.shape[0]][(col - 1) % grid.shape[1]],
                grid[(row + 1) % grid.shape[0]][col],
                grid[(row + 1) % grid.shape[0]][(col + 1) % grid.shape[1]],
            ])

            # Apply the rules of the game
            if grid[row][col] == 1:  # If the cell is alive
                new_grid[row][col] = 1 if 2 <= live_neighbors <= 3 else 0
            else:  # If the cell is dead
                new_grid[row][col] = 1 if live_neighbors == 3 else 0
    return new_grid


# Function to display the simulation state
def draw_indicator(paused):
    text = "OFF" if paused else "ON"
    color = RED if paused else GREEN
    label = pixel_font.render(f"Simulation: {text}", True, color)
    screen.blit(label, (10, 10))  # Draw the label at the top-left corner


# Function to display the help screen
def draw_help_screen():
    screen.fill(BLACK)
    title = pixel_font.render("Conway's Game of Life", True, BLUE)
    instructions = [
        "Space: Play/Pause the simulation",
        "Ctrl+C: Clear the grid",
        "Mouse Click: Toggle cell state",
        "Mouse Scroll: Zoom in/out",
        "Press Enter to start the simulation"
    ]

    # Draw title
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    # Draw instructions
    for i, line in enumerate(instructions):
        text = pixel_font.render(line, True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200 + i * 40))


# Main loop
running = True
paused = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and show_help:
                show_help = False  # Exit the help screen
            if event.key == pygame.K_SPACE and not show_help:
                paused = not paused  # Toggle pause state
            if event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                grid = np.zeros((grid_height, grid_width))  # Clear the grid

        # Handle mouse clicks to toggle cells
        if event.type == pygame.MOUSEBUTTONDOWN and not show_help:
            x, y = event.pos
            col, row = x // cell_size, y // cell_size
            if row < grid.shape[0] and col < grid.shape[1]:
                grid[row][col] = 1 - grid[row][col]  # Toggle the cell's state

        # Handle mouse wheel for zoom
        if event.type == pygame.MOUSEWHEEL and not show_help:
            if event.y > 0:  # Scroll up
                cell_size = min(cell_size + 1, MAX_CELL_SIZE)
            elif event.y < 0:  # Scroll down
                cell_size = max(cell_size - 1, MIN_CELL_SIZE)

            # Recalculate grid dimensions
            grid_width = WIDTH // cell_size
            grid_height = HEIGHT // cell_size
            new_grid = np.zeros((grid_height, grid_width), dtype=int)

            # Resize the grid while preserving cell states
            for row in range(min(grid_height, grid.shape[0])):
                for col in range(min(grid_width, grid.shape[1])):
                    new_grid[row][col] = grid[row][col]
            grid = new_grid

    # Draw the help screen or the simulation
    if show_help:
        draw_help_screen()
    else:
        if not paused:
            grid = update_grid(grid)
        screen.fill(GRAY)
        draw_grid(grid, cell_size)
        draw_indicator(paused)

    pygame.display.flip()
    clock.tick(10)

# Quit pygame
pygame.quit()
