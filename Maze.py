import pygame
import sys
from collections import deque

# Función para encontrar todos los caminos usando BFS
def bfs_all_paths(maze, start, goal):
    queue = deque([[start]])
    all_paths = []

    while queue:
        path = queue.popleft()
        x, y = path[-1]

        if (x, y) == goal:
            all_paths.append(path)
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and 
                maze[nx][ny] == 0 and (nx, ny) not in path):
                new_path = list(path)
                new_path.append((nx, ny))
                queue.append(new_path)
                
    return all_paths

# Función para visualizar los caminos con pygame
def visualize_paths(maze, path_fast, path_slow, start, goal):
    pygame.init()
    screen_size = (600, 600)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Visualización del Laberinto')

    cell_size = screen_size[0] // len(maze)
    colors = {
        'wall': (0, 0, 0),
        'path_fast': (0, 255, 0),  # Verde para el camino más rápido
        'path_slow': (255, 0, 0),  # Rojo para el camino menos eficiente
        'start': (0, 0, 255),
        'goal': (255, 255, 0),
        'empty': (255, 255, 255)
    }

    def draw_maze(current_step_fast=None, current_step_slow=None):
        screen.fill(colors['empty'])
        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                color = colors['wall'] if cell == 1 else colors['empty']
                pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

        if current_step_fast:
            for (x, y) in current_step_fast:
                pygame.draw.rect(screen, colors['path_fast'], (y * cell_size, x * cell_size, cell_size, cell_size))

        if current_step_slow:
            for (x, y) in current_step_slow:
                pygame.draw.rect(screen, colors['path_slow'], (y * cell_size, x * cell_size, cell_size, cell_size))

        pygame.draw.rect(screen, colors['start'], (start[1] * cell_size, start[0] * cell_size, cell_size, cell_size))
        pygame.draw.rect(screen, colors['goal'], (goal[1] * cell_size, goal[0] * cell_size, cell_size, cell_size))

        pygame.display.flip()

    # Mostrar paso a paso
    max_steps = max(len(path_fast), len(path_slow))
    for step in range(max_steps):
        current_step_fast = path_fast[:step + 1] if step < len(path_fast) else path_fast
        current_step_slow = path_slow[:step + 1] if step < len(path_slow) else path_slow
        draw_maze(current_step_fast, current_step_slow)
        pygame.time.wait(500)  # Esperar 500 ms entre pasos

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Función principal para el juego Maze Runner
def maze_game():
    # Datos del laberinto
    maze = [
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (9, 9)

    # Encontrar todos los caminos y visualizar
    all_paths = bfs_all_paths(maze, start, goal)
    if all_paths:
        path_fast = min(all_paths, key=len)
        path_slow = max(all_paths, key=len)
        visualize_paths(maze, path_fast, path_slow, start, goal)
    else:
        print("No se encontró un camino.")

# Ejecutar la función principal solo si se llama directamente
if __name__ == "__main__":
    maze_game()
