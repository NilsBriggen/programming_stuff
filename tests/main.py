from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import ctypes, sys
import kivy
def isAdmin():
    try:
        ctypes.windll.shell32.IsUserAnAdmin()
        return True
    except:
        return False

if isAdmin():
    screen = Screen()
    screen.tracer(0)
    screen.setup(600, 600)
    screen.bgcolor('black')
    screen.title("Snake")

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()



    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    gameOn = True
    while gameOn == True:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 10:
            food.refresh()
            scoreboard.update()
            snake.extend()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            gameOn = False
            scoreboard.GameOver()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                gameOn = False
                scoreboard.GameOver()
            

    screen.exitonclick()

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)