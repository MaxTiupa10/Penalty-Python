
import pygame

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

def KeyBoard_ball(ball,event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            ball.ball_direction = UP_LEFT
        elif event.key == pygame.K_w:
            ball.ball_direction = UP
        elif event.key == pygame.K_e:
            ball.ball_direction = UP_RIGHT
        elif event.key == pygame.K_s:
            ball.ball_direction = CENTER
        elif event.key == pygame.K_a:
            ball.ball_direction = CENTER_LEFT
        elif event.key == pygame.K_d:
            ball.ball_direction = CENTER_RIGHT
        elif event.key == pygame.K_c:
            ball.ball_direction = DOWN_RIGHT
        elif event.key == pygame.K_x:
            ball.ball_direction = DOWN
        elif event.key == pygame.K_z:
            ball.ball_direction = DOWN_LEFT
        if event.key == pygame.K_RETURN:
            ball.Shoot = True
            ball.true = False



def KeyBoard_kepper(goalkeeper,ball,event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            goalkeeper.ball_direction = UP_LEFT
        elif event.key == pygame.K_w:
            goalkeeper.ball_direction = UP
        elif event.key == pygame.K_e:
            goalkeeper.ball_direction = UP_RIGHT
        elif event.key == pygame.K_s:
            goalkeeper.ball_direction = CENTER
        elif event.key == pygame.K_a:
            goalkeeper.ball_direction = CENTER_LEFT
        elif event.key == pygame.K_d:
            goalkeeper.ball_direction = CENTER_RIGHT
        elif event.key == pygame.K_c:
            goalkeeper.ball_direction = DOWN_RIGHT
        elif event.key == pygame.K_x:
            goalkeeper.ball_direction = DOWN
        elif event.key == pygame.K_z:
            goalkeeper.ball_direction = DOWN_LEFT
        if event.key == pygame.K_RETURN:
            ball.Shoot = True
            goalkeeper.true = False