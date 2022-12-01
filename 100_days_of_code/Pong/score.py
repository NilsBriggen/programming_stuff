import turtle as Turtle
import time

ALIGNEMENT = 'center'
FONT = 'Courier'
FONTSIZE = 50
FONTTYPE = 'normal'
END_SCORE = 10

class Score():
    def __init__(self):
        self.writer = Turtle.Turtle()
        self.score1 = 0
        self.score2 = 0
        self.writer.ht()
        self.writer.color('white')
        self.writer.penup()
        self.writer.goto(0, 0)
        self.writer.write(f"{self.score2}:{self.score1}", False, ALIGNEMENT, (FONT, FONTSIZE, FONTTYPE))

    def update_paddle1(self):
        self.score1 += 1
        self.writer.clear()
        self.writer.write(f"{self.score2}:{self.score1}", False, ALIGNEMENT, (FONT, FONTSIZE, FONTTYPE))

        if self.score1 == END_SCORE:
            self.writer.goto(0, 50)
            self.writer.write("Game Over!", False, ALIGNEMENT, (FONT, FONTSIZE, FONTTYPE))
            time.sleep(5)
            self.writer.goto(0, 0)
            self.writer.clear()
            self.score1 = 0
            self.score2 = 0
            self.writer.write(f"{self.score2}:{self.score1}", False, ALIGNEMENT, (FONT, FONTSIZE, FONTTYPE))

    def update_paddle2(self):
        self.score2 += 1
        self.writer.clear()
        self.writer.write(f"{self.score2}:{self.score1}", False, ALIGNEMENT, (FONT, FONTSIZE, FONTTYPE))

        if self.score2 == END_SCORE:
            self.writer.goto(0, 50)
            self.writer.write("Game Over!", False, ALIGNEMENT, (FONT, FONTSIZE, FONTTYPE))
            time.sleep(5)
            self.writer.goto(0, 0)
            self.writer.clear()
            self.score1 = 0
            self.score2 = 0
            self.writer.write(f"{self.score2}:{self.score1}", False, ALIGNEMENT, (FONT, FONTSIZE, FONTTYPE))