from Prutsil import Prutsil
import pygame
import random
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



class Ball(Prutsil):

    def __init__(self):
        super().__init__()
        self.ball_icon = pygame.image.load("фото/ball_43.png")  # Спрайт м'яча
        self.ball_x = 662
        self.ball_y = 500
        self.ball_speed = 20
        self.Shoot = False
        self.Hit = None

    def draw(self):
        Screen.screen.blit(self.ball_icon, (self.ball_x, self.ball_y))  # Відображення спрайту воротаря

    def move(self):
        if self.Shoot:
            if self.ball_y == 500:
                self.Hit = random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1])
            if self.Hit == 1:
                if self.ball_direction == UP_LEFT:
                    if self.ball_x >= 400 and self.ball_y >= 70:
                        self.ball_x -= self.ball_speed*1.05
                        self.ball_y -= self.ball_speed*2
                    else:
                        self.Shoot = False
                elif self.ball_direction == UP:
                    if self.ball_y >= 66:
                        self.ball_y -= self.ball_speed*2
                    else:
                        self.Shoot = False
                elif self.ball_direction == UP_RIGHT:
                    if self.ball_y >= 66:
                        self.ball_x += self.ball_speed
                        self.ball_y -= self.ball_speed*2
                    else:
                        self.Shoot = False
                elif self.ball_direction == CENTER:
                    # В центрі не змінюємо координати м'яча
                    if self.ball_y >= 110:
                        self.ball_y -= self.ball_speed*1.8
                    else:
                        self.Shoot = False
                elif self.ball_direction == CENTER_LEFT:
                    if self.ball_y >= 130:
                        self.ball_x -= self.ball_speed*1.05
                        self.ball_y -= self.ball_speed*1.75
                    else:
                        self.Shoot = False
                elif self.ball_direction == CENTER_RIGHT:
                    if self.ball_x >= 400 and self.ball_y >= 130:
                        self.ball_x += self.ball_speed
                        self.ball_y -= self.ball_speed * 1.75
                    else:
                        self.Shoot = False
                elif self.ball_direction == DOWN_LEFT:
                    if self.ball_y >= 180 and self.ball_x >= 400:
                        self.ball_x -= self.ball_speed*1.05
                        self.ball_y -= self.ball_speed*1.5
                    else:
                        self.Shoot = False
                elif self.ball_direction == DOWN:
                    if self.ball_y >= 195:
                        self.ball_y -= self.ball_speed*1.5
                    else:
                        self.Shoot = False
                elif self.ball_direction == DOWN_RIGHT:
                    if self.ball_y >= 200:
                        self.ball_x += self.ball_speed
                        self.ball_y -= self.ball_speed*1.5
                    else:
                        self.Shoot = False
                return True
            else:
                if self.ball_direction == UP_LEFT:
                    if self.ball_x >= 250 and self.ball_y >= 35:
                        self.ball_x -= self.ball_speed*1.05
                        self.ball_y -= self.ball_speed*2.5
                    else:
                        self.Shoot = False
                elif self.ball_direction == UP:
                    if self.ball_y >= 35:
                        self.ball_y -= self.ball_speed*2
                    else:
                        self.Shoot = False
                elif self.ball_direction == UP_RIGHT:
                    if self.ball_y >= 35:
                        self.ball_x += self.ball_speed
                        self.ball_y -= self.ball_speed*2.5
                    else:
                        self.Shoot = False
                elif self.ball_direction == CENTER:
                    # В центрі не змінюємо координати м'яча
                    if self.ball_y >= 110:
                        self.ball_y -= self.ball_speed*1.8
                    else:
                        self.Shoot = False
                elif self.ball_direction == CENTER_LEFT:
                    if self.ball_y >= 130:
                        self.ball_x -= self.ball_speed* 1.4
                        self.ball_y -= self.ball_speed*1.75
                    else:
                        self.Shoot = False
                elif self.ball_direction == CENTER_RIGHT:
                    if self.ball_x >= 400 and self.ball_y >= 130:
                        self.ball_x += self.ball_speed * 1.4
                        self.ball_y -= self.ball_speed * 1.75
                    else:
                        self.Shoot = False
                elif self.ball_direction == DOWN_LEFT:
                    if self.ball_y >= 180 and self.ball_x >= 300:
                        self.ball_x -= self.ball_speed*1.5
                        self.ball_y -= self.ball_speed*1.5
                    else:
                        self.Shoot = False
                elif self.ball_direction == DOWN:
                    if self.ball_y >= 195:
                        self.ball_y -= self.ball_speed*1.5
                    else:
                        self.Shoot = False
                elif self.ball_direction == DOWN_RIGHT:
                    if self.ball_y >= 200:
                        self.ball_x += self.ball_speed*1.5
                        self.ball_y -= self.ball_speed*1.5
                    else:
                        self.Shoot = False
                return True


    def rand_move(self):
        if self.Shoot:
            if self.ball_y == 500:
                self.ball_direction = random.choice([UP_LEFT, UP, UP_RIGHT, CENTER, CENTER_LEFT, CENTER_RIGHT, DOWN_LEFT, DOWN, DOWN_RIGHT])
                self.Hit = random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1])
            if self.Hit == 1:
                if self.ball_direction == UP_LEFT:
                    if self.ball_x >= 400 and self.ball_y >= 70:
                        self.ball_x -= self.ball_speed * 1.05
                        self.ball_y -= self.ball_speed * 2
                    else:
                        self.Shoot = False
                elif self.ball_direction == UP:
                    if self.ball_y >= 66:
                        self.ball_y -= self.ball_speed * 2
                    else:
                        self.Shoot = False
                elif self.ball_direction == UP_RIGHT:
                    if self.ball_y >= 66:
                        self.ball_x += self.ball_speed
                        self.ball_y -= self.ball_speed * 2
                    else:
                        self.Shoot = False
                elif self.ball_direction == CENTER:
                    # В центрі не змінюємо координати м'яча
                    if self.ball_y >= 110:
                        self.ball_y -= self.ball_speed * 1.8
                    else:
                        self.Shoot = False
                elif self.ball_direction == CENTER_LEFT:
                    if self.ball_y >= 130:
                        self.ball_x -= self.ball_speed * 1.05
                        self.ball_y -= self.ball_speed * 1.75
                    else:
                        self.Shoot = False
                elif self.ball_direction == CENTER_RIGHT:
                    if self.ball_x >= 400 and self.ball_y >= 130:
                        self.ball_x += self.ball_speed
                        self.ball_y -= self.ball_speed * 1.75
                    else:
                        self.Shoot = False
                elif self.ball_direction == DOWN_LEFT:
                    if self.ball_y >= 180 and self.ball_x >= 400:
                        self.ball_x -= self.ball_speed * 1.05
                        self.ball_y -= self.ball_speed * 1.5
                    else:
                        self.Shoot = False
                elif self.ball_direction == DOWN:
                    if self.ball_y >= 195:
                        self.ball_y -= self.ball_speed * 1.5
                    else:
                        self.Shoot = False
                elif self.ball_direction == DOWN_RIGHT:
                    if self.ball_y >= 200:
                        self.ball_x += self.ball_speed
                        self.ball_y -= self.ball_speed * 1.5
                    else:
                        self.Shoot = False
                return True
            else:
                if self.ball_direction == UP_LEFT:
                    if self.ball_x >= 250 and self.ball_y >= 35:
                        self.ball_x -= self.ball_speed*1.05
                        self.ball_y -= self.ball_speed*2.5
                    else:
                        self.Shoot = False
                elif self.ball_direction == UP:
                    if self.ball_y >= 35:
                        self.ball_y -= self.ball_speed*2
                    else:
                        self.Shoot = False
                elif self.ball_direction == UP_RIGHT:
                    if self.ball_y >= 35:
                        self.ball_x += self.ball_speed
                        self.ball_y -= self.ball_speed*2.5
                    else:
                        self.Shoot = False
                elif self.ball_direction == CENTER:
                    # В центрі не змінюємо координати м'яча
                    if self.ball_y >= 110:
                        self.ball_y -= self.ball_speed*1.8
                    else:
                        self.Shoot = False
                elif self.ball_direction == CENTER_LEFT:
                    if self.ball_y >= 130:
                        self.ball_x -= self.ball_speed* 1.4
                        self.ball_y -= self.ball_speed*1.75
                    else:
                        self.Shoot = False
                elif self.ball_direction == CENTER_RIGHT:
                    if self.ball_x >= 400 and self.ball_y >= 130:
                        self.ball_x += self.ball_speed * 1.4
                        self.ball_y -= self.ball_speed * 1.75
                    else:
                        self.Shoot = False
                elif self.ball_direction == DOWN_LEFT:
                    if self.ball_y >= 180 and self.ball_x >= 300:
                        self.ball_x -= self.ball_speed*1.5
                        self.ball_y -= self.ball_speed*1.5
                    else:
                        self.Shoot = False
                elif self.ball_direction == DOWN:
                    if self.ball_y >= 195:
                        self.ball_y -= self.ball_speed*1.5
                    else:
                        self.Shoot = False
                elif self.ball_direction == DOWN_RIGHT:
                    if self.ball_y >= 200:
                        self.ball_x += self.ball_speed*1.5
                        self.ball_y -= self.ball_speed*1.5
                    else:
                        self.Shoot = False
                return True

