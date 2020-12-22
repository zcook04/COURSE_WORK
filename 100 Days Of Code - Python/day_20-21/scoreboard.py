from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.display_scoreboard()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center',
                   move=False, font=('Arial', 10, 'bold'))

    def display_scoreboard(self):
        self.penup()
        self.goto(0, 275)
        self.write(f'Score: {self.score}', align='center',
                   move=False, font=('Arial', 10, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center',
                   move=False, font=('Arial', 10, 'bold'))
