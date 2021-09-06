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
    pieces = ['wp', 'wR', 'wN', 'wB', "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".png"), (SQ_SIZE, SQ_SIZE))
       

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = engine.gameState()
    load_images()
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def draw_game_state(screen, gs):
    draw_board(screen)
    
    draw_pieces(screen, gs.board)

def draw_board(screen):
    colors = [p.Color("white"), p.Color("pink")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) %2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE,SQ_SIZE))
    
def draw_pieces(screen, board):
    pass

if __name__ == '__main__':
    main()



