import pygame
import random

# Definimos las constantes para el tamaño de la cuadrícula y las celdas
GRID_SIZE = 10
CELL_SIZE = 60
TREASURE = 'T'
EMPTY = '-'
VISITED = '*'

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Crear la cuadrícula con un tesoro en una posición aleatoria
def create_grid(size):
    grid = [[EMPTY for _ in range(size)] for _ in range(size)]
    treasure_x = random.randint(0, size - 1)
    treasure_y = random.randint(0, size - 1)
    grid[treasure_x][treasure_y] = TREASURE
    return grid, (treasure_x, treasure_y)

# Dibujar la cuadrícula en la ventana
def draw_grid(screen, grid):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[x][y] == TREASURE:
                pygame.draw.rect(screen, GREEN, rect)
            elif grid[x][y] == VISITED:
                pygame.draw.rect(screen, BLUE, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

# Algoritmo de Búsqueda Recursiva
def search_treasure(screen, grid, x, y, path):
    # Verificar los límites de la cuadrícula
    if x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
        return False
    # Si encontramos el tesoro, agregamos la posición al camino y retornamos True
    if grid[x][y] == TREASURE:
        path.append((x, y))
        return True
    # Si la celda ya ha sido visitada, no la volvemos a explorar
    if grid[x][y] == VISITED:
        return False

    # Marcar la celda como visitada y agregarla al camino
    grid[x][y] = VISITED
    path.append((x, y))
    
    # Dibujar la cuadrícula actualizada y esperar para mostrar la animación
    draw_grid(screen, grid)
    pygame.display.flip()
    pygame.time.wait(500)  # Esperar 500 ms entre pasos para visualizar

    # Intentar explorar las 4 direcciones: derecha, abajo, izquierda, arriba
    if (search_treasure(screen, grid, x + 1, y, path) or
        search_treasure(screen, grid, x, y + 1, path) or
        search_treasure(screen, grid, x - 1, y, path) or
        search_treasure(screen, grid, x, y - 1, path)):
        return True

    # Si no encontramos el tesoro, retrocedemos en el camino
    path.pop()
    return False

# Función principal para ejecutar el juego
def busqueda_recursiva():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Búsqueda del Tesoro')

    grid, treasure_position = create_grid(GRID_SIZE)
    start_x, start_y = 0, 0  # Empezamos en la esquina superior izquierda
    path = []

    print("¡Bienvenido al Juego de Búsqueda del Tesoro!")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # Llamamos a la búsqueda recursiva para encontrar el tesoro
        if search_treasure(screen, grid, start_x, start_y, path):
            print("\n¡Tesoro encontrado!")
            print("El camino para llegar al tesoro es:")
            for step in path:
                print(step)
        else:
            print("\nNo se encontró el tesoro.")

        running = False  # Finalizar el juego después de un intento

    print("\nLa cuadrícula final es:")
    for row in grid:
        print(' '.join(row))

if __name__ == "__main__":
    busqueda_recursiva()
