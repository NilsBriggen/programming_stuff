from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import ctypes
import sys
import os

def restart():
    Screen().clear()
    game()


def game():
    cwd = os.path.dirname(os.path.realpath(__file__))

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    def clear_highscore():
        with open(f'{cwd}\\highscore.txt', 'w') as y:
            y.truncate(0)
            y.write(str(0))
            y.close()

    screen = Screen()
    screen.tracer(0)
    screen.setup(600, 600)
    screen.bgcolor('black')
    screen.title("Snake")

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    gameOn = True
    while gameOn == True:
        screen.update()
        time.sleep(0.25)
        snake.move()

        if snake.head.distance(food) < 10:
            food.refresh()
            scoreboard.update()
            snake.extend()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            gameOn = False
            screen.onkey(clear_highscore, "c")
            screen.onkey(restart, "r")
            scoreboard.GameOver()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                gameOn = False
                screen.onkey(clear_highscore, "c")
                screen.onkey(restart, "r")
                scoreboard.GameOver()

    screen.exitonclick()

game()
