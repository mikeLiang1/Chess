# Planner
# 1.0) Create chess board array, subclasses for colour and piece type, place in starting
# 1.1) Possible moves - Each piece is unique
# 1.2) Check mechanism -  Valid moves (all of the other player's next possible moves attack your king in new position)
# 1.3) Special moves - Castling (both sides), pawn promotion, en pessant, pawn moves double ranks??
# 1.4) Undo function, log system

# 2.0) Implement UI using pygame  (drawing board, drawing pieces, alternating square colours)
# 2.1) Implement drag drop - moving pieces using cursor

# 3.0) Plan out chess AI
# - - - - - - - - - - - - - - - - - - - - 

DIMENSION = 8

## Functions
# Function which prints each row at a time by rank, from white's perspective
def print_board(array):

    for rank in range(DIMENSION):
         print(array[rank])

## Classes
class Piece:

    def __init__(self, colour, row, col):
        self.colour = colour
        self.row = row
        self.col = col

    def __repr__(self): # TODO: Should be __str__
        class_name = type(self).__name__ 
        return "'{}{}'".format(self.colour[0], class_name[0]) # Returns 2 letter string showing colour and piece type respectively

    # def __repr__(self):
    #     return "{}('{}', '{}', '{}')".format(type(self).__name__, self.colour, self.col, self.row)


## Subclasses
class Pawn(Piece):

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    # Ability to move white up by one, or down by one for black pieces (if nothing blocking)
    def move_pawn(self):

        # TODO: Implement user input conditions
        if self.colour == 'white': 
            if chess_board[self.row - 1][self.col] == '--': 
                print('test')
                self.row = self.row-1
                chess_board[self.row - 1][self.col] = chess_board[self.row][self.col] # Allow pawn to move upward by one
                chess_board[self.row][self.col] = '--'
                
                
                # Ability to move upward by two on starting square (if nothing blocking)
                # if chess_board[row - 2][col] == '--' and row == 6:
                #     chess_board[row - 2][col] = chess_board[row][col] # Allow pawn to  move forward by two 
                #     chess_board[row][col] = '--'

        # elif self.colour == 'black':
        #     if self.board[col][row + 1] == '--':
        #         pass # TODO: Allow pawn to move downward by one
                
        #         # Ability to move downward by two on starting square (if nothing blocking)
        #         if self.board[col][row + 2] == '--' and row == 2:
        #             pass # TODO: Allow pawn to  move downward by two 

    # TODO: Ability to capture diagonally (need to work out white/black separation first)
        
class Rook(Piece):
    pass

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

# 8 by 8 2D array
chess_board = [ # TODO: Change all strings to objects like we did with the pawn

    ["bR", "bN", "bB", "bK", "bQ", "bB", "bN", "bR"],
    [Pawn('black', 0, 1), "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["wP", "wP", "wP", "wP", "wP", "wP", Pawn('white', 6, 6), "wP"],
    ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"]

]


Pawn('white', 6, 6).move_pawn()

print_board(chess_board) 

# print(chess_board[0][5])

        


