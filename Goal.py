import KeyBoard
import pygame.time
import Screen
import time

class Goal:

    def __init__(self):
        self.goal_icon = pygame.Rect(420, 50, 513, 170)
        self.goal_x = 631
        self.goal_y = 63

    def draw(self):
        pygame.draw.rect(Screen.screen, (255, 255, 255), self.goal_icon, 10)


class Score:
    def __init__(self):
        self.round = 0
        self.my_score = [2, 2, 2, 2, 2]
        self.bot_score = [2, 2, 2, 2, 2]
        self.yes = pygame.image.load("фото/Забиті незабиті/забитий.png")
        self.no = pygame.image.load("фото/Забиті незабиті/незабитий.png")
        self.my_score_icon = pygame.image.load("фото/Забиті незабиті/ліво.png")
        self.bot_score_icon = pygame.image.load("фото/Забиті незабиті/право.png")
        self.my_sum = 0
        self.bot_sum = 0

    def draw(self):
        Screen.screen.blit(self.my_score_icon, (-52,15))
        Screen.screen.blit(self.bot_score_icon, (1038,15))
        if self.round >= 0:
            if self.bot_score[0] == 0:
                Screen.screen.blit(self.no, (1110, 51))
            elif self.bot_score[0] == 1:
                Screen.screen.blit(self.yes, (1110, 51))
        if self.round >= 1:
            if self.bot_score[1] == 0:
                Screen.screen.blit(self.no, (1160, 51))
            elif self.bot_score[1] == 1:
                Screen.screen.blit(self.yes, (1160, 51))
        if self.round >= 2:
            if self.bot_score[2] == 0:
                Screen.screen.blit(self.no, (1210, 51))
            elif self.bot_score[2] == 1:
                Screen.screen.blit(self.yes, (1210, 51))
        if self.round >= 3:
            if self.bot_score[3] == 0:
                Screen.screen.blit(self.no, (1260, 51))
            elif self.bot_score[3] == 1:
                Screen.screen.blit(self.yes, (1260, 51))
        if self.round >= 4:
            if self.bot_score[4] == 0:
                Screen.screen.blit(self.no, (1310, 51))
            elif self.bot_score[4] == 1:
                Screen.screen.blit(self.yes, (1310, 51))
        if self.round >= 0:
            if self.my_score[0] == 0:
                Screen.screen.blit(self.no, (5, 51))
            elif self.my_score[0] == 1:
                Screen.screen.blit(self.yes, (5, 51))
        if self.round >= 1:
            if self.my_score[1] == 0:
                Screen.screen.blit(self.no, (55, 51))
            elif self.my_score[1] == 1:
                Screen.screen.blit(self.yes, (55, 51))
        if self.round >= 2:
            if self.my_score[2] == 0:
                Screen.screen.blit(self.no, (105, 51))
            elif self.my_score[2] == 1:
                Screen.screen.blit(self.yes, (105, 51))
        if self.round >= 3:
            if self.my_score[3] == 0:
                Screen.screen.blit(self.no, (155, 51))
            elif self.my_score[3] == 1:
                Screen.screen.blit(self.yes, (155, 51))
        if self.round >= 4:
            if self.my_score[4] == 0:
                Screen.screen.blit(self.no, (205, 51))
            elif self.my_score[4] == 1:
                Screen.screen.blit(self.yes, (205, 51))


def Animation_Goal(caption):
    # Колір тексту
    text_color = (255, 255, 255)
    # Кольори для переливання
    gradient_colors = [
        (255, 0, 0), (255, 63, 0), (255, 127, 0), (255, 191, 0), (255, 255, 0),
        (191, 255, 0), (127, 255, 0), (63, 255, 0), (0, 255, 0), (0, 255, 63),
        (0, 255, 127), (0, 255, 191), (0, 255, 255), (0, 191, 255), (0, 127, 255),
        (0, 63, 255), (0, 0, 255), (63, 0, 255), (127, 0, 255), (191, 0, 255),
        (255, 0, 255), (255, 0, 191), (255, 0, 127), (255, 0, 63), (255, 0, 0)
    ]
    # Шрифт тексту
    font = pygame.font.SysFont(None, 200)  # Встановіть потрібний шрифт і розмір
    # Текст "ГОЛ"
    text = font.render(caption, True, text_color)
    # Початкові координати тексту
    text_x = (1336 - text.get_width()) // 2
    text_y = (759 - text.get_height()) // 2
    # Зміна кольору тексту
    current_color_index = int(time.time() * 10) % len(gradient_colors)  # Змінюємо колір кожну 0.1 секунди
    current_color = gradient_colors[current_color_index]# Змінюємо колір кожні 0.5 секунди
    text = font.render(caption, True, current_color)
    Screen.screen.blit(text, (text_x, text_y))


def Animation_Missed(caption):
    text_color = (255, 255, 255)
    # Кольори для перетікання
    gradient_colors = [
        (255, 0, 0), (255, 63, 0), (255, 127, 0), (255, 191, 0), (255, 255, 0),
        # Ви можете додати інші кольори за бажанням
        (191, 255, 0), (127, 255, 0), (63, 255, 0), (0, 255, 0), (0, 255, 63),
        (0, 255, 127), (0, 255, 191), (0, 255, 255), (0, 191, 255), (0, 127, 255),
        (0, 63, 255), (0, 0, 255), (63, 0, 255), (127, 0, 255), (191, 0, 255),
        (255, 0, 255), (255, 0, 191), (255, 0, 127), (255, 0, 63), (255, 0, 0)
    ]
    # Шрифт тексту
    font = pygame.font.SysFont(None, 200)  # Встановіть потрібний шрифт і розмір
    text = font.render(caption, True, (255, 0, 0))
    text_x = (1336 - text.get_width()) // 2
    text_y = (759 - text.get_height()) // 2
    pygame.display.update()
    # Відображення тексту червоним кольором
    text = font.render(caption, True, (255, 0, 0))
    Screen.screen.blit(text, (text_x, text_y))
    pygame.display.update()
    # Очистка екрану
    pygame.display.update()

def check_ball_in_goal(ball_x, ball_y):
    if 50 <= ball_y <= 200 and 420 <= ball_x <= 890:
        return True
    else:
        return False

def check_goalkeeper_ball_collision(goalkeeper, ball):
    goalkeeper_mask = pygame.mask.from_surface(goalkeeper.goalkeeper_icon)
    ball_mask = pygame.mask.from_surface(ball.ball_icon)

    offset = (ball.ball_x - goalkeeper.goalkeeper_x, ball.ball_y - goalkeeper.goalkeeper_y)

    if goalkeeper_mask.overlap(ball_mask, offset):
        return True
    else:
        return False
