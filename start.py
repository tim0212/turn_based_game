# start_screen.py
import pygame, sys
import screen

def start_menu(scence):
    pygame.init()

    pygame.mixer.music.load(r"sound\Coin 1.mp3")  # 슬래시 `/` 또는 이스케이프 `\\` 사용
    pygame.mixer.music.play()

    font = pygame.font.SysFont(None, 48)
    fy = font.get_height()

    menu_options = ["-> Start Game", "X Exit"] #▶ ❌
    selected_index = 0

    while scence == "start_menu":
        screen.init_display()

        title = font.render("TURN-BASED GAME", True, (255, 255, 255))
        screen.screen.blit(title, (screen.x / 2, screen.y / 2 - fy))

        for i, option in enumerate(menu_options):
            color = (255, 255, 0) if i == selected_index else (150, 150, 150)
            text = font.render(option, True, color)
            screen.screen.blit(text, (screen.x / 4, screen.y / 2 - fy * 2 + i * 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                screen.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(menu_options)

                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(menu_options)

                elif event.key == pygame.K_RETURN:
                    if selected_index == 0:
                        screen.screen.fill((20, 20, 30))
                        return "start"

                    elif selected_index == 1:
                        screen.exit()

        screen.update()
