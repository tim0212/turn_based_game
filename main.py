import screen
import pygame

pygame.init()

# 예: 중앙에 글자 띄우기
font = pygame.font.SysFont(None, 48)
text = font.render("Hello", True, (255, 255, 255))
rect = text.get_rect(center=(screen.cx, screen.cy))
screen.blit(text, rect)