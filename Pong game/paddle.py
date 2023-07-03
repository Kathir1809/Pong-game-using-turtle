from turtle import Turtle
class Paddle:
    def __init__(self,pos):
        self.pos = pos
        self.tr = Turtle("square")
        self.create()

    def create(self):
        self.tr.penup()
        self.tr.color("white")
        self.tr.turtlesize(5,1)
        self.tr.goto(self.pos)

    def move_up(self):
        if self.tr.ycor() != 240:
            new_y = self.tr.ycor() + 20
            self.tr.goto(self.tr.xcor(),new_y)

    def move_down(self):
        if self.tr.ycor() != -240:
            new_y = self.tr.ycor() - 20
            self.tr.goto(self.tr.xcor(), new_y)


