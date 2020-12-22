from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self._init_snake()
        self.head = self.segments[0]

    def _init_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in starting_positions:
            self.add_segment(pos)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, pos):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(pos)
        self.segments.append(snake)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
