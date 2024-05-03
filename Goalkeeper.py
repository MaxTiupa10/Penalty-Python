import pygame
from Prutsil import Prutsil
import random
import Screen
from Prutsil import UP_LEFT, UP_RIGHT, CENTER, CENTER_LEFT, CENTER_RIGHT, DOWN_LEFT, DOWN_RIGHT,DOWN,UP


class Goalkeeper(Prutsil):

    def __init__(self):
        super().__init__()
        self.kepper_direction = None
        self.goalkeeper_icon = pygame.image.load("фото/Goalkepper158.png")  # Спрайт воротаря
        self.goalkeeper_x = 631
        self.goalkeeper_y = 63
        self.save_left = []
        self.save_right = []
        self.save_center = []
        for i in range(11):
            a = pygame.image.load(f"фото/Goalkeeper_done/{1+i}ййй-removebg-preview.png")
            self.save_left.append(a)
        for i in range(11):
            b = pygame.image.load(f"фото/Goalkeeper_Right/Goalkepper_Right_{1+i}.png")
            self.save_right.append(b)
        for i in range(6):
            c = pygame.image.load(f"фото/Goalkeeper_Center/center_gk_{i+1}-removebg-preview.png")
            self.save_center.append(c)
        self.current_frame_index = 0  # Індекс поточного кадру
        self.cursor = pygame.image.load("фото/CURSOR.png")

    def draw(self):
        Screen.screen.blit(self.goalkeeper_icon, (self.goalkeeper_x, self.goalkeeper_y))  # Відображення спрайту воротаря

    def move(self):
        if self.goalkeeper_x == 631:
            self.kepper_direction = random.choice([UP_LEFT, UP_RIGHT, CENTER, CENTER_LEFT, CENTER_RIGHT, DOWN_LEFT, DOWN_RIGHT])
        if self.kepper_direction == UP_LEFT:
            if self.goalkeeper_x > 450 or self.goalkeeper_y > 50:
                self.goalkeeper_x -= 18
                self.goalkeeper_y -= 1
                if self.current_frame_index < 10:
                    self.goalkeeper_icon = self.save_left[self.current_frame_index]
                    self.current_frame_index += 1

        elif self.kepper_direction == CENTER_LEFT:
            if self.goalkeeper_x > 450:
                self.goalkeeper_x -= 16
                self.goalkeeper_y += 1.5
                if self.current_frame_index < 11:
                    self.goalkeeper_icon = self.save_left[self.current_frame_index]
                    self.current_frame_index += 1

        elif self.kepper_direction == DOWN_LEFT:
            if self.goalkeeper_x > 450:
                self.goalkeeper_x -= 16
                self.goalkeeper_y += 7
                if self.current_frame_index < 11:
                    self.goalkeeper_icon = self.save_left[self.current_frame_index]
                    self.current_frame_index += 1

        elif self.kepper_direction == UP_RIGHT:
            if self.goalkeeper_x < 740 and self.goalkeeper_y > 50:
                self.goalkeeper_x += 8
                self.goalkeeper_y -= 1
                if self.current_frame_index < 10:
                    self.goalkeeper_icon = self.save_right[self.current_frame_index]
                    self.current_frame_index += 1

        elif self.kepper_direction == CENTER_RIGHT:
            if self.goalkeeper_x < 740:
                self.goalkeeper_x += 9
                self.goalkeeper_y += 1.5
                if self.current_frame_index < 11:
                    self.goalkeeper_icon = self.save_right[self.current_frame_index]
                    self.current_frame_index += 1

        elif self.kepper_direction == DOWN_RIGHT:
            if self.goalkeeper_x < 740:
                self.goalkeeper_x += 10
                self.goalkeeper_y += 7
                if self.current_frame_index < 11:
                    self.goalkeeper_icon = self.save_right[self.current_frame_index]
                    self.current_frame_index += 1

        elif self.kepper_direction == CENTER:
            if self.goalkeeper_y > 55:
                self.goalkeeper_y -= 1
                self.goalkeeper_x += 1
                if self.current_frame_index < 6:
                    self.goalkeeper_icon = self.save_center[self.current_frame_index]
                    self.current_frame_index += 1

    def i_move(self):
        if self.goalkeeper_y == 63:
            self.kepper_direction = self.ball_direction
        if self.kepper_direction == UP_LEFT:
            if self.goalkeeper_x > 450 or self.goalkeeper_y > 50:
                self.goalkeeper_x -= 18
                self.goalkeeper_y -= 1
                if self.current_frame_index < 10:
                    self.goalkeeper_icon = self.save_left[self.current_frame_index]
                    self.current_frame_index += 1

        elif self.kepper_direction == CENTER_LEFT:
            if self.goalkeeper_x > 450:
                self.goalkeeper_x -= 16
                self.goalkeeper_y += 1.5
                if self.current_frame_index < 11:
                    self.goalkeeper_icon = self.save_left[self.current_frame_index]
                    self.current_frame_index += 1

        elif self.kepper_direction == DOWN_LEFT:
            if self.goalkeeper_x > 450:
                self.goalkeeper_x -= 16
                self.goalkeeper_y += 7
                if self.current_frame_index < 11:
                    self.goalkeeper_icon = self.save_left[self.current_frame_index]
                    self.current_frame_index += 1

        elif self.kepper_direction == UP_RIGHT:
            if self.goalkeeper_x < 740 and self.goalkeeper_y > 50:
                self.goalkeeper_x += 8
                self.goalkeeper_y -= 1
                if self.current_frame_index < 10:
                    self.goalkeeper_icon = self.save_right[self.current_frame_index]
                    self.current_frame_index += 1

        elif self.kepper_direction == CENTER_RIGHT:
            if self.goalkeeper_x < 740:
                self.goalkeeper_x += 9
                self.goalkeeper_y += 1.5
                if self.current_frame_index < 11:
                    self.goalkeeper_icon = self.save_right[self.current_frame_index]
                    self.current_frame_index += 1

        elif self.kepper_direction == DOWN_RIGHT:
            if self.goalkeeper_x < 740:
                self.goalkeeper_x += 10
                self.goalkeeper_y += 7
                if self.current_frame_index < 11:
                    self.goalkeeper_icon = self.save_right[self.current_frame_index]
                    self.current_frame_index += 1

        elif self.kepper_direction == CENTER or self.kepper_direction == UP or self.kepper_direction == DOWN:
            if self.goalkeeper_y > 55:
                self.goalkeeper_y -= 1
                self.goalkeeper_x += 1
                if self.current_frame_index < 6:
                    self.goalkeeper_icon = self.save_center[self.current_frame_index]
                    self.current_frame_index += 1
