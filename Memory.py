import pygame
import random
import sys

def memory_game():
    # Inicialización de pygame
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Juego de Memoria')

    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (192, 192, 192)
    colors = [
        (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
        (255, 165, 0), (128, 0, 128), (165, 42, 42), (255, 192, 203)
    ]

    # Parámetros de las cartas
    rows, cols = 4, 4
    padding = 10
    card_width = (screen_width - (cols + 1) * padding) // cols
    card_height = (screen_height - (rows + 1) * padding) // rows

    # Función para crear pares de cartas
    def create_pairs():
        items = list(range(1, 9)) * 2
        random.shuffle(items)
        return items

    # Función para dibujar el tablero
    def draw_board(board, revealed):
        screen.fill(GREY)
        for i in range(rows):
            for j in range(cols):
                index = i * cols + j
                x = j * (card_width + padding) + padding
                y = i * (card_height + padding) + padding

                if revealed[index]:
                    pygame.draw.rect(screen, colors[board[index] - 1], (x, y, card_width, card_height))
                    font = pygame.font.Font(None, 74)
                    text = font.render(str(board[index]), True, BLACK)
                    screen.blit(text, (x + card_width // 2 - text.get_width() // 2, y + card_height // 2 - text.get_height() // 2))
                else:
                    pygame.draw.rect(screen, WHITE, (x, y, card_width, card_height))
                    pygame.draw.rect(screen, BLACK, (x, y, card_width, card_height), 2)

        pygame.display.flip()

    # Función para mostrar un mensaje con botones
    def display_message(message, buttons=None):
        screen.fill(GREY)
        font = pygame.font.Font(None, 74)
        text = font.render(message, True, BLACK)
        rect = text.get_rect(center=(screen_width // 2, screen_height // 3))
        screen.blit(text, rect)

        button_rects = []
        if buttons:
            button_font = pygame.font.Font(None, 50)
            for idx, (btn_text, btn_action) in enumerate(buttons):
                btn_text_surface = button_font.render(btn_text, True, WHITE)
                btn_rect = btn_text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + idx * 100))
                pygame.draw.rect(screen, BLACK, btn_rect.inflate(20, 20))
                screen.blit(btn_text_surface, btn_rect)
                button_rects.append((btn_rect, btn_action))

        pygame.display.flip()
        return button_rects

    # Lógica principal del juego
    def play_game():
        board = create_pairs()
        revealed = [False] * 16
        attempts = 0

        running = True
        first_choice = None

        while running:
            draw_board(board, revealed)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y // (card_height + padding)
                    col = x // (card_width + padding)
                    guess = row * cols + col

                    if 0 <= guess < 16 and not revealed[guess]:
                        if first_choice is None:
                            first_choice = guess
                            revealed[first_choice] = True
                        else:
                            revealed[guess] = True
                            draw_board(board, revealed)
                            pygame.time.wait(1000)  # Esperar 1 segundo
                            if board[first_choice] != board[guess]:
                                revealed[first_choice] = False
                                revealed[guess] = False
                            else:
                                print("¡Encontraste una pareja!")
                            first_choice = None
                            attempts += 1

                        if all(revealed):
                            display_message(f"¡Lo lograste en {attempts} intentos!")
                            pygame.time.wait(2000)  # Esperar 2 segundos
                            return

    # Repetir el juego según la selección del usuario
    while True:
        play_game()
        buttons = display_message("¿Jugar de nuevo?", [("Sí", True), ("No", False)])

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for btn_rect, btn_action in buttons:
                        if btn_rect.collidepoint(event.pos):
                            if btn_action:
                                waiting_for_input = False
                            else:
                                pygame.quit()
                                sys.exit()
