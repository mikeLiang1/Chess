# Planner

# COMPLETED
# 1.0) Create chess board array, subclasses for colour and piece type, place in starting
# 1.1) Possible moves - Each piece is unique
# 2.0) Implement UI using pygame  (drawing board, drawing pieces, alternating square colours)
# 1.2) Check mechanism -  Valid moves (all of the other player's next possible moves attack your king in new position)
# 1.32) Moving a piece on the same square ?!!?! 
# 2.1) Implement drag drop - moving pieces using cursor
# 1.4) Undo function, log system, 
# 1.32) Moving a piece on the same square ?!!?! 
# 2.0) Available moves function

# ONGOING
# 1.3) Special moves - Castling (both sides), pawn promotion, en pessant, pawn moves double ranks??
# 1.31) CHECKMATE, STALEMATE, in check (should you be able to click on other pieces that can't stop the check?)

# FUTURE
# 3.0) Basic chess AI
# - - - - - - - - - - - - - - - - - - - - 
import copy

DIMENSION = 8
EMPTY = "--"


cur_turn = 'white'

## Functions


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

        # Ensure only capture a piece within our 8 x 8 array 
        # assert (0 <= target_row and target_row <= DIMENSION - 1) 
        # assert (0 <= target_col and target_row <= DIMENSION - 1)

        # Piece capture : Target piece can only be captured if object exists at location (not a string)
        # if not isinstance(chess_board[target_row][target_col], str):
        
                  
        if chess_board[target_row][target_col] == EMPTY or chess_board[target_row][target_col].colour != self.colour: 
            add_to_undo()
            
            self.piece_move(target_row, target_col)
            
            return True
        
        
        return False

    # Loop through available moves list, if target square matches a tuple in available moves list, return move capture function
    # TODO: Changge move_cap function name
    def move_cap(self, target_row, target_col):
        
        curr_available_moves = copy.deepcopy(self.available_moves)
        self.available_moves.clear()
        
        for i in curr_available_moves:

            if (target_row, target_col) == i:

                if (target_row == 7 or target_row == 0) and type(self).__name__ == "Pawn": # checking for promotion
                    return self.promote(target_row, target_col)

                # 1) Run is_in_check function (checks if your OWN king is in check)
                # 2) For the piece in question (clicked) , loop through available moves and save the ones which 'stop' the check (using is_in_check), either by capturing or blockinig
                # 2.1 Dont open your own king up to check (run is_in_check again, take out invalid moves)
                # 3) Update the saved squares as the new available moves

                return self.piece_move_capture(target_row, target_col)

        return False
    
    # For knights (one square)
    def empty_or_enemy(self, possible_row, possible_col):

        if chess_board[possible_row][possible_col] is EMPTY:

            self.available_moves.append((possible_row, possible_col))

        else:

            if chess_board[possible_row][possible_col].colour != self.colour:

                self.available_moves.append((possible_row, possible_col))

    # For bishops and rooks (row, column or diagonals)
    def loop_empty_or_enemy(self, possible_row, possible_col):

        if chess_board[possible_row][possible_col] is EMPTY:

            self.available_moves.append((possible_row, possible_col))

            return True

        else:

            if chess_board[possible_row][possible_col].colour != self.colour:

                self.available_moves.append((possible_row, possible_col))

            return False

    # Loops through EVERY enemy piece's available moves and if any matches your king's square, you are in check
    def is_in_check():
        pass
        
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

            if chess_board[self.row + calc][self.col + calc] != EMPTY:

                if chess_board[self.row + calc][self.col + calc].colour != self.colour:

                    self.available_moves.append((self.row + calc, self.col + calc))

        # Pawn diagonal capture : Forward right
        if 0 <= self.row + calc and self.row + calc <= DIMENSION - 1 and 0 <= self.col - calc and self.col - calc <= DIMENSION - 1:

            if chess_board[self.row + calc][self.col - calc] != EMPTY:

                if chess_board[self.row + calc][self.col - calc].colour != self.colour:
                
                    self.available_moves.append((self.row + calc, self.col - calc))

    def promote(self, target_row, target_col):
        if chess_board[target_row][target_col] == EMPTY or chess_board[target_row][target_col].colour != self.colour:
            copy_array = [[],[],[],[],[],[],[],[]]
            for i in range(DIMENSION):
                copy_array[i] = copy.deepcopy(chess_board[i])

            last_board_state.append(copy_array)
            chess_board[self.row][self.col] = EMPTY
            chess_board[target_row][target_col] = Queen(self.colour, target_row, target_col)
            
            return True
        
        return False


class Queen(Piece):

    # TODO: Put rook and bishop available moves into functiions (shorten code)
    
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    def get_rook_available_moves(self):

        # Looping vertically up and down the board from current position
      
        for i in range(self.row - 1, -1, -1): # Range function doesn't include the end range number, so its -1 not 0
            
            keep_looping = self.loop_empty_or_enemy(i, self.col)

            if keep_looping == False:
                break

            # if chess_board[i][self.col] is EMPTY:  

            #     self.available_moves.append((i, self.col))

            # else: 
            #     # If first non EMPTY square is opposite colour, add the potentially capture square to available moves
            #     if chess_board[i][self.col].colour != self.colour:

            #         self.available_moves.append((i, self.col))

            #      # Rook doesn't move through pieces
            #     break        

        for i in range(self.row + 1, DIMENSION, 1):
            
            keep_looping = self.loop_empty_or_enemy(i, self.col)

            if keep_looping == False:
                break

        # Horizontal 
        for i in range(self.col - 1, -1, -1):
            
            keep_looping = self.loop_empty_or_enemy(self.row, i)

            if keep_looping == False:
                break     

        for i in range(self.col + 1, DIMENSION, 1):
            
            keep_looping = self.loop_empty_or_enemy(self.row, i)

            if keep_looping == False:
                break

    def get_bishop_available_moves(self):
        
        # Upwards right
        i = 1
        while (self.row - i > -1 and self.col + i < DIMENSION):

            keep_looping = self.loop_empty_or_enemy(self.row - i, self.col + i)

            if keep_looping == False:
                break

            i += 1

        # Upwards left
        i = 1
        while (self.row - i > -1 and self.col - i > -1):

            keep_looping = self.loop_empty_or_enemy(self.row - i, self.col - i)

            if keep_looping == False:
                break

            i += 1

        # Downwards left
        i = 1
        while (self.row + i < DIMENSION and self.col - i > -1):

            keep_looping = self.loop_empty_or_enemy(self.row + i, self.col - i)

            if keep_looping == False:
                break

            i += 1

        # Downwards right
        i = 1
        while (self.row + i < DIMENSION and self.col + i < DIMENSION):

            keep_looping = self.loop_empty_or_enemy(self.row + i, self.col + i)

            if keep_looping == False:
                break

            i += 1


    def get_available_moves(self):

        # Target square is a horizontal, vertical or diagonal
        return self.get_rook_available_moves() or self.get_bishop_available_moves()

class Rook(Queen):

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    def get_available_moves(self):
        return self.get_rook_available_moves()

class Bishop(Queen):
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)
             
    def get_available_moves(self):
        return self.get_bishop_available_moves()

class Knight(Piece):
    
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)

    def get_available_moves(self):

        for n_possible_row in range(0, DIMENSION):
            for n_possible_col in range(0, DIMENSION):

                # L shape movement
                if abs(n_possible_row - self.row) == 2 and abs(n_possible_col - self.col) == 1:

                    self.empty_or_enemy(n_possible_row, n_possible_col)

                if abs(n_possible_row - self.row) == 1 and abs(n_possible_col - self.col) == 2:

                    self.empty_or_enemy(n_possible_row, n_possible_col)

class King(Piece):

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)
        self.can_castle = True

    def get_available_moves(self):

        for k_possible_row in range(0, DIMENSION):
            for k_possible_col in range(0, DIMENSION):

                # Left, right, up, down
                if abs(k_possible_row - self.row) + abs(k_possible_col - self.col) == 1:

                    self.empty_or_enemy(k_possible_row, k_possible_col)

                # Diagonally - up left, up right, down left, down right

                if abs(k_possible_row - self.row) == abs(k_possible_col - self.col) == 1:

                    self.empty_or_enemy(k_possible_row, k_possible_col)
                
    
    # TODO: MIKE integrate castling code into available moves mechanism
    # def move_cap(self, target_row, target_col):
        
    #     elif self.can_castle == True:
    #         print("can castle")
    #         if target_row == self.row and target_col == 6: #right side castle
    #             if chess_board[self.row][self.col + 1] == EMPTY and chess_board[self.row][self.col+2] == EMPTY and isinstance(chess_board[self.row][self.col+3], Rook) == True:
    #                 self.castle(target_row, target_col, chess_board[self.row][self.col+3], 5)
    #                 self.can_castle = False
    #                 return True
    #         elif target_row == self.row and target_col == 2: # left side castle
    #             if chess_board[self.row][self.col - 1] == EMPTY and chess_board[self.row][self.col-2] == EMPTY and chess_board[self.row][self.col-3] == EMPTY and \
    #                 isinstance(chess_board[self.row][self.col-4], Rook) == True:
    #                 self.castle(target_row, target_col, chess_board[self.row][self.col-4], 3)
    #                 self.can_castle = False
    #                 return True
    #     return False

    def castle(self, target_row, target_col, rook, rook_col):
        print("castled")
        add_to_undo()
        self.piece_move(target_row, target_col)
        rook.piece_move(target_row, rook_col)

        
def add_to_undo():
    copy_array = [[],[],[],[],[],[],[],[]]
    for i in range(DIMENSION):
        copy_array[i] = copy.deepcopy(chess_board[i])

    last_board_state.append(copy_array)


cur_turn = 'white'

def flip_sides():
    global cur_turn
    if cur_turn == 'white':
        cur_turn = 'black'
    else:
        cur_turn = 'white'

def undoMove():
    global chess_board 
    global last_board_state
    if (last_board_state == []): # if empty
        return
    print(chess_board)
    print("\n")
    print(last_board_state)
    for i in range(DIMENSION):
        chess_board[i] = copy.deepcopy(last_board_state[-1][i])   
    last_board_state.pop()
    flip_sides()
    
    
    

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

last_board_state = []


