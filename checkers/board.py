import pygame
from .constants import BLACK, ROWS, COLS, RED, SQUARE_SIZE, CREAM, BROWN, WHITE
from .piece import Piece

#handles the state of the board
class Board:
    #initialization of the board
    def __init__(self):
        self.board = []
        self.red_left = self.black_left = 12
        self.red_kings = self.black_kings = 0
        self.create_board()

    #fill the entire screen with brown
    #fill every other square with cream colour to draw the board
    def draw_squares(self, win):
        win.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                for col in range(row % 2, ROWS, 2):
                    pygame.draw.rect(win, CREAM, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    #tells the score of the board for the AI
    def evaluate(self):
        return self.black_left - self.red_left + (self.black_kings * 0.5 - self.red_kings *0.5)

    def get_all_pieces(self, colour):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.colour == colour:
                    pieces.append(piece)
        return pieces        

    #controls the movements and makes king if piece reaches the end
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS -1 or row == 0:
            piece.make_king()
            if piece.colour == BLACK:
                self.black_kings += 1
            else:
                self.red_kings += 1
    
    #get a piece at specific row and col
    def get_piece(self, row, col):
        return self.board[row][col]

    #draw the pieces to fill the board
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    #draw the board by calling draw_square
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    #remove a given piece
    def remove (self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.colour == RED:
                    self.red_left -= 1
                else:
                    self.black_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return BLACK
        elif self.black_left <= 0:
            return RED

        return None

    #given a piece calculate all the valid moves
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
    
        if piece.colour == RED or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.colour, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.colour, right))
        if piece.colour == BLACK or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.colour, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.colour, right))

        return moves

    def _traverse_left(self, start, stop, step, colour, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, colour, left-1, skipped = last))
                    moves.update(self._traverse_right(r+step, row, step, colour, left+1, skipped = last))
                break
            elif current.colour == colour:
                break
            else:
                last = [current]
            left -= 1

        return moves

    def _traverse_right (self, start, stop, step, colour, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, colour, right-1, skipped = last))
                    moves.update(self._traverse_right(r+step, row, step, colour, right+1, skipped = last))
                break
            elif current.colour == colour:
                break
            else:
                last = [current]
            right += 1
        
        return moves
