import pygame

#constants used in the game, can be manipulated
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#colours in RGB
RED = (255, 0 ,0)
WHITE = (255,255,255)
BLACK = (0, 0, 0)
BLUE = (0,0,255)
GREY = (128, 128, 128)
CREAM = (239,196,139)
BROWN = (172,115,50)

#crown for the king piece
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (45,25))
