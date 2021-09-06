# Planner
# 1.0) Create chess board array, subclasses for colour and piece type, place in starting
# 1.1) Possible moves - Each piece is unique

# 1.2) Check mechanism -  Valid moves (all of the other player's next possible moves attack your king in new position)
# 1.3) Special moves - Castling (both sides), pawn promotion, en pessant, pawn moves double ranks??
# 1.31) CHECKMATE, STALEMATE
# 1.32) Moving a piece on the same square ?!!?! 
# 1.4) Undo function, log system, 

# 2.0) Implement UI using pygame  (drawing board, drawing pieces, alternating square colours)
# 2.1) Implement drag drop - moving pieces using cursor

# 3.0) Plan out chess AI
# - - - - - - - - - - - - - - - - - - - - 

DIMENSION = 8
EMPTY = "--"

## Functions
# Function which prints each row at a time by rank, from white's perspective
def print_board(array):

    for rank in range(DIMENSION):
         print(array[rank])

## Classes
class Piece():

    def __init__(self, colour, row, col):
        self.colour = colour
        self.row = row
        self.col = col

    def __repr__(self): # TODO: Should be __str__
        class_name = type(self).__name__ 
        if class_name == 'Knight':
            class_name = 'Night'
            
        return "{}{}".format(self.colour[0], class_name[0]) # Returns 2 letter string showing colour and piece type respectively

    # def __repr__(self):
    #     return "{}('{}', '{}', '{}')".format(type(self).__name__, self.colour, self.col, self.row)

    # Moves piece at original square to the target square
    def piece_move(self, target_row, target_col):
        
        chess_board[target_row][target_col] = chess_board[self.row][self.col]
        chess_board[self.row][self.col] = EMPTY
        self.row = target_row
        self.col = target_col 

    # Function that can capture and/or move
    def piece_move_capture(self, target_row, target_col):
        
        # Ensure only capture a piece within our 8 x 8 array 
        # TODO: Should assert be in inner function or outer function?
        assert (0 <= target_row and target_row <= DIMENSION - 1) 
        assert (0 <= target_col and target_row <= DIMENSION - 1)

        # Piece capture : Target piece can only be captured if object exists at location (not a string)
        # if not isinstance(chess_board[target_row][target_col], str):
        if chess_board[target_row][target_col] is not EMPTY:
            # Piece can only capture its opposing colour
            if chess_board[target_row][target_col].colour != self.colour:
                self.piece_move(target_row, target_col)
        
        # Piece move : Target square must be an empty square
        else:
            self.piece_move(target_row, target_col)

    # Loops through squares in row or column from current position to target position (non inclusive), returning True or False
    def piece_block_rowcol(self, target_row, target_col):
        
        # Vertical movement 
        if self.col == target_col:
            
            calc = 1
            if self.row > target_row:
                calc = -1

            for i in range(self.row, target_row, calc):

                if chess_board[i][self.col] is not EMPTY:  

                    if i is not self.row: # Skip starting position

                        return True
            
            return False
        
        # Horizontal movement
        elif self.row == target_row:

            calc = 1
            if self.col > target_col:
                calc = -1
            
            for i in range(self.col, target_col, calc):

                if chess_board[self.row][i] is not EMPTY:   

                    if i is not self.col: # Skip starting position

                        return True

            return False

    # Loops through squares in a diagonal, from current position to target position, returning True or False
    def piece_block_diag(self, target_row, target_col):
        pass

## Subclasses
class Pawn(Piece): 

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    # Ability to move white up by one, or down by one for black pieces (if nothing blocking)
    def pawn_move_cap(self, target_row, target_col):

        # TODO: Implement user input conditions for single row and double row advance 

        calc = -1 # Default white case 
        if self.colour == 'black':
            calc = 1
        
        # Pawn advance : Target square is one space forward, ensure it contains EMPTY
        if chess_board[target_row][target_col] == EMPTY and target_row == self.row + calc and target_col == self.col:
            self.piece_move_capture(target_row, target_col)
        
        # Pawn double advance : Target square is two spaces forward, if on starting rank
        elif target_row == self.row + 2*calc and target_col == self.col and self.row == 3.5 - 2.5 * calc:
            # Ensure both positions are EMPTY
            if chess_board[target_row][target_col] == EMPTY and chess_board[target_row - calc][target_col] == EMPTY:

                self.piece_move_capture(target_row, target_col)

        # Pawn diagonal capture : If target square is the one square diagonally forward (left and right)
        elif target_row == self.row + calc and (target_col == self.col + calc or target_col == self.col - calc):
            if chess_board[target_row][target_col] != EMPTY: 

                self.piece_move_capture(target_row, target_col)

# class Pawn(Piece): # TODO: Consider changing pawn code to use target square mechanism

#     def __init__(self, colour, row, col):
#         super().__init__(colour, row, col)

#     # Ability to move white up by one, or down by one for black pieces (if nothing blocking)
#     def pawn_move(self):

#         # TODO: Implement user input conditions for single row and double row advance 

#         calc = -1 # Default white case 
#         if self.colour == 'black':
#             calc = 1
        
#         # if self.colour == 'white':
#         if chess_board[self.row + calc][self.col] == EMPTY: 
#             self.row = self.row + calc
#             chess_board[self.row][self.col] = chess_board[self.row - calc][self.col] # Allow pawn to move upward by one
#             chess_board[self.row - calc][self.col] = EMPTY
            
#             # Ability for white pawn to move upward by two on starting square (if nothing blocking)
#             if chess_board[self.row + calc][self.col] == EMPTY and self.row == 3.5 - 1.5 * calc: # Gives white or black's starting row
#                 self.row = self.row + calc
#                 chess_board[self.row][self.col] = chess_board[self.row - calc][self.col] # Allow pawn to move upward by one
#                 chess_board[self.row - calc][self.col] = EMPTY

#     def pawn_capture(self):

#         calc = -1 # Default white case 
#         if self.colour == 'black':
#             calc = 1

class Rook(Piece):

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    def rook_move_cap(self, target_row, target_col):
                
        # Target square is either in the same row or column
        if target_row == self.row or target_col == self.col:

            if self.piece_block_rowcol(target_row, target_col) is False:

                self.piece_move_capture(target_row, target_col)
        

class Bishop(Piece):

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    def bishop_move_cap(self, target_row, target_col):

        pass 
        # Target square is on either diagonal

class Queen(Piece):
    pass

class Knight(Piece):
    pass

class King(Piece):
    pass

# Creating all the pieces and placing them in their starting positions
bR1 = Rook('black', 0, 0)
bN1 = Knight('black', 0, 1)
bB1 = Bishop('black', 0, 2)
bK = King('black', 0, 3)
bQ = Queen('black', 0, 4)
bB2 = Bishop('black', 0, 5)
bN2 = Knight('black', 0, 6)
bR2 = Rook('black', 0, 7)

bP1 = Pawn('black', 1, 0)
bP2 = Pawn('black', 1, 1 )
bP3 = Pawn('black', 1, 2)
bP4 = Pawn('black', 1, 3)
bP5 = Pawn('black', 1, 4)
bP6 = Pawn('black', 1, 5)
bP7 = Pawn('black', 1, 6)
bP8 = Pawn('black', 1, 7)

wP1 = Pawn('white', 6, 0)
wP2 = Pawn('white', 6, 1)
wP3 = Pawn('white', 6, 2)
wP4 = Pawn('white', 6, 3)
wP5 = Pawn('white', 6, 4)
wP6 = Pawn('white', 6, 5)
wP7 = Pawn('white', 6, 6)
wP8 = Pawn('white', 6, 7)

wR1 = Rook('white', 7, 0)
wN1 = Knight('white', 7, 1)
wB1 = Bishop('white', 7, 2)
wK = King('white', 7, 3)
wQ = Queen('white', 7, 4)
wB2 = Bishop('white', 7, 5)
wN2 = Knight('white', 7, 6)
wR2 = Rook('white', 7, 7)

# 8 by 8 2D array
chess_board = [ 

    [bR1, bN1, bB1, bK, bQ, bB2, bN2, bR2],
    [bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8],
    [wR1, wN1, wB1, wK, wQ, wB2, wN2, wR2]

]
def cBoard():
    return chess_board


# bP1.pawn_move_cap(3, 0)
# bR1.rook_move_cap(2, 0)
# bR1.rook_move_cap(2, 1)
# bR1.rook_move_cap(4, 1)
# bR1.rook_move_cap(4, 0)
# bR1.rook_move_cap(0, 0)

print_board(chess_board) 


        

