from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.direction = 'up'
        self.x_speed = -10
        self.y_speed = 10
        self.shape('circle')
        self.penup()
        self.color('white')

    def start_moving(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        if new_y >= 280 or new_y <= -280:
            self.bounce_y()
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1

    def reset(self):
        self.x_speed = -10
        self.y_speed = 10
        self.setpos(0, 0)
        self.direction = 'up'
