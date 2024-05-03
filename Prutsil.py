import pygame
import Screen
# Прапорці напрямку
UP_LEFT = 7
UP = 8
UP_RIGHT = 9
CENTER = 5
CENTER_LEFT = 4
CENTER_RIGHT = 6
DOWN_LEFT = 1
DOWN = 2
DOWN_RIGHT = 3


class Prutsil:

    def __init__(self):
        self.prutsil = False
        self.circle_color = (214, 214, 214)
        self.ball_direction = CENTER
        # Розмір та положення кола
        self.circle_radius = 21.5
        self.circle_position = (455, 84)
        self.true = True

    def draw_prutsil(self):
        # Оновлення координат м'яча залежно від напрямку удару
        if self.ball_direction == UP_LEFT:
            self.circle_position = (455, 85)
            self.prutsil = self.true
        elif self.ball_direction == UP:
            self.circle_position = (685, 85)
            self.prutsil = self.true
        elif self.ball_direction == UP_RIGHT:
            self.circle_position = (898, 85)
            self.prutsil = self.true
        elif self.ball_direction == CENTER:
            # В центрі не змінюємо координати м'яча
            self.circle_position = (685, 130)
            self.prutsil = self.true
        elif self.ball_direction == CENTER_LEFT:
            self.circle_position = (455, 130)
            self.prutsil = self.true
        elif self.ball_direction == CENTER_RIGHT:
            self.circle_position = (898, 130)
            self.prutsil = self.true
        elif self.ball_direction == DOWN_LEFT:
            self.circle_position = (455, 190)
            self.prutsil = self.true
        elif self.ball_direction == DOWN:
            self.circle_position = (685, 190)
            self.prutsil = self.true
        elif self.ball_direction == DOWN_RIGHT:
            self.circle_position = (898, 190)
            self.prutsil = self.true
        if self.prutsil:
            pygame.draw.circle(Screen.screen, self.circle_color, self.circle_position, self.circle_radius, 6)
            self.prutsil = False
