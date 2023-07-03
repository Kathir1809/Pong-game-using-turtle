from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
from dash_line import Dash


screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

pd_r = Paddle((370,0))
pd_l = Paddle((-380,0))

dash = Dash()
tur = Turtle()
screen.update()
ball = Ball()


score = Score()
ti = 0.1

screen.listen()
screen.onkey(pd_r.move_up, "Up")
screen.onkey(pd_r.move_down, "Down")
screen.onkey(pd_l.move_up, "w")
screen.onkey(pd_l.move_down, "s")

game = True
while game:
    time.sleep(ti)
    screen.update()
    ball.refresh()

    if ball.b.ycor() > 280 or ball.b.ycor() < -280:
        ball.bounce()


    if ball.b.distance(pd_r.tr) < 50 and ball.b.xcor() > 340:
        ball.bouce_paddle()
        score.score_r()
        ti *= 0.9


    if ball.b.distance(pd_l.tr) < 50 and ball.b.xcor() < -340:
        ball.bouce_paddle()
        score.score_l()
        ti *= 0.9


    if ball.b.xcor() > 420:
        ball.refresh_l()
        ti = 0.1

    if ball.b.xcor() < -420:
        ball.refresh_l()
        ti = 0.1


screen.exitonclick()