# Planner
# 1.0) Create chess board array, subclasses for colour and piece type, place in starting
# 1.1) Possible moves - Each piece is unique

# 1.2) Check mechanism -  Valid moves (all of the other player's next possible moves attack your king in new position)
# 1.3) Special moves - Castling (both sides), pawn promotion, en pessant, pawn moves double ranks??
# 1.31) CHECKMATE, STALEMATE
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

    # Takes in an input target square (make sure its valid range), replaces piece at target square, and clears the original square
    def piece_capture(self, target_row, target_col):
        
        # Ensure only capture a piece within our 8 x 8 array 
        assert (0 <= target_row and target_row <= DIMENSION - 1) 
        assert (0 <= target_col and target_row <= DIMENSION - 1)

        # Target piece can only be captured if object exists at location (not a string)
        if not isinstance(chess_board[target_row][target_col], str):
            # Piece can only capture its opposing colour
            if chess_board[target_row][target_col].colour != self.colour:

                chess_board[target_row][target_col] = chess_board[self.row][self.col]
                chess_board[self.row][self.col] = '--'
                self.row = target_row
                self.col = target_col 


## Subclasses
class Pawn(Piece):

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    # Ability to move white up by one, or down by one for black pieces (if nothing blocking)
    def pawn_move(self):

        # TODO: Implement user input conditions for single row and double row advance 

        calc = -1 # Default white case 
        if self.colour == 'black':
            calc = 1
        
        # if self.colour == 'white':
        if chess_board[self.row + calc][self.col] == '--': 
            self.row = self.row + calc
            chess_board[self.row][self.col] = chess_board[self.row - calc][self.col] # Allow pawn to move upward by one
            chess_board[self.row - calc][self.col] = '--'
            
            # Ability for white pawn to move upward by two on starting square (if nothing blocking)
            if chess_board[self.row + calc][self.col] == '--' and self.row == 3.5 - 1.5 * calc: # Gives white or black's starting row
                self.row = self.row + calc
                chess_board[self.row][self.col] = chess_board[self.row - calc][self.col] # Allow pawn to move upward by one
                chess_board[self.row - calc][self.col] = '--'

        # elif self.colour == 'black':
        #     if chess_board[self.row + 1][self.col] == '--': 
        #         self.row = self.row + 1
        #         chess_board[self.row][self.col] = chess_board[self.row - 1][self.col] # Allow pawn to move upward by one
        #         chess_board[self.row - 1][self.col] = '--'
                
        #         # Ability for black pawn to move downward by two on starting square (if nothing blocking)
        #         if chess_board[self.row + 1][self.col] == '--' and self.row == 2:
        #             self.row = self.row + 1
        #             chess_board[self.row][self.col] = chess_board[self.row - 1][self.col] # Allow pawn to move upward by one
        #             chess_board[self.row - 1][self.col] = '--'

    def pawn_capture(self):

        calc = -1 # Default white case 
        if self.colour == 'black':
            calc = 1
        
        # TODO: Implement user input conditions for the 2 immediate forward diagonals 
        self.piece_capture(self.row + calc, self.col + calc)
        # Other diagonal : self.piece_capture(self.row + calc, self.col - calc)

class Rook(Piece):
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    # TODO: 
    def rook_move(self, target_row, target_col):
        pass

    # Very likely this would go inside rook_move 
    def rook_capture(self, target_row, target_col):
        pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class Knight(Piece):
    pass

class King(Piece):
    pass

# TODO: Create and put pieces into their starting positions
bP1 = Pawn('black', 1, 0)
bP2 = Pawn('black', 1, 1 )
bP3 = Pawn('black', 1, 2)
bP7 = Pawn('black', 1, 6)


wP1 = Pawn('white', 6, 0)
wP2 = Pawn('white', 6, 1)
wP3 = Pawn('white', 6, 2)
wP7 = Pawn('white', 6, 6)

bR1 = Rook('black', 0, 0)

# 8 by 8 2D array

chess_board = [ # TODO: Change all strings to objects like we did with the pawn

    [bR1, "bN", "bB", "bK", "bQ", "bB", "bN", "bR"],
    [bP1, bP2, bP3, "bP", "bP", "bP", bP7, "bP"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    [wP1, wP2, wP3, "wP", "wP", "wP", wP7, "wP"],
    ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"]

]

print_board(chess_board) 

# print(chess_board[0][5])

        


