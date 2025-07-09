# start_screen.py

import pygame
import sys

def start_menu(screen, clock):
    pygame.font.init()
    font = pygame.font.SysFont(None, 48)

    menu_options = ["▶ Start Game", "❌ Exit"]
    selected_index = 0

    running = True
    while running:
        screen.fill((20, 20, 30))
        title = font.render("TURN-BASED GAME", True, (255, 255, 255))
        screen.blit(title, (screen.x / 2, screen.y / 2))

        for i, option in enumerate(menu_options):
            color = (255, 255, 0) if i == selected_index else (150, 150, 150)
            text = font.render(option, True, color)
            screen.blit(text, (300, 220 + i * 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(menu_options)

                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(menu_options)

                elif event.key == pygame.K_RETURN:
                    if selected_index == 0:
                        return "start"
                    elif selected_index == 1:
                        pygame.quit(); sys.exit()

        pygame.display.flip()
        clock.tick(60)
