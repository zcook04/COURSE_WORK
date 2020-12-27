from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-60, 280)
        self.penup()
        self.color('white')
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0

    def display(self):
        self.write(f'Score: {self.left_score} - {self.right_score}',
                   font=('Arial', 12, 'bold'))

    def increase_score(self, side):
        if side == "left":
            self.left_score += 1
            self.clear()
            self.write(f'Score: {self.left_score} - {self.right_score}',
                       font=('Arial', 12, 'bold'))
        else:
            self.right_score += 1
            self.clear()
            self.write(f'Score: {self.left_score} - {self.right_score}',
                       font=('Arial', 12, 'bold'))
