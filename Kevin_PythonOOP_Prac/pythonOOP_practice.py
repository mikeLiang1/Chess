# 1 Simple Classes and Instances
class Chess_Piece:
    # Class variables
    num_piece_types = 0
    transformability = 0

    def __init__(self, piece, movement):
        self.piece = piece
        self.movement = movement
        self.description = piece + ' moves in a ' + movement

        Chess_Piece.num_piece_types += 1

    # Methods
    def piece_movement(self): # MUST add the self argument in the method creation  
        return '{} : {}'.format(self.piece, self.movement)

    # Class methods
    @classmethod
    def transform_all(cls, amount):
        cls.transformability = amount
    
    # This class method converts unideal hyphenated inputs into the class relevant format
    @classmethod
    def from_string(cls, hyphenated_str):
        piece, movement = hyphenated_str.split('-')
        return cls(piece, movement)

    # Static methods are used if neither the class or instanced needs to be accessed in it
    @staticmethod
    def is_chessday(day):   
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True


rook = Chess_Piece('Rook', 'straight line')
bishop = Chess_Piece('Bishop', 'diagonal line')
queen = Chess_Piece('Queen', 'straight and diagonal line')
pawn = Chess_Piece('Pawn', 'forward by one')

print(queen.description)
print(rook.piece_movement()) # A method requires the (), unlike the attribute

print(Chess_Piece.num_piece_types)

pawn.transformability = 1 # Instance specific 

print(rook.transformability)
Chess_Piece.transform_all(1) # Scope is whole class
print(rook.transformability)

# These potential instances are not in class format
hyphen_king = 'King-One step in any direction'
hyphen_knight = 'Knight-L shape'

king = Chess_Piece.from_string(hyphen_king)
knight = Chess_Piece.from_string(hyphen_knight)

print(knight.description)

# Using the static method to determine if today is a weekday
import datetime
my_date = datetime.date(2021, 9, 1)
print(Chess_Piece.is_chessday(my_date))