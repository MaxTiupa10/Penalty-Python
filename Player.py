import pygame
import Screen

class Player:

    def __init__(self):
        self.player_icon = pygame.image.load("фото/Stricker_preview_rev_1.png")  # Спрайт гравця
        self.player_x = 500
        self.player_y = 417
        self.shots_remaining = 5
        self.movemant = []
        for i in range(24):
            a = pygame.image.load(f"фото/Player_Rist/{i+1}plp.png")
            self.movemant.append(a)
        self.current_frame_index = 0  # Індекс поточного кадру
        self.cursor = pygame.image.load("фото/CURSOR.png")

    def draw(self):
        Screen.screen.blit(self.player_icon, (self.player_x, self.player_y))  # Відображення спрайту гравця

    def move(self):
        if self.player_x < 600 and self.player_y > 330:
            self.player_x += 4
            self.player_y -= 3.7
        if self.current_frame_index <= 23:
            self.player_icon = self.movemant[self.current_frame_index]
            self.current_frame_index += 1
        else:
            self.player_icon = pygame.image.load("фото/Stricker_preview_rev_1.png")
            self.shots_remaining -= 1
            return True
