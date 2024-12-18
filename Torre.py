# -*- coding: utf-8 -*-
import pygame
import sys


# Inicialización de pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Torres de Hanoi')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [(249, 87, 56), (11, 79, 108), (120, 192, 145), (255, 165, 0), (128, 0, 128), (165, 42, 42), (255, 192, 203)]

# Parámetros de las torres y discos
n = 3  # Número de discos
tower_positions = [200, 400, 600]
disk_widths = [150, 120, 90, 60, 30]

# Inicialización de las torres
def initialize_towers(n):
    return [list(range(n, 0, -1)), [], []]

# Dibuja el estado actual de las torres
def print_current_state(towers):
    screen.fill(WHITE)
    for i, tower in enumerate(towers):
        # Dibujar el palo central
        pygame.draw.line(screen, BLACK, (tower_positions[i], 100), (tower_positions[i], screen_height), 5)
        for j, disk in enumerate(tower):
            disk_width = disk_widths[disk-1]
            disk_height = 20
            x_pos = tower_positions[i] - (disk_width // 2)
            y_pos = screen_height - (j + 1) * disk_height
            pygame.draw.rect(screen, colors[disk-1], (x_pos, y_pos, disk_width, disk_height))
        pygame.display.flip()
    pygame.time.wait(1500)

# Algoritmo de Torres de Hanói
def hanoi(n, source, target, auxiliary, towers):
    if n == 1:
        towers[target].append(towers[source].pop())
        print_current_state(towers)
        return
    hanoi(n - 1, source, auxiliary, target, towers)
    towers[target].append(towers[source].pop())
    print_current_state(towers)
    hanoi(n - 1, auxiliary, target, source, towers)

# Función para iniciar el juego
def hanoi_game():
    towers = initialize_towers(n)
    print_current_state(towers)
    hanoi(n, 0, 2, 1, towers)
    pygame.time.wait(2000)
    return
    # Espera hasta que se cierre la ventana
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return