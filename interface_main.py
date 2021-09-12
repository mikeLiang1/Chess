import pygame as p
import os
import core
import copy


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
  
    moves = []
    load_images()
    running = True
    selected_square = () # a tuple of selected square (row, column)

    while running:
        board = core.chess_board
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            elif event.type == p.KEYDOWN:
                if event.key == p.K_z:
                    core.undoMove()
            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                #core.get_all_available_moves(core.cur_turn)
                if selected_square == (): #first click
                    if board[row][col] != "--" and board[row][col].colour == core.cur_turn: # only if i clicked on a piece i can move it        
                        selected_square = (row, col)   
                        moves = board[row][col].get_available_moves()  
                        if core.is_in_check(core.cur_turn):
                            print("hi")
                            
                            
                            # print(new_moves) 
                            for move in moves:
                                print(move)
                                if board[row][col].move_cap(move[0], move[1]) == True:

                                    core.undoMove()
                                    core.flip_sides()
                            print(core.cur_turn)
                            
                            # board[row][col].move_cap(new_moves[0][0], new_moves[0][1])
                            # if (core.is_in_check(core.cur_turn)):
                            #     print("szztill in check")
                            # core.undoMove()
                            # #core.flip_sides
                                
                             
                        print(moves)
                        #print(core.bQ.available_moves)                  
                else: #second click
                    if selected_square != (row,col):  # if didnt click same spot
                        #print("not clicked on smae sqaure")
                        if board[selected_square[0]][selected_square[1]].move_cap(row, col) == True:  # if clicked on available move sqaure
                            core.flip_sides()                         
                            #animate_move(screen, board, clock, (row,col), selected_square, board[row][col])
                            #highlight_move(screen, selected_square, (row,col))
                    
                    selected_square = ()
                     
        draw_game_state(screen, board, selected_square, moves)
        clock.tick(MAX_FPS)
        p.display.flip()
    
#def highlight_move(screen, target, current):


# highlight sqaure selected and posibble moves
def highlight_squares(screen, selected_sq, moves, board):
    if (selected_sq == ()):
        return
    r,c = selected_sq
    s = p.Surface((SQ_SIZE, SQ_SIZE))
    s.set_alpha(100)
    s.fill(p.Color('blue'))
    screen.blit(s, (c*SQ_SIZE, r*SQ_SIZE))

    #highlight moves
    for move in moves:
        r, c = move
        s.fill(p.Color(0, 255, 255))
        if board[r][c] != core.EMPTY:
            s.fill(p.Color(238, 29, 35))
        screen.blit(s, (c*SQ_SIZE, r*SQ_SIZE))
    

def draw_game_state(screen, board, selected_square, moves):
    draw_board(screen)
    highlight_squares(screen, selected_square, moves, board)
    draw_pieces(screen, board)

def draw_board(screen):
    colors = [p.Color("white"), p.Color(254, 211, 169)]
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
    frames = 20
    
    frame_count = (abs(dr) + abs(dc) * frames)
        
    for frame in range(frame_count + 1):
        r, c = (start[0] + dr*frame/frame_count, start[1] + dc*frame/frame_count)
        draw_board(screen)
        draw_pieces(screen, board)
        screen.blit(IMAGES[repr(piece)], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE)) 
        p.display.flip()          
        clock.tick(60)

if __name__ == '__main__':
    main()



