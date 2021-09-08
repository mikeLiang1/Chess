# Planner
# 1.0) Create chess board array, subclasses for colour and piece type, place in starting
# 1.1) Possible moves - Each piece is unique
# 2.0) Implement UI using pygame  (drawing board, drawing pieces, alternating square colours)
# 1.2) Check mechanism -  Valid moves (all of the other player's next possible moves attack your king in new position)
# 1.32) Moving a piece on the same square ?!!?! 
# 2.1) Implement drag drop - moving pieces using cursor

# 2.0) Available moves function

# 1.3) Special moves - Castling (both sides), pawn promotion, en pessant, pawn moves double ranks??
# 1.31) CHECKMATE, STALEMATE, in check (should you be able to click on other pieces that can't stop the check?)

# 1.32) Moving a piece on the same square ?!!?! 
# 1.4) Undo function, log system, 

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
        self.available_moves = []

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
               
        if chess_board[target_row][target_col] == EMPTY or chess_board[target_row][target_col].colour != self.colour:
            self.piece_move(target_row, target_col)
            return True
        
        return False


    # Loops through squares in row or column from current position to target position (non inclusive), returning True or False
    def piece_block_rowcol(self, target_row, target_col):
        
        # Vertical movement 
        if self.col == target_col:
            
            calc = 1
            if self.row > target_row:
                calc = -1

            for i in range(self.row + calc, target_row, calc):

                if chess_board[i][self.col] is not EMPTY:  

                    return True
            
            return False
        
        # Horizontal movement
        elif self.row == target_row:

            calc = 1
            if self.col > target_col:
                calc = -1
            
            for i in range(self.col + calc, target_col, calc):

                if chess_board[self.row][i] is not EMPTY:   

                    return True

            return False

    # Loops through squares in a diagonal, from current position to target position, returning True or False
    def piece_block_diag(self, target_row, target_col):
        
        calc_row = 1
        if self.row > target_row:
            calc_row = -1 

        calc_col = 1
        if self.col > target_col:
            calc_col = -1 

        for i in range(1, abs(self.row - target_row)): # Skip starting position

            if chess_board[self.row + i * calc_row][self.col + i * calc_col] is not EMPTY:  
 
                return True
        
        return False

    # Loop through available moves list, if target square matches a tuple in available moves list, return move capture function
    def move_cap(self, target_row, target_col):
        
        self.get_available_moves()

        for i in self.available_moves:

            if (target_row, target_col) == i:

                return self.piece_move_capture(target_row, target_col)

        return False
        
## Subclasses
class Pawn(Piece): 

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    def get_available_moves(self):

        # Ability to move white up by one, or down by one for black pieces (if nothing blocking)
        calc = -1 # Default white case 
        if self.colour == 'black':
            calc = 1

         # Pawn advance : Target square is one space forward, ensure it contains EMPTY
        if 0 <= self.row + calc and self.row + calc <= DIMENSION - 1:

            if chess_board[self.row + calc][self.col] == EMPTY:

                self.available_moves.append((self.row + calc, self.col))
        
        # Pawn double advance : Target square is two spaces forward, if on starting rank
        if 0 <= self.row + 2*calc and self.row + 2*calc <= DIMENSION - 1:  

            if chess_board[self.row + 2*calc][self.col] == EMPTY and chess_board[self.row + calc][self.col] == EMPTY and self.row == 3.5 - 2.5 * calc:

                self.available_moves.append((self.row + 2*calc, self.col))
        
        # Pawn diagonal capture : If target square is the one square diagonally forward (left)
        if 0 <= self.row + calc and self.row + calc <= DIMENSION - 1 and 0 <= self.col + calc and self.col + calc <= DIMENSION - 1:

            if chess_board[self.row + calc][self.col + calc] != self.colour and chess_board[self.row + calc][self.col + calc] != EMPTY:

                self.available_moves.append((self.row + calc, self.col + calc))

        # Pawn diagonal capture : Forward right
        if 0 <= self.row + calc and self.row + calc <= DIMENSION - 1 and 0 <= self.col - calc and self.col - calc <= DIMENSION - 1:

            if chess_board[self.row + calc][self.col - calc] != self.colour and chess_board[self.row + calc][self.col - calc] != EMPTY:
                
                self.available_moves.append((self.row + calc, self.col - calc))

class Queen(Piece):
    
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    def get_rook_available_moves(self):

        # Looping vertically up and down the board from current position
      
        for i in range(self.row - 1, 0, -1):
            
            if chess_board[i][self.col] is EMPTY:  

                self.available_moves.append((i, self.col))
                print(self.available_moves)

            else: 
                break        

        for i in range(self.row + 1, DIMENSION - 1, 1):
            
            if chess_board[i][self.col] is EMPTY:  

                self.available_moves.append((i, self.col))
                print(self.available_moves)

            else: 
                break   

        # Horizontal 
        for i in range(self.col - 1, 0, -1):
            
            if chess_board[self.row][i] is EMPTY:  

                self.available_moves.append((self.row, i))
                print(self.available_moves)

            else: 
                break        

        for i in range(self.col + 1, DIMENSION - 1, 1):
            
            if chess_board[self.row][i] is EMPTY:  

                self.available_moves.append((self.row, i))
                print(self.available_moves)

            else: 
                break  

    def bishop_move_cap(self, target_row, target_col):

        # Target square is on either diagonal
        if abs(target_row - self.row) == abs(target_col - self.col): 

            # Check that no piece is blocking diagonal path
            if self.piece_block_diag(target_row, target_col) is False: 

                return self.piece_move_capture(target_row, target_col)
        return False

    def get_available_moves(self):

        # Target square is a horizontal, vertical or diagonal
        return self.get_rook_available_moves() and self.get_bishop_available_moves()

class Rook(Queen):

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    def get_available_moves(self):
        return self.get_rook_available_moves()

class Bishop(Queen):
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)
             
    def move_cap(self, row, col):
        return self.bishop_move_cap(row, col)
class Knight(Piece):
    
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    def move_cap(self, target_row, target_col):

        # L shape movement
        if abs(target_row - self.row) == 2 and abs(target_col - self.col) == 1:

            return self.piece_move_capture(target_row, target_col)

        elif abs(target_row - self.row) == 1 and abs(target_col - self.col) == 2:

            return self.piece_move_capture(target_row, target_col)
        return False

class King(Piece):

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    def move_cap(self, target_row, target_col):

        # Left, right, up, down
        if abs(target_row - self.row) + abs(target_col - self.col) == 1:
            
            return self.piece_move_capture(target_row, target_col)

        # Diagonally - up left, up right, down left, down right
        elif abs(target_row - self.row) ==  abs(target_col - self.col) == 1:
            
            return self.piece_move_capture(target_row, target_col)
        return False

    

# Creating all the pieces and placing them in their starting positions
bR1 = Rook('black', 0, 0)
bN1 = Knight('black', 0, 1)
bB1 = Bishop('black', 0, 2)
bQ = Queen('black', 0, 3)
bK = King('black', 0, 4)
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
wQ = Queen('white', 7, 3)
wK = King('white', 7, 4)
wB2 = Bishop('white', 7, 5)
wN2 = Knight('white', 7, 6)
wR2 = Rook('white', 7, 7)


# 8 by 8 2D array
chess_board = [ 

    [bR1, bN1, bB1, bQ, bK, bB2, bN2, bR2],
    [bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8],
    [wR1, wN1, wB1, wQ, wK, wB2, wN2, wR2]
]

cur_turn = 'white'



print_board(chess_board) 