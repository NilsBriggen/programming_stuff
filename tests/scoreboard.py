from turtle import Turtle
import os
cwd = os.path.dirname(os.path.realpath(__file__))

ALIGNEMENT = 'center'
FONT = 'Courier'
FONTSIZE = 18
FONTTYPE = 'normal'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.color('white')
        self.penup()
        self.goto(150, 270)
        self.write(f"Score: {self.score}", False, ALIGNEMENT, (FONT, FONTSIZE, FONTTYPE))
        with open(f'{cwd}\\highscore.txt') as f:
            highscore = f.read()
        f.close()
        self.goto(-150, 270)
        self.write(f"Highscore: {highscore}", False, ALIGNEMENT, (FONT, FONTSIZE, FONTTYPE))

    def update(self):
        self.clear()
        self.score += 1
        self.goto(150, 270)
        self.write(f"Score: {self.score}", False, ALIGNEMENT, (FONT, FONTSIZE, FONTTYPE))
        with open(f'{cwd}\\highscore.txt') as f:
            highscore = f.read()
        f.close()
        self.goto(-150, 270)
        self.write(f"Highscore: {highscore}", False, ALIGNEMENT, (FONT, FONTSIZE, FONTTYPE))

    def GameOver(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, ALIGNEMENT, (FONT, 30, FONTTYPE))
        with open(f'{cwd}\\highscore.txt') as f:
            highscore = f.read()
            if highscore < str(self.score):
                with open(f'{cwd}\\highscore.txt', 'w') as y:
                    y.truncate(0)
                    y.write(str(self.score))
                    y.close()
            f.close()
            
