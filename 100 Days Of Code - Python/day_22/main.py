from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')

user_paddle = Paddle()
user_paddle.init_paddle('user')
pc_paddle = Paddle()
pc_paddle.init_paddle('pc')

screen.listen()
screen.onkey(user_paddle.go_up, "Up")
screen.onkey(user_paddle.go_down, "Down")

screen.exitonclick()
