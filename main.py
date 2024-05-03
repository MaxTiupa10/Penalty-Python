import subprocess
import sys
import Goalkeeper
import Ball
import Goal
import Player
from KeyBoard import KeyBoard_ball, KeyBoard_kepper
import Screen
import pygame



score = Goal.Score()

# Головний цикл гри
for game_round in range(5):

    player = Player.Player()
    ball = Ball.Ball()
    goalkeeper = Goalkeeper.Goalkeeper()
    goal = Goal.Goal()
    k = 0
    reset = True

    while reset:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            KeyBoard_ball(ball, event)

        if ball.Shoot:
            if player.move():
                if ball.move():
                    goalkeeper.move()

        Screen.screen.blit(Screen.background, (0, 0))
        goal.draw()
        goalkeeper.draw()
        ball.draw_prutsil()
        ball.draw()
        player.draw()
        if player.player_y == 417:
            Screen.screen.blit(player.cursor, (530, 370))
        score.draw()
        if ball.ball_y != 500 and not ball.Shoot:
            if Goal.check_ball_in_goal(ball.ball_x, ball.ball_y):
                if Goal.check_goalkeeper_ball_collision(goalkeeper, ball):
                    Goal.Animation_Missed("SAVED!")
                    score.my_score[game_round] = 0
                    score.round = game_round
                    k += 1
                    if k > 50:
                        reset = False

                else:
                    Goal.Animation_Goal("GOAL!")
                    score.my_score[game_round] = 1
                    score.round = game_round
                    if k == 0:
                        score.my_sum += 1
                    k += 1
                    if k > 50:
                        reset = False

            else:
                Goal.Animation_Missed("MISSED!")
                score.my_score[game_round] = 0
                score.round = game_round
                k += 1
                if k > 50:
                    reset = False

        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)

    bot_player = Player.Player()
    i_goalkeeper = Goalkeeper.Goalkeeper()
    ball = Ball.Ball()
    k = 0
    reset = True

    while reset:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            KeyBoard_kepper(i_goalkeeper, ball, event)

        if ball.Shoot:
            if bot_player.move():
                if ball.rand_move():
                    i_goalkeeper.i_move()

        Screen.screen.blit(Screen.background, (0, 0))
        goal.draw()
        i_goalkeeper.draw()
        if bot_player.player_y == 417:
            Screen.screen.blit(i_goalkeeper.cursor, (660, 20))
        i_goalkeeper.draw_prutsil()
        ball.draw()
        bot_player.draw()
        score.draw()
        if ball.ball_y != 500 and not ball.Shoot:
            if Goal.check_ball_in_goal(ball.ball_x, ball.ball_y):
                if Goal.check_goalkeeper_ball_collision(i_goalkeeper, ball):
                    Goal.Animation_Goal("SAVED!")
                    score.bot_score[game_round] = 0
                    score.round = game_round
                    k += 1
                    if k > 50:
                        reset = False

                else:
                    Goal.Animation_Missed("GOAL!")
                    score.bot_score[game_round] = 1
                    score.round = game_round
                    if k == 0:
                        score.bot_sum += 1
                    k += 1
                    if k > 50:
                        reset = False

            else:
                Goal.Animation_Goal("MISSED!")
                score.bot_score[game_round] = 0
                score.round = game_round
                k += 1
                if k > 50:
                    reset = False

        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(100)


if score.my_sum > score.bot_sum:
    result = "YOU WIN!"
elif score.my_sum == score.bot_sum:
    result = "DRAW!"
else:
    result = "YOU LOST!"



with open("D:/Курсова/РезультатГриПенальті.txt", mode="w", encoding="utf-8")as file:
    file.write(str(score.my_sum)+' ')
    file.write(str(score.bot_sum)+' ')
    file.write(result)

# Шлях до виконуваного файлу .exe
exe_path = 'D:/vs/Cursova/x64/Debug/Cursova.exe'

# Запуск виконуваного файлу
subprocess.call(exe_path)