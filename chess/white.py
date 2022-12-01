import os
import turtle

currentDir = os.getcwd()
pictures = ['bishop.gif', 'bishop(1).gif', 'king.gif', 'king(1).gif', 'knight.gif', 'knight(1).gif', 'queen.gif', 'queen(1).gif', 'rook.gif', 'rook(1).gif', 'pawn.gif', 'pawn(1).gif']
names = ['bishop_B', 'bishop_W', 'king_B', 'king_W', 'knight_B', 'knight_W','queen_B', 'queen_W', 'rook_B', 'rook_W']
pieces = []

class White():
    def __init__(self):
        '''self.bishop_B = turtle.Turtle()
        turtle.register_shape(currentDir+'\\resources\\bishop.gif')
        self.bishop_B.shape(currentDir+'\\resources\\bishop.gif')'''

        for number in range(0, len(pictures)-1):
            exec('self.'+names[number]+'= turtle.Turtle()')
            exec('pieces.append(self.'+names[number]+')')          
            exec("turtle.register_shape(currentDir+'\\resources\\"+pictures[number]+"')")
            names[number].shape(pictures[number])
        

        