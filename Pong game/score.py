from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.s_l = 0
        self.s_r = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_Score()


    def update_Score(self):
        self.goto(-100,200)
        self.write(self.s_l,align='center',font=("Arial Black",30,"normal"))
        self.goto(100,200)
        self.write(self.s_r, align='center', font=("Arial Black", 30, "normal"))


    def score_l(self):
        self.s_l += 1
        self.clear()
        self.update_Score()


    def score_r(self):
        self.s_r += 1
        self.clear()
        self.update_Score()
