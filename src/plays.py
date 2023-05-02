from const import *
from board import Board
from dragger import Dragger
from square import Square

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.board = Board()
        self.dragger = Dragger()

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (174, 137, 104)
                else:
                    color = (236, 218, 185)
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)


    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):

                # print(row, col != 1, 0)
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            for move in piece.moves:
                color = '#808080'
                x = move.final.col * SQSIZE + (SQSIZE // 2)
                y = move.final.row * SQSIZE + (SQSIZE // 2)
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.circle(surface, color, (x, y), 20, 5)

    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'../assets/images/imgs-{size}px/{self.color}_{self.name}.png')

    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []