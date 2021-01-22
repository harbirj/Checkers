from .constants import RED, WHITE, SQUARE_SIZE, GREY, BLACK, CROWN
import pygame

class Piece:
    PADDING = 15
    BORDER = 1

    #initialization of the pieces
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    #calculate the position of the piece
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    #change piece to king if conditions are met
    def make_king(self):
        self.king = True

    #draw the piece with a circle within a circle for outline
    #add crown if king piece
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    #movement of the piece
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __representation(self):
        return str(self.colour)
