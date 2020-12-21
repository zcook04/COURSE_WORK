from turtle import Turtle, Screen, colormode
import random

rgb_colors = [(198, 12, 32), (250, 237, 17), (39, 76, 189),
              (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157)]


zack = Turtle()
zack.shape('turtle')
zack.speed(0)
colormode(255)
zack.pensize(20)


def random_rgb():
    return (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))


def draw_shape(sides, side_len=100):
    angle = 360/sides
    zack.pencolor(random_rgb())
    for _ in range(sides):
        zack.forward(side_len)
        zack.right(angle)


def rand_walk(total_distance, segment_distance):
    while total_distance > 0:
        angle = random.choice([0, 90, 180, 270])
        zack.pencolor(random_rgb())
        zack.right(angle)
        zack.forward(segment_distance)
        total_distance -= segment_distance


def draw_spiral_graph(radius):
    heading = 0
    while heading <= 360:
        zack.pencolor(random_rgb())
        zack.circle(radius)
        zack.setheading(heading)
        heading += 1


def draw_hirst(row_dots, col_dots, distance, colors):
    zack.penup()
    x_start = zack.xcor()
    y_start = zack.ycor()
    new_y = y_start
    for col in range(col_dots):
        for dot in range(row_dots):
            zack.pencolor(random.choice(colors))
            zack.dot()
            zack.forward(distance)
            new_y += 5
        zack.goto((x_start, new_y))


draw_hirst(20, 10, 10, 50, rgb_colors)


# Keep screen open until clicked
screen = Screen()
screen.exitonclick()
