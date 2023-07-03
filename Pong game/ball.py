from turtle import Turtle

class Ball:
    def __init__(self):
        self.create_ball()

    def create_ball(self):
        self.b = Turtle("circle")
        self.b.penup()
        self.b.color("white")
        self.b.turtlesize(1,1)
        self.x_b = 10
        self.y_b = 10


    def refresh(self):
        new_x = self.b.xcor() + self.x_b
        new_y = self.b.ycor() + self.y_b
        self.b.goto(new_x, new_y)

    def refresh_l(self):
        self.b.goto(0,0)
        self.bouce_paddle()


    def bounce(self):
        self.y_b *= -1

    def bouce_paddle(self):
        self.x_b *= -1

