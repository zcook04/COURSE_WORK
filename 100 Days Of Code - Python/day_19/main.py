from turtle import Turtle, Screen

turtle_colors = ['red', 'blue', 'green', 'purple', 'pink', 'teal']

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 500
MAX_Y = SCREEN_HEIGHT / 2
MIN_Y = 0 - MAX_Y
MAX_X = SCREEN_WIDTH / 2
MIN_X = 0 - MAX_X


screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color:")


def get_turts(turtle_colors):
    turts = []
    for i, turt in enumerate(turtle_colors):
        name = Turtle()
        name.color(turt)
        name.shape('turtle')
        turts.append(name)
    return turts


def position_turts(turtles):
    starting_y = 0-(SCREEN_HEIGHT / len(turtles) + 1)
    y_increment = (SCREEN_HEIGHT / len(turtles)+1)
    starting_x = MIN_X
    for i, turt in enumerate(turtles):
        print(starting_x, starting_y)
        turt.goto(starting_x, starting_y)
        starting_y += y_increment


turts = get_turts(turtle_colors)
position_turts(turts)

print(turts)

screen.exitonclick()
