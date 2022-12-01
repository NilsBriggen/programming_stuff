from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from random import randint

score = Score()
paddle = Paddle()
screen = Screen()
BALL = Ball()
SPEED = 1

screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor('black')
screen.title("Cyberpong 2077")

screen.listen()
screen.onkey(paddle.move_up1, "Up")
screen.onkey(paddle.move_down1, "Down")
screen.onkey(paddle.move_up2, "w")
screen.onkey(paddle.move_down2, "s")

coin_flip = randint(1, 2)

if coin_flip == 1:
    BALL.ball.seth(randint(-135, -45))

if coin_flip == 2:
    BALL.ball.seth(randint(45, 135))

while True:
    if BALL.ball.ycor() > 290 or BALL.ball.ycor() < -290:
        BALL.reboundy()

    if BALL.ball.xcor() > 360:
        score.update_paddle1()
        BALL.reset1()

    if BALL.ball.xcor() < -360:
        score.update_paddle2()
        BALL.reset2()

    if BALL.ball.xcor() > 330:
        for obj in paddle.paddle1:
            if obj.distance(BALL.ball) < 20:
                BALL.reboundx()
            else:
                BALL.ball.fd(SPEED)
                Screen().update()

    elif BALL.ball.xcor() < -330:
        for obj2 in paddle.paddle2:
            if obj2.distance(BALL.ball) < 20:
                BALL.reboundx()
            else:
                BALL.ball.fd(SPEED)
                Screen().update()
    
    else:
        BALL.ball.fd(SPEED)
        Screen().update()
