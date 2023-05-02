import pygame
import os

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

    def calc_moves(self, piece, row, col):
        def knight_moves():
            possible_moves = [
                (row + 1, col + 2),
                (row - 1, col + 2),
                (row + 1, col - 2),
                (row - 1, col - 2),
                (row + 2, col + 1),
                (row - 2, col + 1),
                (row + 2, col - 1),
                (row - 2, col - 1)
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    # print(self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color))
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)

        def king_moves():
            possible_moves = [
                (row + 1, col + 1),
                (row + 1, col - 1),
                (row - 1, col + 1),
                (row - 1, col - 1),
                (row, col + 1),
                (row, col - 1),
                (row + 1, col),
                (row - 1, col)
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                # print(isinstance(self.squares[possible_move_row][possible_move_col].piece, King))
                if Square.in_range(possible_move_row, possible_move_col):
                    # print(self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color))
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)

        def pawn_moves():
            moves = []
            color = self.squares[row][col].piece.color
            if color == 'black' and self.squares[row + 1][col].is_empty():
                moves.append((row + 1, col))
                if row == 1 and self.squares[row + 2][col].is_empty():
                    moves.append((row + 2, col))
            elif color == 'white' and self.squares[row - 1][col].is_empty():
                moves.append((row - 1, col))
                if row == 6 and self.squares[row - 2][col].is_empty():
                    moves.append((row - 2, col))

            if color == 'black':
                if row + 1 < 8 and col + 1 < 8:
                    if self.squares[row + 1][col + 1].has_enemy_piece(piece.color):
                        moves.append((row + 1, col + 1))
                if row + 1 < 8 and col - 1 > -1:
                    if self.squares[row + 1][col - 1].has_enemy_piece(piece.color):
                        moves.append((row + 1, col - 1))

            if color == 'white':
                if row - 1 > -1 and col - 1 > -1:
                    if self.squares[row - 1][col - 1].has_enemy_piece(piece.color):
                        moves.append((row - 1, col - 1))
                if row - 1 > -1 and col + 1 < 8:
                    if self.squares[row - 1][col + 1].has_enemy_piece(piece.color):
                        moves.append((row - 1, col + 1))

            for move in moves:
                initial = Square(row, col)
                final = Square(move[0], move[1])
                move = Move(initial, final)
                piece.add_move(move)
