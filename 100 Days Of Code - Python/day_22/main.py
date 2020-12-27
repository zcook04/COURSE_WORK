from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.bgcolor('black')
screen.setup(width=WIDTH, height=HEIGHT)
screen.title('Pong')
screen.tracer(0)

user_paddle = Paddle('user')
pc_paddle = Paddle('pc')
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(user_paddle.go_up, "Up")
screen.onkey(user_paddle.go_down, "Down")
screen.onkey(pc_paddle.go_up, 'Left')
screen.onkey(pc_paddle.go_down, 'Right')


sleep_time = .1
game_on = True
while game_on:
    screen.update()
    scoreboard.display()
    time.sleep(sleep_time)
    ball.start_moving()

    # Detect Paddle Collision With Ball
    if ball.distance(user_paddle) < 60 and ball.xcor() < -320 and ball.x_speed < 0:
        ball.bounce_x()
        sleep_time -= .005
    elif ball.distance(pc_paddle) < 60 and ball.xcor() > 320 and ball.x_speed > 0:
        ball.bounce_x()
        sleep_time -= .005

    # Detect Out Of Bounds
    if ball.xcor() >= 390:
        scoreboard.increase_score('left')
        ball.reset()
        sleep_time = .1
        continue

    if ball.xcor() <= -390:
        scoreboard.increase_score('right"')
        ball.reset()
        sleep_time = .1
        continue


screen.exitonclick()
