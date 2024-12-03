import pygame
import sys
from Torre import hanoi_game
from Maze  import maze_game
from Memory import memory_game

# Inicialización de pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Menú de Inicio')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (192, 192, 192)

# Función para mostrar el menú
def show_menu():
    screen.fill(GREY)
    font = pygame.font.Font(None, 74)
    title = font.render("Selecciona un juego", True, BLACK)
    title_rect = title.get_rect(center=(screen_width//2, screen_height//3))
    screen.blit(title, title_rect)
    
    buttons = [
        ("Torres de Hanói", hanoi_game),
        ("Maze Runner", maze_game),
        ("Juego de Memoria", memory_game)
    ]
    button_rects = []

    button_font = pygame.font.Font(None, 50)
    for idx, (btn_text, btn_action) in enumerate(buttons):
        btn_text_surface = button_font.render(btn_text, True, WHITE)
        btn_rect = btn_text_surface.get_rect(center=(screen_width//2, screen_height//2 + idx * 100))
        pygame.draw.rect(screen, BLACK, btn_rect.inflate(20, 20))
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
