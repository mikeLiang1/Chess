import pygame as p
import os
import core


os.environ["SDL_VIDEODRIVER"]="x11"
os.environ['SDL_AUDIODRIVER'] = 'dsp'

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def load_images():
    pieces = ['wP', 'wR', 'wN', 'wB', "wK", "wQ", "bP", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".png"), (SQ_SIZE, SQ_SIZE))
       

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    board = core.chess_board
   
    load_images()
    running = True
    selected_square = () # a tuple of selected square (row, column)

    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if selected_square == (): #first click
                    if board[row][col] != "--": # only if i clicked on a piece i can move it
                        selected_square = (row, col)  
                                 
                else: #second click
                    if selected_square != (row,col):  
                        board[selected_square[0]][selected_square[1]].piece_move(row, col)
                    selected_square = ()
                    player_clicks = []

                # if selected_square == (row, col): # user has last clicked this square, we unlick
                #     selected_square = ()
                #     player_clicks = []
                   
                # else: # clicked elsewhere   
                #     selected_square = (row, col)
                #     print(board[row][col], selected_square)
                #     player_clicks.append(selected_square)
                # if len(player_clicks) == 2: # players second click we make move
                #     piece = player_clicks[0]
                #     target = player_clicks[1]
                    
                #     if board[piece[0]][piece[1]] != "--": #if is piece
                #         board[piece[0]][piece[1]].pawn_move_cap(target[0], target[1])
                #     selected_sqaure = ()
                #     player_clicks = []
                                                              
        draw_game_state(screen, board)
        clock.tick(MAX_FPS)
        p.display.flip()

def draw_game_state(screen, board):
    draw_board(screen)
    
    draw_pieces(screen, board)

def draw_board(screen):
    colors = [p.Color("white"), p.Color("pink")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) %2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE,SQ_SIZE))
    
def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            
            if piece != "--":
                screen.blit(IMAGES[repr(piece)], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == '__main__':
    main()



