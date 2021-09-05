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

    def __init__(self, colour, col, row):
        self.colour = colour
        self.col = col
        self.row = row

    def __str__(self): # TODO: Not running at all 
        class_name = type(self).__name__ # TODO: First file pawn fucks up
        return "'{}{}'".format(class_name[0], self.colour[0]) # Returns 2 letter string showing colour and piece type respectively

    def __repr__(self):
        return "{}('{}', '{}', '{}')".format(type(self).__name__, self.colour, self.col, self.row)


## Subclasses
class Pawn(Piece):

    def __init__(self, colour, col, row):
        super().__init__(colour, col, row)

        # Ability to move white up by one, or down by one for black pieces (if nothing blocking)
        if self.colour == 'white':
            if self.board[col][row - 1] == '--':
                pass # TODO: Allow pawn to move upward by one
                
                # Ability to move upward by two on starting square (if nothing blocking)
                if self.board[col][row - 2] == '--' and row == 6:
                    pass # TODO: Allow pawn to  move forward by two 

        elif self.colour == 'black':
            if self.board[col][row + 1] == '--':
                pass # TODO: Allow pawn to move downward by one
                
                # Ability to move downward by two on starting square (if nothing blocking)
                if self.board[col][row + 2] == '--' and row == 2:
                    pass # TODO: Allow pawn to  move downward by two 

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
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"]

]

print_board(chess_board) # TODO: How the fuck do we connect the board to the classes?

# print(chess_board[0][5])

        



