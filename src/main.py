from const import *
import pygame
import sys
from game import Game
from square import *
from move import *


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.move_screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):

        screen = self.screen
        move_screen = self.move_screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        self.game.show_bg(self.screen)

        while True:
            game.show_bg(screen)
            game.show_moves(move_screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        board.calc_moves(piece, clicked_row, clicked_col)
                        game.show_bg(screen)
                        game.show_moves(move_screen)
                        game.show_pieces(screen)
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        board.calc_moves(piece, clicked_row, clicked_col)
                        game.show_bg(screen)
                        game.show_moves(move_screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)

                # unclick
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.piece.color != game.next_player:
                        dragger.undrag_piece()
                    # elif dragger.dragging:
                    #     dragger.undrag_piece()
                    #     dragger.update_mouse(event.pos)
                    #     released_row = dragger.mouseY // SQSIZE
                    #     released_col = dragger.mouseX // SQSIZE
                    #     valid_moves = []
                    #     for move in piece.moves:
                    #         valid_moves.append((move.final.row, move.final.col))
                    #     if (released_row, released_col) in valid_moves:
                    #         initial = Square(clicked_row, clicked_col)
                    #         final = Square(released_row, released_col, piece)
                    #         move = Move(initial, final)
                    #         board.move(piece, move)
                    #         game.next_turn()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
