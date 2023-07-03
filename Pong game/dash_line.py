from turtle import Turtle

class Dash(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,300)
        self.right(90)
        for i in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
