import engine
import pygame as p
import os


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
    board = mainxd.chess_board
   
    load_images()
    running = True
    selected_square = () # a tuple of selected square (row, column)
    player_clicks = [] #cur players pervious clicks  

    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if selected_square == (row, col): # user has last clicked this square, we unlick
                    selected_square = ()
                    player_clicks = []
                else:    
                    selected_square = (row, col)
                    player_clicks.append(selected_square)
                    #if player_clicks.len == 2: # players second click we make move

                    

        
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
            print(repr(piece))
            if piece != "--":
                screen.blit(IMAGES[repr(piece)], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == '__main__':
    main()



