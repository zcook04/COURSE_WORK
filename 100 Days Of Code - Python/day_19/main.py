from turtle import Turtle, Screen
import random

turtle_colors = ['red', 'blue', 'green', 'purple', 'pink', 'teal']

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 500
MAX_Y = SCREEN_HEIGHT / 2
MIN_Y = 0 - MAX_Y
MAX_X = SCREEN_WIDTH / 2
MIN_X = 0 - MAX_X


screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)


def get_bet():
    user_bet = screen.textinput(
        title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
    return user_bet


def get_turts(turtle_colors):
    turts = []
    for i, turt in enumerate(turtle_colors):
        color = turt
        turt = Turtle()
        turt.color(color)
        turt.shape('turtle')
        turt.penup()
        turts.append(turt)
    return turts


def position_turts(turtles):
    y_increment = (SCREEN_HEIGHT / (len(turtles)+1))
    starting_y = MIN_Y + y_increment
    starting_x = MIN_X
    for i, turt in enumerate(turtles):
        turt.goto(starting_x, starting_y)
        starting_y += y_increment


def turts_race(turtles: list[Turtle]):
    winner = False
    while not winner:
        for t in turtles:
            t.forward(random.randint(0, 30))
            if t.xcor() >= (MAX_X - 5):
                winner = t.color()[0]
                return winner


def check_bet(b: str, w: str):
    '''b: bet w: winner.  Evaluates if bet == winner'''
    if b == w:
        return True
    else:
        return False


def start_race():
    bet = get_bet()
    turts = get_turts(turtle_colors)
    position_turts(turts)
    winner = turts_race(turts)
    if check_bet(bet, winner):
        print(f'Nice bet! {winner.title()} was impressive this race.')
    else:
        print(
            f'Sorry you bet on {bet.title()} but it seems {winner.title()} was faster.')


start_race()

screen.exitonclick()
