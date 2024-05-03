import pygame

# Ініціалізація Pygame
pygame.init()
# Розміри вікна
screen_width = 1366
screen_height = 742

# Створення вікна гри
icon_image = pygame.image.load("фото/football_icon.png")
pygame.display.set_icon(icon_image)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Серія Пенальті")


background = pygame.image.load("фото/45.jpg")  # Фоновий спрайт

