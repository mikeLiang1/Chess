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
                    if board[row][col] != "--" and board[row][col].colour == core.cur_turn: # only if i clicked on a piece i can move it        
                        selected_square = (row, col)            
                                 
                else: #second click
                    if selected_square != (row,col):  

                        if board[selected_square[0]][selected_square[1]].move_cap(row, col) == True:
                            if core.cur_turn == 'black':
                                core.cur_turn = 'white'
                            else:
                                core.cur_turn = 'black'
                            animate_move(screen, board, clock, (row,col), selected_square, board[row][col])
                    selected_square = ()
                                                              
        draw_game_state(screen, board, selected_square)
        
        clock.tick(MAX_FPS)
        p.display.flip()

# highlight sqaure selected and posibble moves
def highlight_squares(screen, selected_sq):
    if (selected_sq == ()):
        return
    r,c = selected_sq
    s = p.Surface((SQ_SIZE, SQ_SIZE))
    s.set_alpha(100)
    s.fill(p.Color('blue'))
    screen.blit(s, (c*SQ_SIZE, r*SQ_SIZE))
    

def draw_game_state(screen, board, selected_square):
    draw_board(screen)
    highlight_squares(screen, selected_square)
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

def animate_move(screen, board, clock, target, start, piece):
    
    dr = target[0] - start[0]
    dc = target[1] - start[1]
    frames = 10
    frame_count = (abs(dr) + abs(dc) * frames)
    for frame in range(frame_count + 1):
        r, c = (start[0] + dr*frame/frame_count, start[1] + dc*frame/frame_count)
        draw_board(screen)
        draw_pieces(screen, board)
        print(piece)
        screen.blit(IMAGES[repr(piece)], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE)) 
        p.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()



