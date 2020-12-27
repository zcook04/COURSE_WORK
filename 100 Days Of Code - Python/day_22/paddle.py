from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, player_paddle):
        super().__init__()
        self.init_paddle(player_paddle)

    def init_paddle(self, player):
        self.penup()
        self.shape(name='square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        if player == 'user':
            self.setposition(x=-350, y=0)
        if player == 'pc':
            self.setposition(x=350, y=0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor()-20)
