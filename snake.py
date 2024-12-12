from turtle import *
STARTING_POSITION  =[(0,0),(-15,0),(-30,0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.t =[]
        self.createsnake()
        self.head = self.t[0]

    def createsnake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self,i):
        new = Turtle("square")
        new.color("white")
        new.shapesize(stretch_wid=0.75, stretch_len=0.75)
        new.penup()
        new.setpos(i)
        self.t.append(new)

    def extend(self):
        self.add_segment(self.t[-1].position())

    def move(self):
        for i in range(len(self.t) - 1, 0, -1):
            new_x = self.t[i - 1].xcor()
            new_y = self.t[i - 1].ycor()
            self.t[i].goto(new_x, new_y)
        self.t[0].forward(MOVE_DISTANCE)

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

