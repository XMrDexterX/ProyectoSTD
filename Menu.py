# -*- coding: utf-8 -*-
import pygame
import sys
from Torre import hanoi_game
from Maze  import maze_game
from recursividad import busqueda_recursiva

# Inicialización de pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Menu de Inicio')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (11, 79, 108)
DARK_GREY = (11, 79, 108)
BUTTON_COLOR = (11, 79, 108)
BUTTON_HOVER_COLOR = (0, 100, 210)
# Función para mostrar el menú
def show_menu():
    screen.fill(DARK_GREY)
    
    # Dibuja la imagen de fondo
    # screen.blit(background_image, (0, 0))
    
    font = pygame.font.Font(None, 74)
    title = font.render("SELECCIONA UN JUEGO", True, WHITE)
    title_rect = title.get_rect(center=(screen_width // 2, screen_height // 4))
    screen.blit(title, title_rect)
    
    buttons = [
        ("Torres de Hanói", hanoi_game),
        ("Maze Runner", maze_game),
        ("Juego de Recursividad", busqueda_recursiva)]
    button_rects = []

    button_font = pygame.font.Font(None, 50)
    for idx, (btn_text, btn_action) in enumerate(buttons):
        btn_text_surface = button_font.render(btn_text, True, WHITE)
        btn_rect = btn_text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + idx * 80))
        pygame.draw.rect(screen, BUTTON_COLOR, btn_rect.inflate(20, 20))
        pygame.draw.rect(screen, WHITE, btn_rect.inflate(20, 20), 2)  # Border
        screen.blit(btn_text_surface, btn_rect)
        button_rects.append((btn_rect, btn_action))

    pygame.display.flip()
    return button_rects

# Bucle principal del menú de inicio
running = True
while running:
    button_rects = show_menu()
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for btn_rect, btn_action in button_rects:
                    if btn_rect.collidepoint(event.pos):
                        btn_action()
            show_menu() 

if __name__ == "__main__":
    show_menu()